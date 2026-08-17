# Task 434 - Jogo das Emoções: catálogo, prévia e runtime

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

- `contracts/openapi.yaml` — `ContentGameType`, `EmotionsGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/044-jogo-das-emocoes.md`

## Referencia visual

- print: `design-system/front/prints/jogo-das-emocoes-socioemocionais.png`
- governa: etapas Identificar / Situação / Estratégia, tela Parabéns
- lacunas do print (não implementadas): mapa de fases, conquistas, medalhas, coração
- decisão: etapas lineares + conteúdo aleatório a cada entrada

## Objetivo

Criar `gameType: emotions` com pool de stages, bootstrap em `emocoes`, prévia web e renderer mobile.

## Criterios de aceite

- [x] `emotions` no contrato e enums (backend, front, mobile)
- [x] bootstrap em `emocoes` com pool de stages e `roundsPerRun`
- [x] prévia web jogável
- [x] runtime mobile
- [x] testes bootstrap atualizados
- [x] sem mapa / sem conquistas

## Resultado da execucao

Jogo das Emoções end-to-end: 12 stages no pool, 8 por partida aleatórias, categoria Socioemocionais (`emocoes`), prévia web e renderer mobile com feedback e “Jogar de novo”.

## Contexto utilizado

- Slice 044, print socioemocionais, padrões sentence-fill/word-spell, openapi

## Handoff

- `.agents/state/handoffs/TASK-434.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/contents/emotions-game-assets.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/emotionsGame.ts`
- `front-end/src/pages/Main/Library/EmotionsPreviewModal.tsx`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/utils/contentGames.ts`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/emotionsGame.ts`
- `mobile/src/features/games/components/EmotionsGameRenderer/`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `mobile/src/features/games/utils/gameMetadata.ts`
- `mobile/src/features/admin/contents/adapters/adaptContent.ts`
- `mobile/src/features/admin/contents/utils/labels.ts`
- `design-system/front/prints/jogo-das-emocoes-socioemocionais.png`
- `STORAGE_BUCKET_MAP.md`
- `tasks/slices/044-jogo-das-emocoes.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx jest contents-catalog-bootstrap.service.spec.ts` — PASS
- typecheck front: erros pré-existentes; sem erros novos em `emotions*`

## Pendencias pos-task

- Capas ilustradas no S3 quando houver arte
- Ilustrações no lugar de emoji (opcional)

## Status final

done
