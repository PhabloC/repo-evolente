# Task 073 - Endurecer auth refresh e hidratacao web

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

- `contracts/openapi.yaml#/paths/auth`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Eliminar fragilidades da sessao autenticada ja identificadas em code review: consulta redundante no refresh, segredo de refresh inseguro por fallback e logout indevido ao hidratar sessoes antigas sem `refreshToken`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-054.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API auth | `contracts/openapi.yaml#/paths/auth` | validar impacto contratual do refresh | sim |
| Backend auth | `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/SECURITY.md` | corrigir fluxo de refresh e segredo dedicado | sim |
| Front-end auth | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `SECURITY.md` | ajustar hidratacao e compatibilidade com storage legado | sim |
| Implementacao atual | `backend/src/modules/auth/**`, `backend/src/config/app.config.ts`, `front-end/src/stores/authStore.ts` | aplicar correcoes no menor escopo | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a leitura ao fluxo de auth ja existente, sem abrir mobile nem requisitos amplos

## Criterios de conclusao

- [ ] `signIn` e `refresh` deixam de consultar o usuario mais vezes do que o necessario
- [ ] refresh de usuario ausente/inativo falha com `UnauthorizedException` consistente
- [ ] `REFRESH_TOKEN_SECRET` deixa de compartilhar fallback com `JWT_SECRET`
- [ ] hidratacao do store web preserva sessoes legadas sem `refreshToken` ate falha/renovacao real
- [ ] validacoes focadas de backend e front-end executadas

## Dependencias

- Task 054 - done

## Resultado da execucao

- o backend passou a reutilizar o usuario ja carregado no login e a carregar o usuario do refresh apenas uma vez, sem consulta redundante dentro de `buildAuthSession`
- o refresh agora converte usuario ausente para `UnauthorizedException` consistente e preserva a rejeicao de contas inativas
- o segredo de refresh deixou de herdar `JWT_SECRET` como fallback e usa default de desenvolvimento separado
- o store web passou a aceitar sessoes legadas sem `refreshToken`, mantendo a sessao ate expirar ou falhar uma renovacao real

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-054.md`

### Sob demanda

- `contracts/openapi.yaml#/paths/auth`
- `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/SECURITY.md`
- `front-end/docs/ai/ARCHITECTURE.md`, `front-end/docs/ai/CODE_STYLE.md`, `front-end/docs/ai/SECURITY.md`
- `backend/src/config/app.config.ts`
- `backend/src/modules/auth/auth.service.ts`
- `backend/src/modules/auth/auth.service.spec.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/stores/authStore.test.ts`
- `front-end/src/services/http/apiClient.ts`

## Handoff

- `.agents/state/handoffs/TASK-073.md`

## Arquivos alterados

- `backend/src/config/app.config.ts`
- `backend/src/modules/auth/auth.service.ts`
- `backend/src/modules/auth/auth.service.spec.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/stores/authStore.test.ts`
- `tasks/change-requests/073-endurecer-auth-refresh-e-hidratacao-web.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-073.md`

## Validacoes executadas

- `cd backend && npm run build` - ok
- `cd backend && npm run test -- src/modules/auth/auth.service.spec.ts` - ok
- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- src/stores/authStore.test.ts` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
