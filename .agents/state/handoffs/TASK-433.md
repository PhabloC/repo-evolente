# Handoff — Task 433

## Identificador

- task: 433
- título: Complete a palavra: catálogo, níveis, TTS e runtime
- slice: 043
- status final: done

## Decisões preservadas

- `gameType: word-spell`, categoria de conteúdo `leitura` (grupo UI “Leitura e escrita”)
- `roundsPerRun: 10`; categorias bootstrap: insetos, animais, frutas, transporte
- dificuldades `facil` / `medio` / `dificil` (difícil = `parts` com 2 palavras)
- `voiceMode: tts` no MVP; botão TTS fala `word.label`
- tiles = shuffle(letras de `parts` + `distractors`); gap visual entre parts

## Contexto mínimo lido

- AGENTS.md / task 433 / slice 043

## Contexto sob demanda carregado

- padrões sentence-fill, odd-one-out upload, word-search setup
- `word-spell-game-assets.ts`

## Arquivos alterados

- contrato, backend (service/bootstrap/spec/in-memory/upload), STORAGE_BUCKET_MAP
- front-end types + WordSpellPreviewModal + wiring
- mobile types + WordSpellGameRenderer + wiring
- task/slice/index/handoff

## Validacoes executadas

- bootstrap unit tests: 8 passed

## Pendências

- pasta `jogo_complete_a_palavra/` com capas + items (parent)
- upload S3 via script após assets

## Próxima ação sugerida

Adicionar assets, upload, reiniciar backend e validar “Complete a palavra” na biblioteca.

## Próximo contexto recomendado

- `jogo_complete_a_palavra/` + `STORAGE_BUCKET_MAP.md` §15
- não recarregar specs de outros jogos salvo regressão

## Contexto que não deve ser carregado

- next-js, Asaas, memória articulação
