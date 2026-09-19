# Task 712 - Áudio pós-acerto da memória de articulação

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem alteração de endpoint; o campo é persistido dentro do `gameConfig` existente

## Modo de execucao

cross-stack

## Slice vertical

- Slice 034 - Jogo da memória de articulação
- `tasks/slices/034-jogo-memoria-articulacao.md`

## Objetivo

Publicar o áudio “Agora faça o exercício descrito na carta” e reproduzi-lo após o término do feedback “Muito bem!” ao acertar um par no jogo da memória de articulação.

## Dependencias

- Task 408
- Task 409
- Task 527

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/034-jogo-memoria-articulacao.md`
- `tasks/change-requests/527-feedbacks-curtos-compartilhados-voz.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| upload e vínculo | `backend/scripts/upload-game-session-audios.mjs` + assets do jogo | publicar MP3 e atualizar o `gameConfig` |
| runtime mobile | `mobile/src/features/games/components/MemoryGameRenderer/` e `GameSessionAudio/` | encadear os áudios após o acerto |
| prévia web | `front-end/src/pages/Main/Library/GamePreviewModal.tsx` e feedback compartilhado | manter o mesmo comportamento na prévia |

## Orçamento de contexto

- risco: baixo; mudança limitada a áudio de sessão e sequência de feedback

## Critérios de aceite

- [x] áudio publicado em `dev/games/memoria_articulacao/audio/instrucao-exercicio.mp3`
- [x] URL vinculada em `exerciseInstructionAudioUrl` do jogo de articulação
- [x] “Muito bem!” termina antes da instrução do exercício no mobile
- [x] prévia web mantém a mesma sequência
- [x] fallback TTS preservado quando o MP3 não estiver disponível

## Resultado da execucao

- O script oficial publicou o arquivo local `audios-atividades/jogo_memoria_articulacao/mulher-2026-09-18-21-55-[excited]Agora-faça-o-exercício-descrito-na-cart.mp3` e atualizou o conteúdo no banco.
- O runtime aguarda `announcePraise()` antes de `announceExerciseInstruction()`; o player gravado resolve apenas no fim do MP3.
- O bootstrap gera/preserva o campo apenas para `memoria_articulacao`.

## Contexto utilizado

- Slice 034, Task 527, script de upload, bootstrap de catálogo, serviço de áudio mobile, preview web e tipos de `MemoryGameConfig`.

## Handoff

- Campo de configuração: `exerciseInstructionAudioUrl`.
- Chave pública: `games/memoria_articulacao/audio/instrucao-exercicio.mp3`.
- Próximo contexto recomendado: smoke manual no app e na prévia web acertando um par com áudio habilitado.

## Arquivos alterados

- `backend/scripts/upload-game-session-audios.mjs`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/game-session-audio-assets.ts`
- `backend/src/modules/contents/memory-articulation-game-assets.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/game-session-audio-assets.spec.ts`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/memoryGame.ts`
- `front-end/src/pages/Main/Library/librarySharedFeedback.ts`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/memoryGame.ts`
- `mobile/src/features/games/components/GameSessionAudio/index.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`

## Validacoes executadas

- `npm run upload:game-session-audios` — passou; upload e vínculo confirmados no log.
- `backend`: teste isolado `game-session-audio-assets.spec.ts` — passou (4 testes).
- `backend`, `mobile` e `front-end`: checks globais ainda possuem erros preexistentes fora deste escopo.
- teste mobile da memória não iniciou por falha do mock nativo existente de `expo-audio` (`Cannot read properties of undefined (reading 'prototype')`).

## Pendencias pos-task

- Smoke manual no dispositivo/navegador para confirmar a audição com o catálogo atualizado.

## Status final

done
