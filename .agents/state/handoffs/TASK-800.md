# TASK-800

- Título: API para excluir, editar perfil e isentar usuário
- Slice: 072
- Status final: done

## Decisões

- `feeExempt` no usuário libera o gate de assinatura sem pagar
- `DELETE /users/{userId}` remove a conta e dependentes; 403 para si mesmo ou último master
- `PATCH /users/{userId}` já existia no backend e foi documentado com `role` e `feeExempt`
- Master continua isento por papel; `feeExempt` é forçado para false nesse caso

## Contexto usado

- `contracts/openapi.yaml` `/users/{userId}`
- `backend/src/modules/users/`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- FKs em `1830000000000-AddReferentialForeignKeys.ts`

## Arquivos

- `contracts/openapi.yaml`
- `backend/src/modules/users/**`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `backend/src/database/migrations/1950000000000-AddFeeExemptToUsers.ts`

## Validações

- `users.service.spec.ts`: 17 testes passando (update, isenção, delete, último master)

## Pendências

- Rodar `npm run migration:run` no backend se a coluna `fee_exempt` ainda não existir
- Reiniciar `npm run start:dev` depois da migration

## Próximo contexto

- Task 801 e `front-end/src/pages/Main/AdminUsers/`
