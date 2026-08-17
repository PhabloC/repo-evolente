# Task 420 - Provider Asaas e checkout mensal

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

- `contracts/openapi.yaml#/paths` subscription (após Task 419)

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Implementar `AsaasPaymentProvider` atrás da interface existente, com valores mensais e criação de cobrança/assinatura para profissional e responsável.

## Dependencias

- Task 419

## Criterios de aceite

- [x] `PAYMENT_PROVIDER=asaas` seleciona o provider real; `fake` permanece para dev/testes
- [x] Env: API key, webhook secret, valores `7900` / `4900`, moeda BRL
- [x] Checkout cria cobrança/assinatura mensal no Asaas (sandbox) em status `pending`
- [x] Meios: cartão, PIX, boleto expostos conforme contrato
- [x] Persistência alinhada ao enum OpenAPI (`pending|active|overdue|suspended|canceled|refused`)
- [x] Master nunca inicia checkout (já isento)
- [x] Testes unitários do provider com HTTP mockado
- [x] Sem secrets commitados

## Fora de escopo

- Webhook e job de atraso (Task 421)
- UI (Task 422)

## Resultado da execucao

- `AsaasPaymentProvider` cria checkout RECURRENT mensal no sandbox Asaas e devolve `invoiceUrl`.
- DI: `PAYMENT_PROVIDER=asaas|fake`.
- Service grava `amountCents` oficiais; `GET /subscriptions/me` retorna `plans`.
- `/confirm` e webhook fake bloqueados quando provider=asaas.
- Enum de status expandido no backend.

## Contexto utilizado

- task 420, slice 039, handoff 419
- módulo subscriptions + docs Asaas Checkout
- `.env.example` (sem secrets)

## Handoff

- `.agents/state/handoffs/TASK-420.md`

## Arquivos alterados

- `backend/src/modules/subscriptions/providers/payment-provider.ts`
- `backend/src/modules/subscriptions/providers/fake-payment.provider.ts`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts`
- `backend/src/modules/subscriptions/subscriptions.module.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `backend/src/modules/subscriptions/subscriptions.service.spec.ts`
- `backend/src/modules/subscriptions/entities/subscription.entity.ts`
- `backend/.env.example`
- `tasks/change-requests/420-provider-asaas-checkout-mensal.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-420.md`

## Validacoes executadas

- `npm test -- --testPathPatterns=subscriptions` — 8 passed

## Pendencias pos-task

- Task 421: webhook Asaas + ciclo overdue/suspended/canceled/refund
- Task 422: UI abrir `invoiceUrl` do Asaas
- Confirmar no sandbox se `BOLETO` é aceito no Checkout (se API rejeitar, ajustar billingTypes)
- Reiniciar backend se necessário para ler `PAYMENT_PROVIDER=asaas` do `.env`

## Status final

done
