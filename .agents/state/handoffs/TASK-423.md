# Handoff - Task 423

## Task

- identificador: 423
- título: Cancelamento/reembolso web e gate mobile
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 039
- objetivo de negócio: Asaas + ciclo assinatura
- entrega verificável: cancel/refund na web com bloqueio; mobile só avisa web
- status do slice: done (419–425)

## Decisões preservadas

- decisão: gestão financeira só na web (Configurações → card Assinatura)
- motivo: mobile sem checkout Asaas nesta fase
- impacto: `SubscriptionManagementCard` + copy mobile

- decisão: reembolso só se `firstPaidAt` / `refundEligibleUntil` dentro de 3 dias; senão hint sem botão
- motivo: regra de negócio Slice 039
- impacto: UI oculta CTA fora da janela

- decisão: após cancel/refund → `setAccessGranted(false)` + navigate `/assinatura`
- motivo: bloqueio imediato + retorno ao gate
- impacto: usuário não permanece nas rotas principais

- decisão: master não vê o card
- motivo: isento de assinatura
- impacto: `role === 'master'` → `null`

## Contexto utilizado

### Contexto mínimo lido

- task 423, slice 039, Settings, subscriptionService, home/perfil mobile

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| OpenAPI cancel/refund | API client | `subscriptionService` |
| DS implícito Settings | UI | Card + CSS módulo |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| jogos / admin planos | fora do escopo |
| docs Asaas API | já coberto na 420/421 |

## Resultado por stack

- front-end: card cancel/refund em Settings; redirect ao gate
- backend: sem alteração nesta task (421)
- mobile: copy home + perfil responsável

## Arquivos alterados

- `front-end/src/pages/Main/Settings/SubscriptionManagementCard.tsx`
- `front-end/src/pages/Main/Settings/subscriptionManagement.module.css`
- `front-end/src/pages/Main/Settings/index.tsx`
- `front-end/src/services/subscriptions/subscriptionService.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/423-cancelamento-reembolso-web-e-gate-mobile.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`

## Validações executadas

- validação: lints Settings/card — ok
- validação: tsc front filtrado Settings — sem erros nesses arquivos

## Pendências ou bloqueios

- Webhook Asaas: URL pública + `PAYMENT_GATEWAY_WEBHOOK_SECRET` no `.env` (humano)
- Teste E2E sandbox: pagar → webhook → cancel/refund em Perfil

## Próxima ação sugerida

- Configurar webhook Asaas e validar fluxo sandbox ponta a ponta
- Sem task de código restante no Slice 039

## Próximo contexto recomendado

- `.env` backend (`ASAAS_*`, `PAYMENT_PROVIDER`)
- docs Asaas webhook + `subscriptions.service` handleAsaasWebhook

## Contexto que não deve ser carregado na próxima etapa

- jogos / redesign admin
- planejar novo slice sem necessidade humana
