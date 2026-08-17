# Task 506 - Permitir responsável montar trilha mesmo com vínculo

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile
- contracts

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` (descrição de `canManage`)

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Dependencias

- Task 501, 505

## Objetivo

O responsável pode montar/editar/sugerir a trilha da criança; não fica restrito ao profissional.

## Criterios de aceite

- [x] Guardian dono da criança tem `canManage: true` (com ou sem vínculo ativo)
- [x] Testes backend atualizados
- [x] Copy mobile não implica “só profissional monta”

## Resultado da execucao

Removido bloqueio por link ativo; openapi/copy atualizados; chip de autoria via `professionalUserId`.

## Contexto utilizado

- trails.service, openapi, TrailTodayScreen, TrailLibraryPane

## Handoff

- `.agents/state/handoffs/TASK-506.md`

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

## Pendencias pos-task

- recarregar app / backend já em watch

## Status final

done
