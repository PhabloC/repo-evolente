# Task 603 - Validar assinatura antes de autenticar no mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /subscriptions/me`

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Impedir que responsável sem acesso por assinatura entre no estado autenticado do app mobile após o login.

## Contexto mínimo

- esta task
- Slice 039
- handoff TASK-599
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/hooks/useSignInForm.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Verificação de acesso | `contracts/openapi.yaml#/paths/~1subscriptions~1me` | resposta `accessGranted` |
| Cabeçalho autenticado antes da store | `mobile/src/shared/network/apiClient.ts` | enviar token recém obtido |

## Orçamento de contexto

- baixo
- estratégia: somente login de responsável; sem alterar backend, checkout ou telas autenticadas.

## Critérios de aceite

- [x] Responsável sem assinatura ativa permanece no login com mensagem clara.
- [x] Sessão sem acesso não é persistida nem marcada como autenticada.
- [x] Master e responsável com acesso seguem o fluxo existente.

## Resultado da execucao

- Após credenciais válidas, o login de responsável consulta `/subscriptions/me` usando o token recém emitido, antes de persistir a sessão.
- Sem `accessGranted`, apresenta a orientação para regularizar no site e mantém o app no login.

## Contexto utilizado

- Task 603, Slice 039, handoff TASK-599, serviço de autenticação, contrato de assinatura e cliente HTTP mobile.

## Handoff

- `.agents/state/handoffs/TASK-603.md`

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `tasks/change-requests/603-gate-assinatura-antes-login-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `.agents/state/handoffs/TASK-603.md`

## Validacoes executadas

- `npx eslint src/features/auth/services/authService.ts` — passou.

## Pendencias pos-task

- Nenhuma.

## Status final

done
