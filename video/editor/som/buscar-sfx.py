#!/usr/bin/env python3
"""Busca efeito sonoro de licença livre no Openverse (API aberta, sem chave) e baixa para som/sfx/.

Só CC0 por padrão (sem crédito, sem risco). Registra fonte e licença em som/sfx/LICENCAS.md.
Uso:
  python3 som/buscar-sfx.py "rain window" --listar      # vê as opções
  python3 som/buscar-sfx.py "rain window" --baixar 2 --nome chuva
"""
import argparse, json, urllib.parse, urllib.request
from datetime import date
from pathlib import Path

PASTA = Path(__file__).resolve().parent / "sfx"
API = "https://api.openverse.org/v1/audio/"

def buscar(termo, licenca):
    q = urllib.parse.urlencode({"q": termo, "license": licenca, "page_size": 10})
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": "garoa-pitch/1.0"})
    return json.load(urllib.request.urlopen(req, timeout=30))["results"]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("termo")
    p.add_argument("--licenca", default="cc0")
    p.add_argument("--listar", action="store_true")
    p.add_argument("--baixar", type=int, help="número da opção na lista")
    p.add_argument("--nome")
    a = p.parse_args()
    res = buscar(a.termo, a.licenca)
    for i, r in enumerate(res, 1):
        dur = (r.get("duration") or 0) / 1000
        print(f"{i:2}. {r['title'][:50]:50} {dur:5.1f}s  {r['license']}  {r.get('provider')}  {r['foreign_landing_url']}")
    if a.baixar:
        r = res[a.baixar - 1]
        ext = (r.get("filetype") or Path(urllib.parse.urlparse(r["url"]).path).suffix.lstrip(".") or "mp3")
        destino = PASTA / f"{a.nome or r['id']}.{ext}"
        req = urllib.request.Request(r["url"], headers={"User-Agent": "garoa-pitch/1.0"})
        destino.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        linha = f"| {destino.name} | \"{r['title']}\", {r.get('creator')}, {r['foreign_landing_url']} | {r['license'].upper()} | {date.today():%d/%m/%Y} |\n"
        with open(PASTA / "LICENCAS.md", "a") as f: f.write(linha)
        print(f"\nbaixado: {destino}")

if __name__ == "__main__":
    main()
