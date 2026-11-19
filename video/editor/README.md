# Editor do pitch da Garoa

Montado em 18/11/2026 juntando o que já funcionou em outros projetos: os cortes do vídeo do
portfólio, as regras de som e música do Mira, o motor de edição estudado na esteira e as
ferramentas dos reels (HyperFrames, Openverse, Earshot, /watch). Plano completo em
[`../plano-de-edicao.md`](../plano-de-edicao.md); roteiro em [`../../roteiro/roteiro-3min.md`](../../roteiro/roteiro-3min.md).

## Pastas
| Pasta | O quê |
|---|---|
| `brutos/` | gravações da Carol, a narração do Sávio e as gravações de tela do app (fora do git) |
| `cortar/limpar.py` | tira pausas e respirações, aplica cortes à mão, nivela o som e confere transcrevendo |
| `som/musica/` | 4 faixas da Biblioteca de Áudio do YouTube (tensão e leve), fora do git |
| `som/sfx/` | efeitos CC0 (whoosh, chuva na janela, gota) e `LICENCAS.md` |
| `som/buscar-sfx.py` | busca e baixa mais efeitos CC0 no Openverse, anotando a licença |
| `saida/` | o que sai do `limpar.py` (fora do git) |
| `../motion/` | projeto HyperFrames (identidade da Garoa já aplicada) para slides, textos e a montagem final |
| `../cenas/` | cenas geradas por IA (fal, MiniMax H3) |

## Passo a passo quando o material chegar
1. Pôr os arquivos em `brutos/` com nome do trecho: `carol-2.mov`, `carol-4.mov`, `savio-1.m4a`...
2. Ver o texto com os tempos: `python3 cortar/limpar.py brutos/carol-2.mov --so-transcrever`.
3. Limpar: `python3 cortar/limpar.py brutos/carol-2.mov --cortar 3.2-5.8` (os tempos do que sobra de erro ou repetição). Sai em `saida/carol-2-limpo.mp4`, já transcrito para conferir.
4. Montar no HyperFrames (`../motion`): cada trecho do roteiro vira uma cena; câmera, cena de IA ou gravação do app por baixo, motion por cima, música e efeitos na trilha. `npm run dev` para ver, `npm run render` para gerar.
5. Revisar: assistir com o /watch (quadro a quadro) e ouvir com o Earshot antes de subir.
6. YouTube não listado, testar em janela anônima, colar o link no `email-arquetipo.md`.

## Ferramentas instaladas no Mac (18/11/2026)
- Plugin `hyperframes@hyperframes` no Claude Code e CLI `npx hyperframes@0.9.69` (Node 24).
- Plugin `watch@claude-video` (o Claude assiste um vídeo: quadros e transcrição). Vale a partir de uma sessão nova.
- `earshot` (uv) como MCP no Claude Code, modelos de áudio já baixados.
- `whisper-cli` com `~/Claude/esteira/models/ggml-large-v3-turbo.bin` e `ffmpeg` 8 (sem `drawtext`: texto vai pelo HyperFrames).

Testado: `limpar.py` tirou as pausas de uma fala de 11,6 s para 9,0 s e a transcrição do resultado saiu inteira; o HyperFrames renderizou um cartão de 3 s com as fontes do app em 6,6 s.
