# Handoff — Task 781

## Status

done

## Decisões

- `POST /subscriptions/apple/confirm` paralelo ao Asaas
- `provider=apple`, `checkoutId=apple:{originalTransactionId}`
- Aceita recibo clássico (verifyReceipt) e JWS StoreKit 2 (decode claims; `APPLE_IAP_ALLOW_JWS_DECODE`)
- IAP mobile só para responsável

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/subscriptions/**` (controller, service, module, dto, verifier, spec)

## Validações

- `subscriptions.service.spec.ts` — 26 passed (inclui Apple IAP)

## Pendências

- Configurar `APPLE_IAP_SHARED_SECRET` / product no Connect
- Evoluir verificação JWS para App Store Server API (criptográfica)

## Próximo

- Task 782 (paywall) — código já iniciado; falta build Sandbox
