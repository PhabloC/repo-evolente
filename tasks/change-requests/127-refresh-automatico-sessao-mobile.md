# Task 127 - Refresh automatico da sessao no mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1auth~1refresh`
- `contracts/openapi.yaml#/paths/~1auth~1login`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Eliminar falhas `401` nas telas autenticadas do mobile quando o `accessToken` expira, renovando a sessao automaticamente com `refreshToken` antes de exigir novo login.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/127-refresh-automatico-sessao-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `contracts/openapi.yaml`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-120.md`
- `.agents/state/handoffs/TASK-126.md`
- `front-end/src/services/http/apiClient.ts`
- `mobile/src/shared/network/apiClient.ts`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/store/useSessionStore.ts`
- `mobile/src/shared/storage/secureStorage.ts`

## Orcamento de contexto

- 11 fontes
- estrategia de reducao: restringir a auth/session/network do mobile e reutilizar o padrao ja consolidado no web

## Criterios de aceite

- Requests autenticadas do mobile renovam a sessao ao receber `401` elegivel
- Novo `accessToken`/`refreshToken` fica persistido no `SecureStore`
- Falha de refresh limpa a sessao local e evita loop infinito
- Cobertura de regressao adicionada para o fluxo de refresh do mobile

## Fora de escopo

- Alteracoes de contrato
- Mudancas visuais
- Sincronizacao offline

## Dependencias

- Task 120
- Task 126

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Mobile ganhou renovacao automatica de sessao via `/auth/refresh` no cliente HTTP compartilhado
- Sessao renovada passa a atualizar store e `SecureStore` sem exigir novo login
- Requests de auth sensiveis ficam fora do retry e o refresh falho limpa a sessao local
- Cobertura de regressao adicionada para a renovacao explicita da sessao

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: contrato auth, docs mobile `ARCHITECTURE.md`/`CODE_STYLE.md`/`QA.md`, handoffs `TASK-120` e `TASK-126`, padrao web de refresh, `apiClient`, `authService`, `useSessionStore` e `secureStorage`
- Fontes evitadas: UI mobile, backend nao-auth e design system

## Handoff

- `.agents/state/handoffs/TASK-127.md`

## Arquivos alterados

- `mobile/src/shared/network/apiClient.ts`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `tasks/change-requests/127-refresh-automatico-sessao-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-127.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- Validar em dispositivo fisico o fluxo de expiracao real do token

## Status final

done
