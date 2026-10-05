# TASK-766

## Status

done

## Slice

- `tasks/slices/039-gateway-asaas-assinatura.md`

## Decisões

- Cancelar assinatura `active` mantém acesso até `accessEndsAt` (próximo aniversário mensal de `firstPaidAt`/`confirmedAt`) e cancela a renovação no Asaas.
- Reembolso, cancelamento de `overdue` e cancelamento pelo master continuam imediatos.
- Expiração lazy (me/gate/verify) + cron horário; vínculos do responsável só são cancelados na expiração.
- `PAYMENT_DELETED`/`CHECKOUT_*` ignorados em assinatura já cancelada.

## Validações

- Jest subscriptions (42), vitest util web (2), jest mobile subscription types (5), eslint nos arquivos alterados.
- Migração `1930000000000` aplicada em `82.112.244.57/evolente`.

## Pendências

- Webhooks Asaas não chegam (tabela de eventos vazia) — task própria.
- Validação visual dos cards no estado cancelado com acesso.

## Próximo contexto

- `backend/src/modules/subscriptions/subscriptions.service.ts` (cancel/expiry) e os dois `SubscriptionManagementCard`.
