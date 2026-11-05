# IAP StoreKit no iOS (Evolente)

Documento vivo do processo para atender a Guideline **3.1.1** da App Store.
Atualizar este arquivo a cada avanço das tasks do Slice 070.

## 1. Por que estamos fazendo isso

A Apple rejeitou o app porque ele **acessa conteúdo/serviço digital** (trilha, jogos, vídeos, área logada do responsável) liberado por assinatura comprada **fora** do app (Asaas na web), sem oferecer a mesma compra via **In-App Purchase**.

Não basta “só ter login” no mobile: o login entrega o benefício pago.

Referência da rejeição: `erro_aprovacao.md` (também Guideline 2.5.4 — `UIBackgroundModes` audio; tratado em `mobile/app.json` via `expo-audio` com background desligado).

## 2. Decisões de produto

| Decisão | Escolha |
|---|---|
| Repositório | Um único app Expo (não split Android/iOS) |
| Branches | Feature temporária; **não** branches permanentes por plataforma |
| Web / Android | Continuam com **Asaas** (Android já aprovado sem checkout in-app) |
| iOS | **StoreKit / IAP** obrigatório para o plano digital do responsável |
| Profissional no mobile | Shell não suportado → IAP mobile focado em **responsável** |
| Remover Asaas? | **Não** |

## 3. Fluxo do usuário (iOS)

```
Login
  → JWT ok
  → GET /subscriptions/me
       ├─ accessGranted=true  → shell (home/trilha)
       └─ accessGranted=false → tela Assinar (StoreKit)
              → compra ou restaurar
              → POST /subscriptions/apple/confirm
              → accessGranted=true → shell
```

Android: sem tela IAP; login sem acesso continua bloqueado/orientando pagamento na web.

## 4. App Store Connect (manual — pendente humano)

Checklist:

1. [x] Acordo de apps pagos / Paid Applications ativo
2. [x] Grupo de assinaturas (ex.: Evolente)
3. [x] Produto mensal responsável, product id: `br.com.evolente.responsavel.monthly` (R$ 49)
4. [x] Texto de assinatura (PT-BR)
5. [ ] Conta Sandbox para testes
6. [x] Shared Secret → `APPLE_IAP_*` no `.env` do **backend** (não no mobile)

Sem produtos criados no Connect, a compra no app falha mesmo com código pronto.

## 5. Arquitetura técnica

### Backend

- Provedor Asaas permanece o default de checkout web (`PAYMENT_PROVIDER=asaas`).
- Novo caminho paralelo: `POST /subscriptions/apple/confirm`
  - Body: `productId`, `transactionId`, `originalTransactionId`, `receiptData` (ou JWS StoreKit 2 — ver implementação)
  - Valida com Apple
- Persiste `Subscription` com `provider=apple`, `checkoutId=apple:{originalTransactionId}`
- Grava `accessEndsAt` com a data de expiração da Apple. Sem essa data a confirmação é recusada.
- Status `active` enquanto o período não venceu. Ao vencer, o acesso cai e a assinatura deixa de contar como ativa.
- `POST /api/subscriptions/webhooks/apple` recebe App Store Server Notifications V2. O JWS é verificado com a Apple Root CA - G3. Renovação estende o período; cancelamento da renovação mantém o acesso até `accessEndsAt`; expiração, reembolso e revogação cortam o acesso na hora.
- Cancelar uma assinatura Apple no app só atualiza o banco. A cobrança da Apple é cancelada em Ajustes → Assinaturas. Reembolso não passa pelo Asaas: a Apple estorna e o webhook encerra o acesso.

Env vars previstas:

| Variável | Uso |
|---|---|
| `APPLE_IAP_SHARED_SECRET` | verifyReceipt (assinaturas) |
| `APPLE_IAP_PRODUCT_RESPONSAVEL` | product id esperado (default `br.com.evolente.responsavel.monthly`) |
| `APPLE_IAP_BUNDLE_ID` | `br.com.evolente` |

### Mobile

