# Task 766 - Cancelamento mantém acesso até o fim do ciclo pago

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `POST /subscriptions/cancel`, schema `Subscription` (novo campo `accessEndsAt`), `SubscriptionStatusResponse.accessGranted`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 039 — `tasks/slices/039-gateway-asaas-assinatura.md`

## Origem

Bug reportado: conta responsável pagou PIX mensal (confirmado em 2026-10-02), cancelou a assinatura em 2026-10-05 e perdeu o acesso imediatamente, apesar do mês já pago. Investigação: `admin_audit_logs` registra `source=user_cancel`; o pagamento e a liberação funcionaram. A regra "cancelamento bloqueia na hora" era decisão do slice 039.

## Decisão humana (2026-10-05)

- Cancelamento pelo usuário de assinatura `active` mantém o acesso até o fim do ciclo mensal já pago e apenas interrompe a renovação.
- Reembolso continua bloqueando na hora.
- Cancelamento de assinatura `overdue` continua bloqueando na hora (ciclo não pago).
- Cancelamento pelo master (admin) continua imediato.

## Escopo

- Backend: coluna `subscriptions.access_ends_at`; `cancelSubscription` calcula o fim do ciclo (aniversário mensal de `firstPaidAt`/`confirmedAt`), cancela a renovação no Asaas, mantém `accessGranted` até `accessEndsAt`; expiração revoga acesso e cancela vínculos do responsável (lazy em `/me`, gate e verify + cron horário); webhooks `PAYMENT_DELETED`/`CHECKOUT_*` não revogam assinatura já cancelada.
- Contrato: documentar `accessEndsAt` e a nova regra de cancelamento.
- Web: card de assinatura não redireciona quando o acesso continua, mostra "acesso até dd/mm/aaaa" e textos de confirmação atualizados.
- Mobile: card de assinatura só encerra sessão quando `accessGranted=false`; textos atualizados.

## Fora de escopo

- Reativar a mesma assinatura cancelada (novo checkout continua sendo o caminho).
- Investigar entrega de webhooks Asaas (tabela `subscription_webhook_events` vazia) — tratar em task própria.
- Reativação manual da conta afetada.

## Criterios de aceite

- [x] Cancelar assinatura `active` paga retorna `accessGranted=true` e `subscription.accessEndsAt` no fim do ciclo.
- [x] Após `accessEndsAt`, `/subscriptions/me` e o gate retornam sem acesso e vínculos do responsável são cancelados.
- [x] Cancelar `overdue` e reembolsar continuam bloqueando na hora.
- [x] `PAYMENT_DELETED` após cancelamento não revoga o acesso do período pago.
- [x] Web e mobile informam até quando o acesso continua e não deslogam/redirecionam.
- [x] Testes do service atualizados e passando.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- esta task

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Regra de cancelamento | `backend/src/modules/subscriptions/` | alterar service/entity/repository | sim |
| Contrato | `contracts/openapi.yaml` paths `/subscriptions/cancel` e schema `Subscription` | documentar campo | sim |
| UI web | `front-end/src/pages/Main/Settings/SubscriptionManagementCard.tsx`, `front-end/src/types/subscription.ts` | textos e fluxo pós-cancelamento | sim |
| UI mobile | `mobile/src/features/shell/components/SubscriptionManagementCard/`, `mobile/src/features/profile/` | textos e fluxo pós-cancelamento | sim |

## Orçamento de contexto

- médio; carregar somente módulo de assinaturas, os dois cards e tipos; não carregar gates nem admin.

## Resultado da execucao

- Backend: `cancelSubscription` calcula `accessEndsAt` como o próximo aniversário mensal de `firstPaidAt` (fallback `confirmedAt`) e só revoga na hora quando não há ciclo pago (overdue/sem pagamento). Expiração aplicada em `getStatus`, `assertAccessGranted`, `verifyPayment` e por cron horário (`SubscriptionAccessExpiryService`), considerando todas as assinaturas do usuário (um checkout pendente posterior não impede a expiração). Webhooks `PAYMENT_DELETED`/`CHECKOUT_*` ignorados para assinatura já cancelada; `PAYMENT_REFUNDED` zera `accessEndsAt` e revoga.
- Migração `1930000000000-AddAccessEndsAtToSubscriptions` aplicada no banco configurado (`82.112.244.57/evolente`) com autorização do usuário.
- Contrato: `Subscription.accessEndsAt`, descrição de `/subscriptions/cancel` e `accessGranted`.
- Web: card mostra "Acesso até", mensagem pós-cancelamento sem redirecionar quando o acesso continua, textos do modal/hint atualizados.
- Mobile: card só chama `onAccessBlocked` quando `accessGranted=false`; descrição e modal atualizados.

## Contexto utilizado

- Slice 039, módulo `backend/src/modules/subscriptions/`, paths de assinatura do `openapi.yaml`, cards de assinatura web/mobile e tipos.

## Arquivos alterados

- `backend/src/database/migrations/1930000000000-AddAccessEndsAtToSubscriptions.ts`
- `backend/src/modules/subscriptions/entities/subscription.entity.ts`
- `backend/src/modules/subscriptions/subscriptions.repository.ts`
- `backend/src/modules/subscriptions/subscriptions.in-memory.repository.ts`
- `backend/src/modules/subscriptions/subscriptions.typeorm.repository.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `backend/src/modules/subscriptions/subscriptions.service.spec.ts`
- `backend/src/modules/subscriptions/subscriptions.module.ts`
- `backend/src/modules/subscriptions/subscription-access-expiry.service.ts`
- `backend/src/modules/subscriptions/utils/billing-cycle.util.ts` (+ spec)
- `contracts/openapi.yaml`
- `front-end/src/types/subscription.ts`
- `front-end/src/utils/resolveScheduledAccessEnd.ts` (+ test)
- `front-end/src/pages/Main/Settings/SubscriptionManagementCard.tsx`
- `mobile/src/features/profile/types/subscription.ts` (+ test)
- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`

## Validacoes executadas

- `backend`: `npx jest src/modules/subscriptions --runInBand` — 42 testes passaram; `npx eslint src/modules/subscriptions` — ok; `tsc --noEmit` sem erros novos (erros pré-existentes em specs de admin/contents e em testes de `verifyPayment`).
- `front-end`: `npx vitest run src/utils/resolveScheduledAccessEnd.test.ts` — 2 testes; eslint ok; `tsc -b` sem erros nos arquivos alterados (erros pré-existentes em testes de pacientes/planos).
- `mobile`: `npx jest src/features/profile/types/subscription.test.ts` — 5 testes; eslint ok; `tsc` sem erros nos arquivos alterados (erros pré-existentes em jogos/admin/login).

## Pendencias pos-task

- Conta `phablo2@teste.com.br` cancelada antes desta mudança continua sem acesso (fora de escopo; assinatura remota já apagada no Asaas).
- `subscription_webhook_events` vazia: webhooks Asaas não chegam a este ambiente — criar task própria.
- Validação visual dos cards web/mobile no estado "cancelada com acesso até".

## Handoff

- `.agents/state/handoffs/TASK-766.md`

## Status final

done
