# Roteiro do videopitch da Garoa (até 3 min)

> A parede conta a história. Tom do arquétipo **Cuidador**: acolhedor e firme, sem culpar ninguém.
> **Carol** aparece de frente para a câmera nos trechos dela. **Sávio** narra o resto, por cima das cenas e dos slides.
> Cerca de 420 palavras faladas (ritmo calmo, uns 140 por minuto).

Legenda do que aparece: **IA** = cena gerada (fal, MiniMax H3) · **Motion** = slide animado (HyperFrames) · **App** = gravação de tela do app · **Câmera** = Carol gravada · **Wokwi** = trecho do vídeo do Victor.

| # | Tempo | Etapa | Quem | Texto falado | O que aparece |
|---|---|---|---|---|---|
| 1 | 0:00–0:15 | Abertura de impacto | Sávio (narração, voz baixa) | "Toda noite, ela tenta avisar. Ela sua, ela mancha, ela escurece atrás do guarda-roupa. Mas ninguém escuta a parede." | **IA** cena 01 (quarto à noite, criança dormindo, câmera chega no mofo). **Motion** por cima no fim: a gota da Garoa acende e a frase "a parede fala." |
| 2 | 0:15–0:35 | Quem é o cidadão | Carol (câmera) | "Essa é a casa de muitas famílias de São Paulo. Gente que mora de aluguel, em casa úmida e fria, com criança pequena, muitas vezes com asma ou rinite. Em Heliópolis e Vila Prudente, um levantamento encontrou umidade ou infiltração em noventa e dois e meio por cento das casas visitadas." | **Câmera** em tela cheia. Corte seco para **Motion**: "92,5%" gigante, "de 600 casas com umidade ou infiltração", fonte pequena (CEFAVELA/UFABC, preliminar). |
| 3 | 0:35–0:55 | O problema | Sávio (narração) | "O mofo cresce escondido e adoece quem dorme ali. E quando a família reclama com o dono do imóvel, ouve a pior frase: 'a culpa é de vocês, que não abrem a janela'. Sem prova, a conversa acaba aí." | **IA** cena 02 (mãe olhando a parede manchada, celular na mão). **Motion** por cima: balão "a culpa é de vocês" riscado. |
| 4 | 0:55–1:35 | A solução e a proposta de valor | Carol (câmera, 10 s) e depois Sávio (narração) | Carol: "Por isso criamos a Garoa. A parede fala." · Sávio: "Um sensor barato mede o ar e a parede fria de cada cômodo, até atrás do guarda-roupa, onde o mofo começa. A Garoa calcula o ponto de orvalho e avisa antes do mofo aparecer. Responde a pergunta de todo dia: abro a janela? E cada mancha, cada crise de asma e cada aviso ao dono vão para um diário, que vira um laudo para imprimir, com data, hora e a lei do inquilinato. O que antes era só a palavra da família vira registro." | **Câmera** curta. Depois **App**: tela Agora com a cena viva (parede ilustrada suando, garoa e mofo crescendo) e o estado "Risco de mofo: Há condições para o mofo crescer"; cartão "Abra a janela agora" / "Mantenha a janela fechada"; Diário com "Avisei o dono"; Laudo. **Motion**: setas e rótulos sobre o app. |
| 5 | 1:35–1:55 | As tecnologias | Sávio (narração) | "Por trás, um ESP32 com sensores no ar e na parede decide sozinho, mesmo sem internet, e manda as medições para o app. O app web, que também funciona sem internet, compara com o clima real da rua, hora a hora. E um modelo matemático com dados do INMET mostra quando a janela vale a pena." | **Wokwi** (vídeo do Victor, LED e LCD mudando de estado) e **App** (Adicionar sensor). **Motion**: três cartões "Sensor ESP32 · App web (PWA) · Modelo matemático". |
| 6 | 1:55–2:15 | O ecossistema | Carol (câmera) | "A Garoa não trabalha sozinha. O laudo pode chegar à UBS, que acompanha a saúde da criança, ao CRAS, e à Defensoria Pública, que defende o direito à moradia digna. E as associações de moradores levam o sensor de casa em casa." | **Câmera** com **Motion** ao lado: mapa simples com ícones UBS, CRAS, Defensoria, associação de bairro ligados à gota. |
| 7 | 2:15–2:35 | Impacto: medir e ampliar | Sávio (narração) | "Vamos medir em horas de risco de mofo por cômodo, e em crises de asma, idas ao pronto-socorro e faltas na escola que a própria família registra. Começamos em Heliópolis e Vila Prudente e podemos chegar a qualquer bairro onde a parede chora." | **Motion**: gráfico simples de "horas de risco" caindo. **IA** cena 03 (bairro de SP na garoa, vista de cima). |
| 8 | 2:35–2:50 | O time | Sávio (narração) | "Somos cinco: Ana, no design da experiência; Arthur, no modelo matemático e no Python; Carolina, na marca e na história; Sávio, no app; e Victor, no sensor." | **Motion** com a foto da equipe sem fundo (`slides/imagens/equipe-sem-fundo.png`): seta e nome entram em cada pessoa. |
| 9 | 2:50–3:00 | Encerramento memorável | Carol (câmera, olhando firme) | "A parede sempre soube. Sem a Garoa, ela só ia mofar. Com a Garoa, ela fala." | **Câmera** e corte para **Motion** final: logo da Garoa, "a parede fala.", nomes e RMs pequenos. |

