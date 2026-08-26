# Handoff TASK-628

## Status final

done

## Decisões preservadas

- `inspectRemotePayment` só confirma pagamento quando `checkoutSession` ou `subscription` bate com o checkout atual; `externalReference` genérico não basta.
- `linkByCode` converte vínculo `CANCELED` existente para `PENDING` se `guardian.subscriptionAccessGranted`; caso contrário, `403`.
- `verifyPayment` chama `enforceOverdueSuspensionForUser` antes de decidir acesso e usa `isAccessGrantedForSubscription` no retorno.

## Arquivos alterados

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- specs correspondentes

## Validações

- jest nos 3 spec files — 51 testes passando
