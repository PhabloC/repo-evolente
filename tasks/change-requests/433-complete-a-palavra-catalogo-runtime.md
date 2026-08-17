# Task 433 - Complete a palavra: catálogo, níveis, TTS e runtime

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `ContentGameType`, `WordSpellGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/043-complete-a-palavra.md`

## Referencia visual

- print: `design-system/front/prints/complete-a-palavra-ortografia.png`
- governa: categoria, progresso 0/10, TTS, figura, slots, teclado de letras
- lacunas: moedas fora de escopo; capa gerar; níveis fácil/médio/difícil

## Objetivo

Criar `word-spell` em `leitura` com múltiplas categorias, 10 palavras por partida, letras embaralhadas, TTS e dificuldades (fácil → médio → difícil com duas palavras).

## Orçamento de contexto

- risco: medio

## Criterios de aceite

- [x] Contrato e enums
- [x] Bootstrap `leitura` com categorias e 3 dificuldades
- [x] Setup categoria + dificuldade; progresso 0–10
- [x] TTS no botão; letras embaralhadas
- [x] Difícil com duas palavras
- [x] Prévia web + mobile

## Resultado da execucao

Jogo `word-spell` (`Complete a palavra`) wired end-to-end: OpenAPI, validação backend, bootstrap em `leitura` com 4 categorias e `roundsPerRun: 10`, prévia web com setup/play (slots + tiles + TTS + shake), runtime mobile equivalente, script de upload e seção 15 do `STORAGE_BUCKET_MAP.md`. Assets binários em `jogo_complete_a_palavra/` ficam a cargo do parent.

## Contexto utilizado

- task 433, slice 043
- padrões sentence-fill / odd-one-out / word-search
- `word-spell-game-assets.ts` já existente

## Handoff

- `.agents/state/handoffs/TASK-433.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/scripts/upload-word-spell-assets.mjs`
- `STORAGE_BUCKET_MAP.md`
- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/wordSpellGame.ts`
- `front-end/src/pages/Main/Library/WordSpellPreviewModal.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/utils/contentGames.ts`
- `front-end/src/constants/contentOptions.ts`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/wordSpellGame.ts`
- `mobile/src/features/games/utils/gameMetadata.ts`
- `mobile/src/features/games/components/WordSpellGameRenderer/*`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `tasks/slices/043-complete-a-palavra.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-433.md`

## Validacoes executadas

- `npx jest src/modules/contents/contents-catalog-bootstrap.service.spec.ts` — 8 passed (catálogo length 13; word-spell title/category/roundsPerRun/categories; duplicate filter length 1)

## Pendencias pos-task

- Parent deve adicionar assets em `jogo_complete_a_palavra/` (capas + `items/`) e rodar `node backend/scripts/upload-word-spell-assets.mjs`
- Validar prévia visual com print após upload das imagens

## Status final

done
