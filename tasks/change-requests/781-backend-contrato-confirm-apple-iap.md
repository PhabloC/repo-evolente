# Task 781 - Backend e contrato: confirmar Apple IAP

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `POST /subscriptions/apple/confirm`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 070 — `tasks/slices/070-iap-storekit-ios.md`

## Escopo

- OpenAPI + backend confirm Apple IAP com validação de recibo/JWS e liberação de acesso responsável.

## Criterios de aceite

- [x] OpenAPI cobre `POST /subscriptions/apple/confirm`
- [x] Conta responsável sem assinatura ativa passa a `active` após confirm válido
- [x] ProductId inválido / recibo inválido → 400
- [x] Papéis não-responsável → 403
- [x] Asaas continua intacto
- [x] Doc de processo atualizado
- [x] Teste unitário do fluxo Apple

## Resultado da execucao

- Endpoint `POST /subscriptions/apple/confirm` + `AppleIapVerifier` (verifyReceipt + JWS decode).
- Schema OpenAPI `ConfirmAppleIapRequest` e response `ServiceUnavailable`.
- Teste `confirma Apple IAP e libera acesso do responsável` passando.

## Contexto utilizado

- `backend/src/modules/subscriptions/`, `contracts/openapi.yaml`, doc ios-iap

## Handoff

- `.agents/state/handoffs/TASK-781.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/subscriptions/dto/confirm-apple-iap.dto.ts`
- `backend/src/modules/subscriptions/providers/apple-iap.verifier.ts`
- `backend/src/modules/subscriptions/subscriptions.controller.ts`
- `backend/src/modules/subscriptions/subscriptions.module.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `backend/src/modules/subscriptions/subscriptions.service.spec.ts`
- `docs/development/ios-iap-storekit.md`

## Validacoes executadas

- Jest `subscriptions.service.spec.ts` — 26 passed

## Pendencias pos-task

- Secrets Apple em produção
- Verificação criptográfica completa do JWS (App Store Server API) como hardening

## Status final

done
