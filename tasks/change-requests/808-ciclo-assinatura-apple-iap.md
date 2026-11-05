# Task 808 - Ciclo da assinatura Apple IAP

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `POST /subscriptions/apple/confirm`
- `POST /subscriptions/cancel`
- `POST /subscriptions/refund`
- `POST /subscriptions/webhooks/apple`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 070 — `tasks/slices/070-iap-storekit-ios.md`

## Escopo

- Persistir `expiresAt` da Apple em `accessEndsAt` e encerrar o acesso quando o período passa.
- Cancelar assinatura `provider=apple` só no banco, sem chamar o Asaas.
- Recusar reembolso local de compra Apple e orientar o estorno pela Apple.
- Receber App Store Server Notifications V2 (JWS verificado com Apple Root CA - G3) para renovar, cancelar no fim do período ou revogar na hora.
- Esconder o reembolso local na web e no app quando a assinatura é Apple.

## Fora de escopo

- App Store Server API para consulta ativa (issuer, key id, private key).
- Reembolso iniciado pelo backend na Apple.
- Google Play Billing.

## Criterios de aceite

- [x] Confirm Apple grava `accessEndsAt` e recusa recibo sem data de expiração.
- [x] Período vencido tira `accessGranted` e deixa de contar como ativa.
- [x] Cancel e refund de assinatura Apple não chamam o provedor Asaas.
- [x] Refund Apple responde `APPLE_REFUND_VIA_APP_STORE` sem revogar na hora.
- [x] Notificação `DID_RENEW` estende o período; `REFUND`/`EXPIRED` revogam.
- [x] Web e app não oferecem reembolso local para `provider=apple`.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- este arquivo
- `tasks/slices/070-iap-storekit-ios.md`
- `.agents/state/handoffs/TASK-781.md`

## Contexto sob demanda

- `backend/src/modules/subscriptions/` — regra de acesso, cancel, refund e verifier
- `contracts/openapi.yaml` paths `/subscriptions/apple/confirm`, `/cancel`, `/refund`, `/webhooks/asaas` — modelo do novo webhook
- `docs/development/ios-iap-storekit.md` — processo IAP
- cards de gestão já existentes (cópia, sem tela nova): `front-end/src/pages/Main/Settings/SubscriptionManagementCard.tsx` e `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`
- `backend/docs/ai/SECURITY.md` — webhook público

## Orçamento de contexto

- médio; um fluxo de assinatura Apple, sem redesign e sem App Store Server API
- referência visual: cards existentes; a mudança é texto e ocultar o botão de reembolso quando `provider=apple`

## Resultado da execucao

- Backend grava `expiresAt` em `accessEndsAt`, expira o acesso no gate e no cron, cancela Apple só no banco e recusa reembolso local.
- `POST /api/subscriptions/webhooks/apple` verifica o JWS com a Apple Root CA - G3 e aplica renovação, fim de período e revogação.
- Web e app ocultam o reembolso local quando `provider=apple` e explicam o cancelamento da cobrança em Ajustes.
- Slice 070 permanece `in_progress` (Sandbox e URL do webhook ainda são passo humano).
- Contrato: path e schema do webhook; descrição de refund distingue Apple e Asaas.
- Referência visual: cards de gestão já existentes; só texto e ocultação do botão.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, slice 070, task 808, handoff 781.
- Sob demanda: módulo de assinaturas, OpenAPI de subscription, doc IAP, cards web/mobile, `backend/docs/ai/SECURITY.md`.
- Evitado: `requirements/` e `design-system/` (sem tela nova).

## Handoff

- `.agents/state/handoffs/TASK-808.md`
- Próximo contexto: cadastrar a URL do webhook no App Store Connect.

## Arquivos alterados

- `backend/src/modules/subscriptions/` (service, controller, verifier, JWS, repositórios, DTO, utils, testes)
- `contracts/openapi.yaml`
- `docs/development/ios-iap-storekit.md`
- `backend/.env.example`
- `front-end/src/pages/Main/Settings/SubscriptionManagementCard.tsx`
- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`

## Validacoes executadas

- Jest `subscriptions.service.spec.ts`, `apple-jws.spec.ts`, `apple-notification.util.spec.ts`: passou
- `tsc --noEmit`: arquivos desta task sem erro novo

## Pendencias pos-task

- Cadastrar `https://api.evolente.com.br/api/subscriptions/webhooks/apple` no App Store Connect (produção e sandbox), versão 2.
- Assinaturas Apple já gravadas sem `accessEndsAt` só recebem prazo na próxima confirmação, restauração ou notificação.

## Status final

done
