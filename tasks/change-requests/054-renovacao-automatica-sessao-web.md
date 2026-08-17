# Task 054 - Renovacao automatica da sessao web

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` auth

## Modo de execucao

cross-stack

## Objetivo

Evitar que a sessao web caia quando o usuario fica um tempo sem interagir, renovando a autenticacao de forma transparente enquanto a sessao ainda for valida.

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-005.md`
- `.agents/state/handoffs/TASK-006.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API auth | `contracts/openapi.yaml` | definir endpoint e payload de refresh | sim |
| Backend auth | `backend/docs/ai/ARCHITECTURE.md`, `SECURITY.md` | implementar renovacao segura da sessao | sim |
| Front-end auth | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `SECURITY.md` | integrar refresh transparente no cliente web | sim |
| Implementacao atual | `backend/src/modules/auth/**`, `front-end/src/{stores/services/pages}/**` relacionados a auth | alterar apenas auth e sessao web | sim |

## Orçamento de contexto

- medio
- estrategia: restringir a auth backend, contrato auth e sessao web; sem tocar mobile

## Criterios de conclusao

- [x] login passa a retornar refresh token utilizavel
- [x] backend expõe renovacao de sessao compatível com o contrato
- [x] front-end renova token automaticamente em expiracao de access token sem derrubar a sessao
- [x] falha real de refresh limpa sessao local de forma consistente
- [x] validacoes focadas de backend e front aprovadas

## Dependencias

- Task 005 - done
- Task 006 - done

## Resultado da execucao

- backend passou a emitir `refreshToken` obrigatório junto do login e expôs `POST /auth/refresh` com validação dedicada.
- front-end passou a persistir `accessToken` + `refreshToken`, renovar sessão ao receber `401` elegível e repetir a requisição original uma única vez.
- falhas reais de refresh agora limpam a sessão local de forma centralizada, evitando estado autenticado inconsistente.

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-005.md`, `.agents/state/handoffs/TASK-006.md`

### Sob demanda

- `contracts/openapi.yaml`
- `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/SECURITY.md`
- `front-end/docs/ai/ARCHITECTURE.md`, `front-end/docs/ai/CODE_STYLE.md`, `front-end/docs/ai/SECURITY.md`
- `backend/src/modules/auth/**`
- `front-end/src/services/http/apiClient.ts`
- `front-end/src/services/auth/authService.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/types/auth.ts`

## Handoff

- `.agents/state/handoffs/TASK-054.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/.env.example`
- `backend/src/config/app.config.ts`
- `backend/src/modules/auth/auth.controller.ts`
- `backend/src/modules/auth/auth.service.ts`
- `backend/src/modules/auth/auth.service.spec.ts`
- `backend/src/modules/auth/dto/refresh-token.dto.ts`
- `front-end/src/pages/Auth/Login/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx`
- `front-end/src/pages/Main/Admin/index.test.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/services/adapters/adaptAuthResponse.test.ts`
- `front-end/src/services/auth/authService.ts`
- `front-end/src/services/http/apiClient.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/types/auth.ts`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-054.md`

## Validacoes executadas

- `cd backend && npm run build`
- `cd backend && npm run test -- src/modules/auth/auth.service.spec.ts`
- `cd backend && npm run lint` com falha preexistente em `src/modules/guardians/guardians.service.ts`, `src/modules/patients/patients.service.ts` e `src/modules/patients/patients.service.spec.ts` por `prettier/prettier` de line ending
- `cd front-end && npm run lint`
- `cd front-end && npm run build`
- `cd front-end && npm run test -- --run`

## Pendencias pos-task

- nenhuma funcional para o refresh web
- permanece dívida técnica preexistente de lint no backend fora do escopo desta task

## Status final

done
