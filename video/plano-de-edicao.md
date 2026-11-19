# Plano de edição do pitch (o que a esteira e o Mira já ensinaram)

> Fontes: `~/Claude/esteira/docs/research/2026-11-03-motor-de-edicao-de-reels.md`,
> `2026-11-03-editar-gravacao-bruta-longa.md`, `~/Claude/mira/docs/adr/0017-musica-pelo-clima-do-corte.md`,
> `mira/docs/research/2026-11-07-efeitos-sonoros-meme.md` e o projeto Remotion do JOVI.

## Os seis elementos que fazem o vídeo prender
| Elemento | No pitch da Garoa |
|---|---|
| Cortes (ritmo) | Tirar pausas e recomeços da Carol e da narração; corte seco entre câmera e slide |
| Transições | Whoosh curto entre trechos; a gota da Garoa como transição de marca |
| Efeitos | Zoom lento (Ken Burns) nas cenas de IA e na foto do time |
| Motion graphics | Os slides animados: 92,5%, cartões de tecnologia, mapa do ecossistema, setas no app |
| Legenda dinâmica | Palavras-chave em rosa-ipê, não a fala inteira |
| Sons | Música por clima e poucos efeitos, sem abafar a voz |

## Ferramenta: o Remotion do JOVI, não começar do zero
- `~/FIAP/challenge-JOVI/entrega-cp1-sprint4/motion` já roda: React, fontes do Google, cenas, narração e efeitos (`gerar-efeitos-v8.mjs`, `gerar-trilha-v2.mjs`). Copiar a estrutura para `gs-storytelling-pitch/video/motion/`.
- O ffmpeg do Homebrew vem **sem** `drawtext`/libass: texto e legenda vão pelo Remotion, não pelo ffmpeg.
- Antes de renderizar, mostrar "cartões" de cada trecho para o Sávio aprovar. Referência visual (um motion que já ficou bom) faz o modelo repetir o estilo.

## Receita para o áudio da Carol e da narração
1. Transcrever com tempo por palavra: `whisper-cli -m ~/Claude/esteira/models/ggml-large-v3-turbo.bin -l pt -ojf`.
2. Pausas: `silencedetect=n=-38dB:d=0.3`, deixando 0,12 s de cada lado.
3. Cortar frase repetida ou que morre no meio; cortar onde a frase continua gramatical.
4. Cada pedaço com `afade` de 12 ms nas pontas (sem estalo), depois `concat`.
5. Final: `highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11`. Aceleração de 1,04 passa despercebida se faltar tempo.
6. Conferir **transcrevendo o resultado**. O Whisper erra nome próprio (Garoa, UBS, CRAS): revisar a legenda à mão.

## Música (licença limpa, já baixada no Mira)
Biblioteca de Áudio do YouTube: monetizável, sem crédito e **sem Content ID**. Arquivos em `~/Claude/mira/dados/musica/` (não vão para o git).
| Trecho | Clima | Sugestão |
|---|---|---|
| 1 a 3 (abertura e problema) | tensão | "Midnight Trace" ou "Shadow Chase" (Jimena Contreras) |
| 4 a 9 (solução até o fim) | leve | "On The Eve" ou "A Stroll" (The Grey Room) |
- Virada da trilha exatamente em "Por isso criamos a Garoa" (trecho 4). O Mira mede a "explosão" de cada faixa e alinha com o momento principal: fazer o mesmo.
- Música baixa debaixo da voz (uns −18 dB abaixo da fala).

## Efeitos sonoros
- Fontes seguras: Biblioteca de Áudio do YouTube, Pixabay, Freesound só **CC0**. Nada de soundboard de meme.
- Já tem um whoosh CC0 conferido no Mira (`dados/amostras/sfx/whoosh.wav`, "Whoosh" de qubodup, Freesound #60013).
- Poucos: whoosh nas transições, um "ding" suave quando a gota acende, chuva de fundo na abertura.

## Gancho
Os dois primeiros segundos decidem: abrir em tensão, número ou reversão, nunca em apresentação. A abertura com o quarto e o mofo já faz isso.

## Subir no YouTube
- Não listado. Conferir sem login: `https://www.youtube.com/oembed?url=<link>&format=json` responde se abre.
- Testar o link numa janela anônima (pedido da disciplina) antes de colar no e-mail.
