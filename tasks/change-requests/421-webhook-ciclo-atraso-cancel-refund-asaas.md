# Task 421 - Webhook Asaas e ciclo (atraso, cancel, refund)

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Slice vertical

- `tasks/slices/039-gateway-asaas-assinatura.md`

## Criterios de aceite

- [x] Webhook Asaas validado com `PAYMENT_GATEWAY_WEBHOOK_SECRET`
- [x] Pagamento confirmado → `active` + `accessGranted=true`
- [x] Atraso → `overdue`; após **3 dias** → `suspended` + inativa conta
- [x] Cancelamento → `canceled` + bloqueio imediato
- [x] Reembolso até 3 dias → `canceled`; fora da janela rejeita
- [x] Regularização overdue → active via PAYMENT_RECEIVED
- [x] Idempotência de webhook
- [x] Testes

## Resultado da execucao

- `POST /subscriptions/webhooks/asaas` com header `asaas-access-token`
- `POST /subscriptions/cancel` e `/refund`
- Campos de ciclo + tabela `subscription_webhook_events`
- Migration `1850000000000` aplicada

## Handoff

- `.agents/state/handoffs/TASK-421.md`

## Status final

done
