#!/usr/bin/env python3
"""Limpa uma gravação de fala: tira silêncios e respirações, aplica cortes à mão e nivela o som.

Receita do vídeo do portfólio (esteira, docs/research/2026-11-03-editar-gravacao-bruta-longa.md):
silencedetect a -38 dB por 0,3 s, 0,12 s de margem de cada lado, afade de 12 ms nas pontas,
highpass 80 Hz e loudnorm -16 LUFS. No fim transcreve o resultado para conferir.

Uso:
  python3 cortar/limpar.py brutos/carol-2.mov            # só tira as pausas
  python3 cortar/limpar.py brutos/carol-2.mov --cortar 3.2-5.8 12-14.1   # e corta trechos (segundos do bruto)
  python3 cortar/limpar.py brutos/carol-2.mov --so-transcrever          # vê o texto com tempos antes de cortar
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent.parent
TRAB = AQUI / "trabalho"; SAIDA = AQUI / "saida"
MODELO = Path.home() / "Claude/esteira/models/ggml-large-v3-turbo.bin"
FADE = 0.012

def rodar(*cmd, **kw):
    return subprocess.run(list(map(str, cmd)), check=True, capture_output=True, text=True, **kw)

def duracao(f):
    # A menor duração entre vídeo e áudio: celular às vezes grava um mais longo que o outro.
    saida = rodar("ffprobe", "-v", "error", "-show_entries", "stream=duration", "-of", "csv=p=0", f).stdout
    return min(float(x) for x in saida.split() if x not in ("", "N/A"))

def wav16k(f, destino):
    rodar("ffmpeg", "-v", "error", "-y", "-i", f, "-ar", "16000", "-ac", "1", destino)

def transcrever(wav, base):
    rodar("whisper-cli", "-m", MODELO, "-l", "pt", "-ojf", "-np", "-of", base, "-f", wav)
    dados = json.load(open(f"{base}.json"))
    linhas = []
    for seg in dados.get("transcription", []):
        a = seg["offsets"]["from"] / 1000; b = seg["offsets"]["to"] / 1000
        linhas.append(f"{a:7.2f}–{b:6.2f}  {seg['text'].strip()}")
    return "\n".join(linhas)

def trechos_com_fala(f, dur, limiar, minimo, margem):
    log = subprocess.run(["ffmpeg", "-i", str(f), "-af", f"silencedetect=n={limiar}dB:d={minimo}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    if len(fim) < len(ini): fim.append(dur)
    trechos, atual = [], 0.0
    for a, b in zip(ini, fim):
        if a <= 0.01: atual = max(0, b - 0.1); continue
        a2 = a + margem; b2 = b - margem if b < dur - 0.01 else b
        if b2 > a2: trechos.append((atual, a2)); atual = b2
    if atual < dur - 0.05: trechos.append((atual, dur))
    return trechos

def tirar(trechos, cortes):
    for ca, cb in cortes:
        novo = []
        for a, b in trechos:
            if b <= ca or a >= cb: novo.append((a, b))
            else:
                if a < ca: novo.append((a, ca))
                if b > cb: novo.append((cb, b))
        trechos = novo
    return [(round(a, 3), round(b, 3)) for a, b in trechos if b - a >= 0.12]

def montar(f, trechos, destino, acelerar):
    fc, rot = [], ""
    for k, (a, b) in enumerate(trechos):
        L = b - a
        fc.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{k}]")
        fc.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d={FADE},afade=t=out:st={L-FADE:.3f}:d={FADE}[a{k}]")
        rot += f"[v{k}][a{k}]"
    fc.append(f"{rot}concat=n={len(trechos)}:v=1:a=1[vc][ac]")
    v = f"[vc]setpts=PTS/{acelerar}[v]" if acelerar != 1 else "[vc]null[v]"
    a = f"[ac]{'atempo=' + str(acelerar) + ',' if acelerar != 1 else ''}highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11[a]"
    fc += [v, a]
    script = TRAB / (Path(destino).stem + ".fc"); script.write_text(";\n".join(fc))
    rodar("ffmpeg", "-v", "error", "-y", "-i", f, "-/filter_complex", script, "-map", "[v]", "-map", "[a]",
          "-r", "30", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
          "-c:a", "aac", "-b:a", "192k", "-ar", "48000", destino)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("bruto")
    p.add_argument("--cortar", nargs="*", default=[], help="trechos a tirar, em segundos do bruto: 3.2-5.8")
    p.add_argument("--limiar", type=float, default=-38, help="dB abaixo do qual é silêncio")
    p.add_argument("--minimo", type=float, default=0.3, help="segundos de silêncio para cortar")
    p.add_argument("--margem", type=float, default=0.12, help="segundos mantidos de cada lado da pausa")
    p.add_argument("--acelerar", type=float, default=1.0, help="1.04 não se percebe")
    p.add_argument("--so-transcrever", action="store_true")
    a = p.parse_args()
    f = Path(a.bruto).resolve(); nome = f.stem
    TRAB.mkdir(exist_ok=True); SAIDA.mkdir(exist_ok=True)
    wav = TRAB / f"{nome}.wav"; wav16k(f, wav)
    print("Bruto:\n" + transcrever(wav, TRAB / nome))
    if a.so_transcrever: return
    dur = duracao(f)
    cortes = [tuple(map(float, c.split("-"))) for c in a.cortar]
    trechos = tirar(trechos_com_fala(f, dur, a.limiar, a.minimo, a.margem), cortes)
    destino = SAIDA / f"{nome}-limpo.mp4"
    montar(f, trechos, destino, a.acelerar)
    novo = sum(b - x for x, b in trechos) / a.acelerar
    print(f"\n{nome}: {dur:.1f}s → {novo:.1f}s, {len(trechos)} trechos → {destino}")
    wav2 = TRAB / f"{nome}-limpo.wav"; wav16k(destino, wav2)
    print("Resultado (conferir se nenhuma sílaba ficou solta):\n" + transcrever(wav2, TRAB / f"{nome}-limpo"))

if __name__ == "__main__":
    main()
