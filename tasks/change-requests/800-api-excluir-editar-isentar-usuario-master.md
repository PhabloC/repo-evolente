# Task 800 - API para excluir, editar perfil e isentar usuário

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

- `contracts/openapi.yaml#/paths/~1users~1{userId}`
- `contracts/openapi.yaml#/components/schemas/User`
- `contracts/openapi.yaml#/components/schemas/UpdateUserRequest`

## Modo de execucao

single-stack

## Slice vertical

- Slice 072 — `tasks/slices/072-gestao-operacional-usuarios-master.md`

## Objetivo

Expor no contrato e no backend exclusão de usuário, atualização administrativa (incluindo papel) e isenção de mensalidade para profissional ou responsável.

## Dependências

- Slice 009 — done
- Task 610 — done

## Contexto mínimo

- esta task
- `tasks/slices/072-gestao-operacional-usuarios-master.md`
- `contracts/openapi.yaml` paths `/users/{userId}` e schema `User`
- `backend/src/modules/users/`
- `backend/src/modules/subscriptions/subscriptions.service.ts` (`getStatus`, `assertAccessGranted`, `resolveAccessGranted`)

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| FKs de exclusão | `backend/src/database/migrations/1830000000000-AddReferentialForeignKeys.ts` | ordem de limpeza |
| Perfis de acesso | `backend/src/modules/{professionals,guardians}` | gravar `accessGranted` ao isentar |
| Testes | `backend/src/modules/users/users.service.spec.ts` | regressão de delete, papel e isenção |

## Orçamento de contexto

- médio
- estratégia: só paths de usuário/assinatura e FKs; sem mobile nem UI

## Critérios de aceite

- [x] `DELETE /users/{userId}` remove a conta (403 se for a própria ou o último master)
- [x] `PATCH /users/{userId}` documentado e aceita `role` e `feeExempt`
- [x] `User.feeExempt` entra no contrato e na persistência
- [x] Usuário profissional/responsável isento passa no gate de assinatura sem pagar
- [x] Master continua isento por papel e não usa `feeExempt`

## Fora de escopo

- UI web
- UI mobile

## Resultado da execucao

- Contrato documenta PATCH/DELETE em `/users/{userId}` e `feeExempt`
- Persistência ganhou `users.fee_exempt`
- Gate de assinatura libera profissional/responsável isento
- Exclusão limpa dependentes e bloqueia autoexclusão/último master

## Contexto utilizado

- Task 800, Slice 072, OpenAPI `/users/{userId}`, módulo users e subscriptions

## Handoff

- `.agents/state/handoffs/TASK-800.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/users/entities/user.entity.ts`
- `backend/src/modules/users/dto/update-user.dto.ts`
- `backend/src/modules/users/users.repository.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/modules/users/users.typeorm.repository.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.controller.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `backend/src/database/migrations/1950000000000-AddFeeExemptToUsers.ts`

## Validacoes executadas

- Jest `users.service.spec.ts`: 17 testes passando
- Migration `AddFeeExemptToUsers1950000000000` aplicada no banco local

## Pendencias pos-task

- Reiniciar o backend local após a migration

## Status final

done
