# Task 599 - Cancelar e reembolsar assinatura no perfil mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `GET /subscriptions/me`, `POST /subscriptions/cancel`, `POST /subscriptions/refund`

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Espelhar na versão mobile (perfil do responsável) as ações já existentes na web: **Cancelar assinatura** e **Solicitar reembolso** (janela de 3 dias), com confirmação e bloqueio imediato de acesso.

## Dependencias

- Task 423 (web cancel/refund + aviso mobile) — done
- Task 469 (modal de confirmação web) — done

## Contexto mínimo

- esta task
- slice 039
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/profile/`
- referência de comportamento: `front-end/src/pages/Main/Settings/SubscriptionManagementCard.tsx`
- `front-end/src/services/subscriptions/subscriptionService.ts` (cancel/refund)

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| UI confirm | `mobile/src/shared/components/AppConfirmModal/` | modal de confirmação |
| DS mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | tokens/copy se necessário |
| Docs mobile | `mobile/docs/ai/ARCHITECTURE.md`, `COMPONENT_REUSE.md` | padrões de feature |

## Orçamento de contexto

- medio
- estrategia: só perfil do responsável + service de assinatura; sem checkout Asaas no app; sem shell profissional

## Criterios de aceite

- [x] Perfil do responsável exibe status da assinatura e ações quando `active` ou `overdue`
- [x] **Cancelar assinatura** confirma via modal → `POST /subscriptions/cancel` → acesso bloqueado
- [x] **Solicitar reembolso** só na janela de 3 dias (`refundEligibleUntil` / `firstPaidAt`) → `POST /subscriptions/refund`
- [x] Após sucesso: sessão limpa / usuário sem acesso (logout equivalente ao gate web)
- [x] Master não gerencia assinatura própria neste fluxo (shell responsável)
- [x] Checkout/reativação continua na web (copy clara)

## Fora de escopo

- Checkout Asaas no mobile
- Shell/perfil profissional mobile
- Alterações no backend (já implementado)

## Referencia visual

### Mobile

- Artefato DS mobile + paridade comportamental com o card web de Configurações (sem print dedicado de cancel/refund)
- Não inferir layout web pixel a pixel; usar componentes mobile existentes (`Button`, `AppConfirmModal`, cards clay do perfil)

## Resultado da execucao

- Card **Assinatura** no perfil do responsável com status, cancelar e reembolso (3 dias)
- `subscriptionService` mobile chama `/subscriptions/me|cancel|refund`
- Confirmação via `AppConfirmModal`; sucesso faz logout (bloqueio imediato)
- Reativação/checkout permanece na web

## Contexto utilizado

- Task 599, slice 039, card web de referência, `AppConfirmModal`, perfil responsável

## Handoff

- `.agents/state/handoffs/TASK-599.md`

## Arquivos alterados

- `mobile/src/features/profile/types/subscription.ts`
- `mobile/src/features/profile/types/subscription.test.ts`
- `mobile/src/features/profile/services/subscriptionService.ts`
- `mobile/src/features/shell/components/SubscriptionManagementCard/`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/599-cancelar-reembolsar-assinatura-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Validacoes executadas

- `npx jest src/features/profile/types/subscription.test.ts` — 3 passed
- Lint IDE nos arquivos novos — sem erros
- tsc do mobile tem erros pré-existentes em outros módulos; nenhum erro nos arquivos desta task

## Pendencias pos-task

- Validação manual no app com assinatura active + janela de reembolso
- Profissional continua só na web (sem shell mobile)

## Status final

done
