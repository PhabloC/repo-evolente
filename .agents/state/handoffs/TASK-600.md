# Handoff TASK-600

## Status

done

## Objetivo

Simplificar o CTA da confirmação de cancelamento de assinatura no perfil mobile.

## Decisões

- Apenas a copy do cancelamento mudou para `Confirmar`.
- Reembolso e estado de processamento foram preservados.

## Contexto utilizado

- Task 600, Slice 039, handoff da Task 599 e `SubscriptionManagementCard`.

## Arquivos alterados

- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`

## Validações

- `npx eslint src/features/shell/components/SubscriptionManagementCard/index.tsx` — passou

## Pendências

- Nenhuma.

## Próximo contexto recomendado

- Nenhum; task concluída.
