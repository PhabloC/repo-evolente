# Handoff TASK-599

## Status

done

## Objetivo

Cancelar / reembolsar assinatura no perfil mobile do responsável (paridade com a web).

## Decisões

- UI no card clay do perfil (`SubscriptionManagementCard` no shell)
- APIs: `GET /subscriptions/me`, `POST /cancel`, `POST /refund`
- Reembolso só na janela de 3 dias
- Pós-sucesso: logout (equivalente ao redirect `/assinatura` na web)
- Checkout/reativação continua só na web

## Arquivos

- `mobile/src/features/profile/services/subscriptionService.ts`
- `mobile/src/features/profile/types/subscription.ts`
- `mobile/src/features/shell/components/SubscriptionManagementCard/`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Validação

- unit test `isRefundEligible` ok

## Próximo

Testar no device/emulador com usuário responsável com assinatura ativa.
