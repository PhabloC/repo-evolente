# Handoff - Task 808

## Task

- identificador: 808
- título: Ciclo da assinatura Apple IAP
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 070
- objetivo de negócio: assinatura iOS via StoreKit, Asaas na web/Android
- entrega verificável: prazo da Apple persistido, cancel/reembolso Apple fora do Asaas, webhook de notificação

## Decisões preservadas

- decisão: `accessEndsAt` recebe `expiresAt` da Apple; confirmação sem data é recusada
- motivo: status `active` sem data deixava o acesso permanente
- impacto: o gate e o cron encerram o acesso quando a data passa
- decisão: cancelamento Apple só no banco; reembolso local responde `APPLE_REFUND_VIA_APP_STORE`
- motivo: o id da transação Apple não existe no Asaas
- impacto: a cobrança recorrente da Apple continua até o usuário cancelar em Ajustes; o estorno chega pelo webhook
- decisão: `POST /api/subscriptions/webhooks/apple` exige JWS com cadeia até a Apple Root CA - G3 e OID de recibo no certificado folha; `bundleId` é obrigatório
- motivo: certificado de desenvolvedor também encadeia na mesma raiz, e o endpoint é público
- impacto: a URL precisa ser cadastrada no App Store Connect (Server Notifications V2)
- decisão: confirmação StoreKit 2 não decodifica JWS sem verificar a cadeia
- motivo: o fallback aceitava claims sem assinatura
- impacto: `APPLE_IAP_ALLOW_JWS_DECODE=false` continua exigindo o recibo clássico
- decisão: notificação sem assinatura local responde 503 e não grava o evento
- motivo: 200 fazia a Apple parar de reenviar um reembolso que chegou antes do confirm
- decisão: `DID_FAIL_TO_RENEW` em carência grava `gracePeriodExpiresDate` em `accessEndsAt`
- motivo: o prazo do período pago já pode ter passado enquanto a Apple ainda retenta a cobrança

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/070-iap-storekit-ios.md`
- `tasks/change-requests/808-ciclo-assinatura-apple-iap.md`
- `.agents/state/handoffs/TASK-781.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `backend/src/modules/subscriptions/` | regra de acesso, cancel, refund e verifier | implementação |
| `contracts/openapi.yaml` paths de subscription | novo webhook e texto de refund | contrato |
| `docs/development/ios-iap-storekit.md` | processo IAP | atualização |
| cards de gestão web e mobile | `provider=apple` | ocultar reembolso local |
| `backend/docs/ai/SECURITY.md` | webhook público | JWS assinado |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` | sem ambiguidade de negócio além do bug já confirmado |
| `design-system/` | cópia nos cards existentes, sem tela nova |

## Resultado por stack

- front-end: card de assinatura explica Apple e não oferece reembolso local
- backend: prazo, cancel/refund e webhook
- mobile: mesmo ajuste de cópia no card de gestão

## Arquivos alterados

- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `backend/src/modules/subscriptions/subscriptions.controller.ts`
- `backend/src/modules/subscriptions/subscriptions.service.spec.ts`
- `backend/src/modules/subscriptions/providers/apple-iap.verifier.ts`
- `backend/src/modules/subscriptions/providers/apple-jws.ts`
- `backend/src/modules/subscriptions/providers/apple-root-ca-g3.ts`
- `backend/src/modules/subscriptions/utils/apple-notification.util.ts`
- `backend/src/modules/subscriptions/dto/apple-server-notification.dto.ts`
- `contracts/openapi.yaml`
- `docs/development/ios-iap-storekit.md`
- `front-end/src/pages/Main/Settings/SubscriptionManagementCard.tsx`
- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`

## Validações executadas

- validação: Jest `subscriptions.service.spec.ts`, `apple-jws.spec.ts`, `apple-notification.util.spec.ts` — passou
- validação: `tsc --noEmit` nos arquivos desta task — sem erro novo; o projeto já tem erros de spec fora deste escopo

## Pendências ou bloqueios

- item: cadastrar `POST /api/subscriptions/webhooks/apple` no App Store Connect (produção e sandbox)
- item: assinaturas Apple já salvas com `accessEndsAt` nulo só ganham prazo na próxima confirmação, restauração ou notificação

## Próxima ação sugerida

- próxima task ou próximo passo: configurar a URL de Server Notifications V2 e validar em Sandbox

## Próximo contexto recomendado

- arquivos/trechos que devem ser carregados: `docs/development/ios-iap-storekit.md`, `backend/src/modules/subscriptions/subscriptions.service.ts`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `requirements/` e `design-system/`
- motivo: não se aplicam ao cadastro do webhook na Apple
