# Task 489 - Hardening do PATCH do perfil próprio no backend

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem mudança de contrato; validação mais estrita no DTO existente

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Objetivo

Fazer `PATCH /users/me` rejeitar `name: null` como payload inválido em vez de deixar o erro estourar na persistência.

## Criterios de aceite

- [x] ausência continua opcional para `name`
- [x] `null` em `name` falha na validação do DTO
- [x] teste de regressão cobre o cenário
- [x] handoff gerado

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/change-requests/489-hardening-patch-perfil-proprio-backend.md`
- `.agents/state/handoffs/TASK-256.md`

## Contexto sob demanda

- `backend/AGENTS.md` e `backend/docs/ai/AGENTS.md`
- `backend/docs/ai/SECURITY.md` e `backend/docs/ai/QA.md`
- `backend/src/modules/users/dto/`

## Orçamento de contexto

- 7 fontes
- estratégia: limitar ao DTO e a uma spec unitária de validação

## Resultado da execucao

O DTO de perfil próprio agora diferencia corretamente campo ausente de `null`, eliminando o caminho que terminava em erro 500 na coluna `users.name`.

## Contexto utilizado

- slice 027
- handoff 256
- DTO `update-own-profile`

## Handoff

- `.agents/state/handoffs/TASK-489.md`

## Arquivos alterados

- `backend/src/modules/users/dto/update-own-profile.dto.ts`
- `backend/src/modules/users/dto/update-own-profile.dto.spec.ts`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- --runInBand src/modules/subscriptions/subscriptions.service.spec.ts src/modules/admin/admin.service.spec.ts src/modules/contents/catalog-config-merge.spec.ts src/modules/users/dto/update-own-profile.dto.spec.ts` — PASS
- `npx eslint src/modules/subscriptions/subscriptions.service.ts src/modules/subscriptions/subscriptions.service.spec.ts src/modules/users/dto/update-own-profile.dto.ts src/modules/users/dto/update-own-profile.dto.spec.ts src/modules/admin/admin.service.ts src/modules/admin/admin.service.spec.ts src/modules/contents/fluency-game-assets.ts src/modules/contents/dialogue-game-assets.ts src/modules/contents/emotions-game-assets.ts src/modules/contents/jigsaw-game-assets.ts src/modules/contents/catalog-config-merge.spec.ts` — PASS

## Pendencias pos-task

- nenhuma

## Status final

done
