# Slice 070 - IAP StoreKit no iOS

## Status

in_progress

> Código MVP (contrato + backend + paywall iOS) entregue nas tasks 780–782.
> Slice permanece `in_progress` até produto App Store Connect + build Sandbox + reenvio à review.

## Objetivo de negocio

Atender a rejeição App Store (Guideline 3.1.1): permitir que o responsável compre/restaure a assinatura digital pelo **In-App Purchase (StoreKit)** no iOS, mantendo Asaas na web/Android.

## Entrega verificavel

- Conta responsável sem `accessGranted` no iOS vê tela de Assinar (IAP) após login.
- Compra Sandbox/produção via StoreKit confirma no backend e libera `accessGranted`.
- Restaurar compras reativa acesso da mesma conta Apple → Evolente.
- Android permanece sem checkout in-app (Asaas/web).
- Documentação viva do processo em `docs/development/ios-iap-storekit.md`.

## Fora de escopo

- Google Play Billing
- IAP para profissional no mobile (shell mobile do profissional não é suportado)
- Remover Asaas da web
- Entitlement External Link Account / Alternative Payments EUA
- Webhook Apple Server Notifications v2 completo (pode ficar em task follow-up; MVP valida na confirmação)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- backend
- mobile
- contracts (OpenAPI)
- docs (raiz)

## Contrato

- `POST /subscriptions/apple/confirm`
- `POST /subscriptions/apple/restore` (opcional se restore reutilizar confirm)
- schemas de request/response alinhados a `SubscriptionConfirmResponse` / `SubscriptionStatusResponse`

## Referencia visual por stack

### Mobile

- tipo: artefato de design system
- fonte primaria: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- lacunas: paywall IAP sem print dedicado — uma tela simples com tokens Evolente (marca, CTA único, sem clutter)

### Web

- sem UI nesta slice (Asaas permanece)

## Permissoes e atores

- Responsável: compra/restaura IAP no iOS
- Master: isento (sem paywall)
- Profissional: continua pagando na web; app mobile não é shell suportado

## Decisoes humanas confirmadas (2026-10-08)

- Manter um único repositório mobile; IAP só com `Platform.OS === 'ios'`
- Não separar branch permanente Android/iOS
- Asaas permanece na web; Android aprovado sem checkout in-app
- StoreKit é o caminho para a Apple; não alegar “só login” como isenção

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- `erro_aprovacao.md` (rejeição Apple 3.1.1 / 2.5.4)
- `docs/development/ios-iap-storekit.md`

## Contexto sob demanda

| Gatilho | Fonte |
|---|---|
| Gate de assinatura | `backend/src/modules/subscriptions/` |
| Login mobile bloqueia sem acesso | `mobile/src/features/auth/services/authService.ts` |
| Contrato | `contracts/openapi.yaml` paths `/subscriptions/*` |
| Fix background audio (paralelo) | `mobile/app.json` plugin `expo-audio` |

## Tasks relacionadas

- `tasks/change-requests/780-documentar-processo-iap-storekit-ios.md`
- `tasks/change-requests/781-backend-contrato-confirm-apple-iap.md`
- `tasks/change-requests/782-mobile-paywall-storekit-ios.md`

## Orçamento de contexto

- médio-alto; fatiar em 3 tasks (doc → back/contrato → mobile)
- bloquear se tentar implementar webhook Apple completo + RevenueCat + redesign na mesma task