## Cenas de IA para gerar (fal, MiniMax H3, 5 s, 16:9)
- [x] **01 Abertura:** quarto à noite, chuva, criança dormindo, câmera chega no mofo atrás do guarda-roupa (`video/cenas/01-abertura-mofo-teste.mp4`).
- [ ] **02 Problema:** mãe de uns 30 anos, de costas ou de perfil, olhando a parede manchada da sala com o celular na mão; luz de fim de tarde, casa simples de SP.
- [ ] **03 Impacto:** vista aérea de um bairro de São Paulo (casas de bloco, lajes) sob garoa fina, amanhecendo.
- [ ] **Reserva:** close de gotas de água condensando numa parede fria, em câmera lenta (cobre transições).

## Gravações
- **Carol (câmera):** trechos 2, 4 (só a primeira frase), 6 e 9. Celular na horizontal, luz de janela de frente, fundo neutro. Gravar cada trecho 2 ou 3 vezes.
- **Sávio (voz):** trechos 1, 3, o resto do 4, 5, 7 e 8. Gravar num lugar silencioso, celular a um palmo da boca.
- **App** (garoa-seven.vercel.app, casa de demonstração do Jabaquara, com 14 dias de medições). Gravar em 1080p, com o cursor calmo:
  1. **Agora:** a cena viva do cômodo mais urgente e a resposta "Abro a janela?" (trecho 4).
  2. **Simular:** "banho quente" e "madrugada fria", a parede indo de Tudo certo para Risco de mofo e Condensação (trecho 4 ou transição).
  3. **Cômodo:** gráfico parede × rua e os últimos 14 dias (trecho 7, "horas de risco").
  4. **Diário:** uma anotação e o "Avisei o dono" (trecho 4).
  5. **Laudo:** rolar o documento até "Isto não é perícia" e a base legal (trecho 4 e 6).
  6. **Adicionar sensor:** o ESP32 aparecendo para conectar (trecho 5).

## Conferência com os critérios
| Critério | Onde está |
|---|---|
| Cidadão e problema (2,0) | Trechos 2 e 3 |
| Solução e proposta de valor (2,0) | Trecho 4 |
| Tecnologias e coerência (1,5) | Trecho 5 |
| Storytelling e qualidade do vídeo (2,0) | A parede como fio da história, do 1 ao 9 |
| Branding (2,5) | Lema "a parede fala", tom Cuidador, rosa-ipê nos slides; o e-mail da Carol fecha a parte do arquétipo |
