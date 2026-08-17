# Handoff - Task 254

## Task

- identificador: 254
- título: Corrigir fala e fluxo assíncrono da escrita guiada mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 030
- objetivo de negócio: manter a escrita guiada estável quando a fala é interrompida ou quando a próxima letra é carregada após acerto

## Decisões preservadas

- `expo-speech` continua sendo a base de voz do jogo
- Cancelamento de fala deve resolver a promessa ativa como `stopped`, sem fallback tardio
- A próxima instrução da escrita guiada deve ser falada apenas pelo efeito ligado a `currentLetter`

## Contexto efetivamente usado

- task 254, índice, slice 030
- handoffs `TASK-167`, `TASK-169` e `TASK-227`
- docs locais `mobile/docs/ai/AGENTS.md` e `CODE_STYLE.md`
- serviço `gameSpeechService` e renderer `AlphabetWritingGameRenderer`

## Arquivos alterados

- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.test.tsx`

## Validacoes executadas

- `cd mobile && npm run test -- gameSpeechService AlphabetWritingGameRenderer` — ok
- `cd mobile && npm run typecheck` — ok

## Pendencias ou bloqueios

- Falta smoke test manual em dispositivo real para interrupções muito rápidas de fala e avanço entre letras

## Próximo contexto recomendado

- `mobile/src/features/games/components/AlphabetGameRenderer/index.tsx`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `tasks/slices/028-runtime-jogos-mobile-extensivel.md` se surgir novo ajuste transversal no TTS
