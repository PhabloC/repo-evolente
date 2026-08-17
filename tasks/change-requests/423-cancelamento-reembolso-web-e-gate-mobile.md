# Task 423 - Cancelamento/reembolso web e gate mobile

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` cancel / refund / subscriptions/me

## Modo de execucao

cross-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Permitir cancelamento e reembolso (dentro da janela) na web com bloqueio imediato, e refletir perda de acesso no app mobile com mensagem clara (checkout permanece na web).

## Dependencias

- Task 421
- Task 422

## Contexto mínimo

- esta task
- slice 039
- handoffs 421 e 422
- gate/perfil web de assinatura
- `mobile/src/features/profile/` e home responsável (aviso sem acesso)

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| DS web | `design-system/front/Design_System_Evolente_Desktop.md` | UI cancel/refund |
| DS mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | copy/estado sem acesso |
| Docs stacks | `front-end/docs/ai/`, `mobile/docs/ai/` | padrões |

## Orçamento de contexto

- medio
- estrategia: só telas de assinatura/perfil; sem jogos/admin

## Criterios de aceite

- [x] Web: ação de cancelar → confirma → bloqueio imediato e retorno ao gate
- [x] Web: reembolso disponível só nos 3 primeiros dias de uso; fora da janela, ação ausente ou erro claro
- [x] Reembolso bem-sucedido cancela e bloqueia na hora
- [x] Mobile: quando `accessGranted=false` / assinatura inativa, mostra aviso e orienta regularizar na web (sem checkout Asaas no app nesta fase)
- [x] Master não vê cancel/refund de assinatura própria (isento)

## Fora de escopo

- Checkout Asaas no mobile
- Push de cobrança

## Referencia visual

### Web

- artefato DS desktop (assinatura); sem print dedicado de cancel/refund

### Mobile

- artefato DS mobile + estados já usados no perfil/home para assinatura sem acesso

## Resultado

### Front-end

- Card em Configurações (`SubscriptionManagementCard`) com status, cancelar e reembolso (janela 3 dias)
- Confirmação → `POST /subscriptions/cancel` ou `/refund` → `accessGranted=false` → redirect `/assinatura`
- Master: card não renderiza

### Mobile

- Home e perfil do responsável: copy orientando regularizar no site (sem checkout no app)

## Status final

done
