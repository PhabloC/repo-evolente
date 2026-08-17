# Handoff - Task 054

## Task

- identificador: 054
- título: Renovacao automatica da sessao web
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 002 - Autenticacao
- objetivo de negócio: manter a sessao web utilizavel mesmo apos o access token expirar por ociosidade
- entrega verificável: refresh token no backend + renovacao transparente no front-end

## Decisões preservadas

- decisão: tratar a correção como continuação do Slice 002 em vez de abrir novo slice
- motivo: a falha está no fluxo central de autenticação e sessão
- impacto: a governança e a rastreabilidade ficam alinhadas ao auth já existente

- decisão: usar refresh token stateless com retry transparente no interceptor HTTP do front-end
- motivo: evita logout por ociosidade sem introduzir dependência de polling ou cron no cliente
- impacto: a sessão só cai quando o refresh realmente expira ou se torna inválido

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/054-renovacao-automatica-sessao-web.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-005.md`
- `.agents/state/handoffs/TASK-006.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | API auth | verificar refresh token e endpoint |
| `backend/src/modules/auth/**` | backend auth | checar implementação atual |
| `front-end/src/stores/authStore.ts` | sessão web | checar persistência e queda de token |
| `front-end/src/services/http/apiClient.ts` | cliente HTTP | checar interceptors e tratamento de 401 |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `mobile/` | o pedido é sobre o site |
| `design-system/` | correção de sessão sem impacto visual |

## Resultado por stack

- backend: login passou a emitir `refreshToken` obrigatório e a API expõe `POST /auth/refresh`
- front-end: store persiste `refreshToken`, interceptor renova a sessão ao receber `401` elegível e repete a chamada original

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
- `tasks/change-requests/054-renovacao-automatica-sessao-web.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`

## Validações executadas

- `cd backend && npm run build`
- `cd backend && npm run test -- src/modules/auth/auth.service.spec.ts`
- `cd front-end && npm run lint`
- `cd front-end && npm run build`
- `cd front-end && npm run test -- --run`

## Pendências ou bloqueios

- sem pendência funcional desta task
- `cd backend && npm run lint` segue falhando por line endings preexistentes em `src/modules/guardians/guardians.service.ts`, `src/modules/patients/patients.service.ts` e `src/modules/patients/patients.service.spec.ts`

## Próxima ação sugerida

- se quiser endurecer segurança depois, adicionar rotação e revogação explícita de refresh token no backend

## Próximo contexto recomendado

- `backend/src/modules/auth/**`
- `front-end/src/services/http/apiClient.ts`
- `front-end/src/stores/authStore.ts`

## Contexto que não deve ser carregado na próxima etapa

- `design-system/front/`
- motivo: sem necessidade para correção de sessão
