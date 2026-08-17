# Handoff - Task 421

## Task

- identificador: 421
- status final: done

## Decisões preservadas

- Webhook `asaas-access-token` vs `PAYMENT_GATEWAY_WEBHOOK_SECRET` (se vazio em dev, aceita)
- OVERDUE 3 dias → SUSPENDED + user inactive
- Cancel/refund endpoints API (UI na 423)
- Idempotência via `subscription_webhook_events`

## Próxima ação

- Task 422 (feita em seguida) / 423 cancel UI
- Configurar webhook no painel Asaas apontando para `/api/subscriptions/webhooks/asaas`
