# Handoff - Task 127

## Identificador

- Task 127 - Refresh automatico da sessao no mobile
- `tasks/change-requests/127-refresh-automatico-sessao-mobile.md`

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Status final

done

## Decisoes preservadas

- O mobile agora tenta renovar a sessao via `/auth/refresh` quando uma request autenticada recebe `401` elegivel
- Requests de auth sensiveis (`/auth/login`, `/auth/logout`, `/auth/refresh`, recovery e reset) ficam fora do retry
- Falha de refresh limpa `SecureStore` e estado local para evitar loop infinito com token expirado

## Contexto efetivamente usado

- Task 127, Slice 002, handoffs `TASK-120` e `TASK-126`, contrato auth, `front-end/src/services/http/apiClient.ts`, `mobile/src/shared/network/apiClient.ts`, `mobile/src/features/auth/services/authService.ts`, `mobile/src/shared/storage/secureStorage.ts`

## Arquivos alterados

- `mobile/src/shared/network/apiClient.ts`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `tasks/change-requests/127-refresh-automatico-sessao-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok (11 suites, 22 testes)

## Pendencias

- Validar em dispositivo fisico o fluxo real apos expiracao de token

## Proximo contexto recomendado

- `mobile/src/shared/network/apiClient.ts` e `mobile/src/features/auth/services/authService.ts` para qualquer ajuste futuro de sessao no mobile
