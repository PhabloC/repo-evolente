# Handoff - Task 420

## Task

- identificador: 420
- título: Provider Asaas e checkout mensal
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- Slice 039
- status: todo (419, 420, 424, 425 done; 421–423 pendentes)

## Decisões preservadas

- decisão: Asaas Checkout `RECURRENT` + `MONTHLY` com `CREDIT_CARD`, `PIX`, `BOLETO`
- motivo: assinatura mensal + meios confirmados
- impacto: `AsaasPaymentProvider.createCheckout`

- decisão: confirmação Asaas só via webhook (Task 421); `/confirm` e webhook fake só com `fake`
- motivo: cutover seguro
- impacto: `assertFakeProviderOnly`

- decisão: valores default 7900/4900 via env com fallback
- motivo: planos oficiais
- impacto: persistência `amountCents` no checkout

- decisão: enum status expandido no entity (varchar; sem migration)
- motivo: alinhar contrato OpenAPI
- impacto: admin/update pode usar novos status; ciclo completo na 421

## Contexto utilizado

- subscriptions module, Asaas Checkout docs, .env.example

## Arquivos alterados

- providers asaas/fake/payment-provider
- subscriptions service/module/entity/specs
- `.env.example`
- task/index/slice/handoff

## Validações executadas

- subscriptions tests — 8 passed

## Pendências ou bloqueios

- Webhook (421) e UI checkout (422)
- `.env` local já com `PAYMENT_PROVIDER=asaas` + API key (não commitado)

## Próxima ação sugerida

- Task 421 (webhook + ciclo) ou 422 (UI abrir invoiceUrl)

## Próximo contexto recomendado

- handoff 420
- task 421
- Asaas webhook docs
- subscriptions.service / controller

## Contexto que não deve ser carregado na próxima etapa

- jogos / design-system prints
