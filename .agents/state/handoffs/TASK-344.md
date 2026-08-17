# Handoff - Task 344

## Task

- identificador: 344
- título: Capa e verso dedicados no jogo da memória
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 032
- objetivo de negócio: consolidar o jogo da memória com capa própria do jogo e verso próprio das cartas

## Decisões preservadas

- `gameConfig.coverUrl` do `memory` agora aponta para `games/memoria/capa_jogo_memoria.webp`
- `gameConfig.cardBackUrl` expõe `games/memoria/capinha_jogo.webp`
- o script de upload do jogo da memória sobe arquivos raiz e cartas por categoria
- web e mobile usam `cardBackUrl` nas cartas escondidas quando ele existir

## Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/344-capa-e-verso-dedicados-jogo-memoria.md`
- `tasks/slices/032-jogo-memoria.md`
- `.agents/state/handoffs/TASK-343.md`

## Contexto sob demanda carregado

- `jogo_memoria/`
- `contracts/openapi.yaml`
- `STORAGE_BUCKET_MAP.md`
- `backend/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `backend/src/modules/contents/`
- `backend/scripts/upload-memory-game-assets.mjs`
- `front-end/src/pages/Main/Library/`
- `mobile/src/features/games/`

## Arquivos alterados

- backend de `contents` + script `upload-memory-game-assets`
- contrato OpenAPI e `STORAGE_BUCKET_MAP.md`
- prévia web da biblioteca e tipos compartilhados do front
- renderer mobile e utilitários do jogo da memória
- task, slice, índice e este handoff

## Validacoes executadas

- backend tests focados de `contents`
- `node --check` do script de upload
- `vitest` da biblioteca web
- `jest` focado do mobile (`memoryGame` + `MemoryGameRenderer`)
- upload real para o bucket

## Pendências

- reiniciar o backend da instância que ainda não reprocessou o bootstrap do catálogo após a Task 344

## Próxima ação sugerida

- validar no ambiente em execução se a capa do card do jogo e o verso das cartas já refletem os assets dedicados após restart do backend

## Próximo contexto recomendado

- `backend/src/modules/contents/memory-game-assets.ts`
- `backend/scripts/upload-memory-game-assets.mjs`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`
