# Task 508 - Aviso ao criar trilha própria com vínculo e trilha existentes

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `TrailListResponse.hasActiveProfessionalLink`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Dependencias

- Task 506

## Objetivo

Exibir confirmação/aviso quando o responsável for criar/alterar a própria trilha e a criança já tiver vínculo profissional ativo **e** trilha montada. Sem vínculo, não exibir aviso.

## Criterios de aceite

- [x] API expõe `hasActiveProfessionalLink` na listagem de trilhas
- [x] Mobile avisa antes de gerar/alterar se vínculo ativo + trilha existente
- [x] Sem vínculo: fluxo sem aviso

## Resultado da execucao

Campo `hasActiveProfessionalLink` no list; modal de aviso em suggest e add na biblioteca quando há vínculo + trailId.

## Contexto utilizado

- trails.service, openapi, TrailTodayScreen, TrailLibraryPane

## Handoff

- `.agents/state/handoffs/TASK-508.md`

## Arquivos alterados

- `backend/src/modules/trails/trails.service.ts`
- `backend/src/modules/trails/trails.service.spec.ts`
- `contracts/openapi.yaml`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/trail/adapters/adaptDayTrail.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailLibraryPane.tsx`

## Validacoes executadas

- trails.service.spec: 8 passed
- lints ok

## Pendencias pos-task

- nenhuma

## Status final

done