- Lib IAP compatível com Expo 57 (definir na task 782: `expo-iap` ou `react-native-iap`).
- Código de compra/paywall atrás de `Platform.OS === 'ios'`.
- Ajuste do `authService`: no iOS, ausência de `accessGranted` não encerra o login com erro genérico; encaminha ao paywall.

### Contrato

- Path planejado: `/subscriptions/apple/confirm` (task 781).

## 6. O que muda na UI

- **Nova tela** Assinar (só iOS): plano, preço, Assinar, Restaurar.
- Login / home / trilha: iguais para quem já tem acesso.
- Android: sem mudança de checkout.

## 7. Testes

1. Build EAS iOS (dev/preview) com IAP
2. Conta Sandbox na App Store do device
3. Login responsável sem assinatura Asaas → paywall
4. Comprar → backend confirma → entra no app
5. Reinstalar → Restaurar compras
6. Conta já paga no Asaas → entra sem paywall
7. Android regression: login sem IAP UI

## 8. Reenvio à App Store

1. Confirmar remoção de `audio` em `UIBackgroundModes` (plugin `expo-audio` com background off) no build nativo
2. IAP funcional em Sandbox + produtos aprovados/pending no Connect
3. Notas de review: explicar que assinatura digital está disponível via IAP; web/Asaas é multiplataforma (3.1.3b) **com** IAP também disponível
4. Conta demo se necessário (login + instrução Sandbox)

## 9. Status da implementação

| Item | Status | Task |
|---|---|---|
| Slice 070 criado | feito | — |
| Este documento | feito (vivo) | 780 |
| OpenAPI `apple/confirm` | feito (código) | 781 |
| Backend confirm + validação Apple | feito (código; JWS com cadeia Apple e OID de recibo, ou verifyReceipt) | 781 |
| Paywall mobile iOS (`expo-iap`) | feito (código) | 782 |
| Env `APPLE_IAP_*` em produção | pendente humano | — |
| Produtos App Store Connect | pendente humano | — |
| Build EAS nativo iOS + Sandbox | pendente | — |
| Apple Server Notifications v2 | feito (código; URL no App Store Connect é passo humano) | 808 |

### Env vars backend

```
APPLE_IAP_SHARED_SECRET=
APPLE_IAP_PRODUCT_RESPONSAVEL=br.com.evolente.responsavel.monthly
APPLE_IAP_BUNDLE_ID=br.com.evolente
APPLE_IAP_ALLOW_JWS_DECODE=true
```

### Product ID mobile

`br.com.evolente.responsavel.monthly` — espelhar no App Store Connect.

## 10. Tasks do backlog

- `tasks/slices/070-iap-storekit-ios.md`
- `tasks/change-requests/780-documentar-processo-iap-storekit-ios.md`
- `tasks/change-requests/781-backend-contrato-confirm-apple-iap.md`
- `tasks/change-requests/782-mobile-paywall-storekit-ios.md`
- `tasks/change-requests/808-ciclo-assinatura-apple-iap.md`

## 11. Histórico curto

- **2026-10-08** — Decisão de implementar IAP só iOS; doc criado; slice/tasks abertas. Fix `expo-audio` background já aplicado em `mobile/app.json` em sessão anterior.
- **2026-10-08 (tarde)** — Endpoint `POST /subscriptions/apple/confirm`, verifier Apple, paywall `SubscribeScreen` + `expo-iap`, gate iOS no login. Pendente: produtos no Connect, secrets, build nativo e testes Sandbox.
- **2026-11-04** — `accessEndsAt` da Apple passa a valer; cancel/reembolso Apple não chama o Asaas; webhook `POST /subscriptions/webhooks/apple`. Pendente humano: cadastrar essa URL em App Store Connect (Server Notifications V2). Assinaturas já gravadas sem data de expiração só recebem o prazo na próxima confirmação, restauração ou notificação.
- **2026-11-04** — JWS sem cadeia ou sem o OID de recibo da App Store é recusado. Notificação sem assinatura local responde 503 para a Apple reenviar. Carência de cobrança estende `accessEndsAt`.
