# Handoff - Task 343

## Task

- identificador: 343
- título: Jogo da memória educativo com assets no bucket
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 032
- objetivo de negócio: incluir um jogo da memória infantil educativo no catálogo, com assets reais no bucket, prévia web e execução mobile

## Decisões preservadas

- o novo `gameType` é `memory`
- o jogo é individual, sem ranking e sem multiplayer
- as imagens sobem para `dev/games/memoria/{categoria}/{arquivo}.webp`
- o `gameConfig` usa `pairsPerRound`, `coverUrl` e `categories[].cards[]`
- a capa do card reutiliza a primeira imagem disponível das categorias publicadas

## Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/343-jogo-memoria-educativo-com-assets-no-bucket.md`
- `tasks/slices/032-jogo-memoria.md`

## Contexto sob demanda carregado

- `STORAGE_BUCKET_MAP.md`
- `contracts/openapi.yaml`
- `jogo_memoria/`
- `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ARCHITECTURE.md`, `front-end/docs/ai/ACCESSIBILITY.md`
- `mobile/docs/ai/ARCHITECTURE.md`, `mobile/docs/ai/CODE_STYLE.md`
- `backend/src/modules/contents/`
- `front-end/src/pages/Main/Library/`
- `mobile/src/features/games/`

## Arquivos alterados

- backend de `contents` + script `upload-memory-game-assets`
- contrato OpenAPI e `STORAGE_BUCKET_MAP.md`
- biblioteca web (`Main/Library`) e tipos compartilhados do front
- runtime mobile (`trail/types`, `gameMetadata`, `MemoryGameRenderer`, `memoryGame`)
- task, slice, índice e este handoff

## Validacoes executadas

- backend tests focados de `contents` — ok
- backend eslint focado dos arquivos alterados — ok
- `node --check` do script de upload — ok
- `vitest` da biblioteca web — ok
- `jest` focado do mobile (`memoryGame` + `MemoryGameRenderer`) — ok
- upload real para o bucket — ok, 66 arquivos publicados em **quarta-feira, 29 de julho de 2026**

## Pendências

- reiniciar o backend da instância que usa o banco atual para o bootstrap criar/atualizar o conteúdo `memory` em runtime, se ainda não houve restart após esta task

## Próxima ação sugerida

- validar no ambiente em execução se o item `Jogo da memória` já aparece na biblioteca/trilha após restart do backend

## Próximo contexto recomendado

- `backend/src/modules/contents/memory-game-assets.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`

## Contexto que não deve ser carregado

- slices e docs de auth, relatórios, pacientes e módulos não relacionados ao runtime de jogos
