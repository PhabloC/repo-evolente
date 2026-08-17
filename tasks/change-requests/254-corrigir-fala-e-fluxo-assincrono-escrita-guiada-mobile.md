# Task 254 - Corrigir fala e fluxo assíncrono da escrita guiada mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/030-escrita-guiada-de-letras.md`

## Dependencias

- Task 167
- Task 169
- Task 227

## Objetivo

Corrigir regressões no runtime da escrita guiada para que interrupções de fala não deixem promessas pendentes e para que a próxima instrução seja reproduzida uma única vez após cada acerto.

## Entrega verificavel

- `stopGameSpeech` encerra de forma determinística a fala ativa sem deixar promessas pendentes
- Nova reprodução cancela ou resolve a promessa anterior com segurança
- Após um acerto, a instrução da próxima letra é falada apenas uma vez
- Testes cobrindo cancelamento/interrupção da fala e prevenção de replay duplicado

## Fora de escopo

- Mudanças de layout do jogo
- Novos efeitos sonoros ou vozes gravadas
- Alterações no catálogo, backend ou web

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-167.md`
- `.agents/state/handoffs/TASK-169.md`
- `.agents/state/handoffs/TASK-227.md`

## Contexto sob demanda

- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.test.tsx`

## Orcamento de contexto

baixo

## Estrategia de reducao

Restringir a mudança ao serviço de fala e ao renderer da escrita guiada, sem reabrir outros renderers, tela de trilha ou contrato de conteúdos.

## Referencia visual

- nao se aplica

## Resultado da execucao

- `gameSpeechService` agora encerra a promessa ativa ao parar a fala, tratando também `onStopped`
- Cancelamentos de fala não disparam fallback tardio nem deixam o fluxo anterior pendurado
- `AlphabetWritingGameRenderer` passou a reproduzir a próxima instrução apenas pelo efeito reativo de `currentLetter`
- Foram adicionados testes para interrupção da fala e para evitar replay duplicado após acerto

## Contexto utilizado

- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.test.tsx`
- `.agents/state/handoffs/TASK-167.md`
- `.agents/state/handoffs/TASK-169.md`
- `.agents/state/handoffs/TASK-227.md`

## Handoff

- `.agents/state/handoffs/TASK-254.md`

## Arquivos alterados

- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/services/gameSpeechService.test.ts`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.test.tsx`

## Validacoes executadas

- `cd mobile && npm run test -- gameSpeechService AlphabetWritingGameRenderer` — ok
- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- Validar em dispositivo real interrupções rápidas de fala ao tocar “Ouvir” repetidamente
- Validar no fluxo real que o próximo prompt não reinicia a fala após cada acerto

## Status final

done
