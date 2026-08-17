# Task 436 - Fluência em Ação: catálogo, prévia e runtime

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

- `contracts/openapi.yaml` — `ContentGameType`, `FluencyGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/045-fluencia-em-acao.md`

## Referencia visual

- print: `design-system/front/prints/fluencia-em-acao.png`
- governa: passagem (texto + destaques + ilustração + ouvir/avançar) e ritmo (chips + ilustração + ouvir)
- lacunas do print (não implementadas): menu, níveis, conquistas, microfone, dicas
- decisão: 10 etapas sorteadas; só TTS; categoria `fala`

## Objetivo

Criar `gameType: fluency` com pool de 10 stages (`passage` | `rhythm`), bootstrap em `fala`, prévia web e renderer mobile.

## Criterios de aceite

- [x] `fluency` no contrato e enums (backend, front, mobile)
- [x] bootstrap em `fala` com 10 stages e `roundsPerRun: 10`
- [x] prévia web jogável com ouvir (TTS) e avançar
- [x] runtime mobile equivalente
- [x] testes bootstrap atualizados
- [x] sem menu / níveis / conquistas / microfone

## Resultado da execucao

Fluência em Ação end-to-end: 10 stages (passagem + ritmo), categoria Fluência (`fala`), prévia web e renderer mobile com Ouvir (TTS) e Próximo.

## Contexto utilizado

- Slice 045, print fluencia-em-acao, padrões emotions/word-spell, openapi

## Handoff

- `.agents/state/handoffs/TASK-436.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/contents/fluency-game-assets.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/fluencyGame.ts`
- `front-end/src/pages/Main/Library/FluencyPreviewModal.tsx`
- `front-end/src/pages/Main/Library/GamePreviewModal.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/utils/contentGames.ts`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/utils/fluencyGame.ts`
- `mobile/src/features/games/components/FluencyGameRenderer/`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- `mobile/src/features/games/utils/gameMetadata.ts`
- `mobile/src/features/admin/contents/adapters/adaptContent.ts`
- `mobile/src/features/admin/contents/utils/labels.ts`
- `design-system/front/prints/fluencia-em-acao.png`
- `STORAGE_BUCKET_MAP.md`
- `tasks/slices/045-fluencia-em-acao.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx jest contents-catalog-bootstrap.service.spec.ts` — PASS
- backend watch: Nest application successfully started

## Pendencias pos-task

- Capas/ilustrações no S3 (`fluencia_em_acao/`) quando houver arte

## Status final

done
