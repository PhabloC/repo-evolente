# Task 628 - Corrigir Asaas checkout, revinculação pós-cancelamento e verifyPayment overdue

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

- `POST /subscriptions/verify-payment` (ou equivalente exposto)
- `GET /subscriptions/me`
- `POST /patients/link`
- webhooks/checkout Asaas

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 — Gateway Asaas e ciclo de assinatura (`tasks/slices/039-gateway-asaas-assinatura.md`)
- Slice 054 — Cancelamento em cascata (`tasks/slices/054-cancelamento-conta-responsavel-acesso-profissional.md`)

## Objetivo

Corrigir três bugs de backend identificados em code review:

1. **Asaas:** pagamento histórico com mesmo `externalReference` (`userId:audience`) ativa checkout novo sem pagamento atual.
2. **Patients:** após cancelamento e renovação da assinatura, `linkByCode` devolve vínculo `CANCELED` sem fluxo de revinculação.
3. **Subscriptions:** `verifyPayment` retorna `accessGranted: true` para `OVERDUE` vencido há >3 dias sem aplicar `enforceOverdueSuspensionForUser`.

## Comportamento esperado

- Inspeção remota só confirma pagamento quando `checkoutSession` ou `subscription` corresponder ao checkout atual (não basta `externalReference` genérico).
- Profissional que revincula por código com assinatura do responsável restabelecida recebe vínculo `PENDING` (não permanece `CANCELED`).
- `verifyPayment` aplica suspensão por atraso, recarrega assinatura e deriva `accessGranted` do estado atualizado.

## Contexto mínimo

- esta task, slices 039/054
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`

## Contexto sob demanda

- testes em `subscriptions.service.spec.ts` e `patients.service.spec.ts`

## Orçamento de contexto

- baixo/médio — três pontos localizados em serviços existentes.

## Critérios de aceite

- [x] Pagamento antigo com mesmo `externalReference` não libera checkout novo.
- [x] `linkByCode` converte vínculo `CANCELED` existente para `PENDING` quando assinatura ativa.
- [x] `verifyPayment` chama `enforceOverdueSuspensionForUser` e retorna acesso coerente.
- [x] Testes focados passam.

## Resultado da execucao

- Removida correspondência só por `externalReference` em `inspectRemotePayment`.
- `linkByCode` reabre vínculo cancelado como `PENDING` com guard de assinatura do responsável.
- `verifyPayment` alinhado a `getStatus`/`assertAccessGranted` para suspensão por atraso.

## Validacoes executadas

- `npx jest` — 51 testes nos 3 arquivos de spec — ok

## Status final

done
