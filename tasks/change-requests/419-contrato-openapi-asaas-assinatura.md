# Task 419 - Contrato OpenAPI: Asaas e ciclo de assinatura

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend (contrato)
- front-end (consumidor futuro)
- mobile (consumidor de status)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` subscription (atualizar)

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Atualizar o OpenAPI para refletir checkout Asaas, webhook real, cancelamento, reembolso e status de ciclo (incluindo atraso/inativação), alinhado às regras confirmadas em requirements.

## Dependencias

- Slice 005 / Tasks 012–013 (base fake) — done
- Requirements atualizados (valores, Asaas, regras) — done

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `requirements/001-escopo-produto.md` (seção 8)
- `requirements/002-regras-de-negocio.md` (seção 5)

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Paths atuais | `contracts/openapi.yaml` `/subscriptions/*` | evoluir sem quebrar consumidores |
| Fake webhook | path `/subscriptions/webhooks/fake` | restringir a modo fake ou documentar deprecação |

## Orçamento de contexto

- baixo
- só contrato + seções de requirements de pagamento
- estrategia de reducao: não carregar UI nem implementação backend

## Criterios de aceite

- [x] Documentar planos: profissional `7900`, responsável `4900`, mensal, BRL
- [x] Checkout descreve meios: cartão, PIX, boleto via Asaas
- [x] Webhook Asaas autenticado (secret) no contrato
- [x] Endpoints (ou operações) de cancelamento e reembolso com regras: bloqueio imediato; reembolso só até 3 dias de uso
- [x] Status cobre ciclo `PENDING` → `ACTIVE` → `OVERDUE` → `SUSPENDED` → `CANCELED` (mais `refused` no checkout)
- [x] Master isento permanece explícito
- [x] Fake confirm/webhook documentados como apenas `PAYMENT_PROVIDER=fake`

## Fora de escopo

- Implementar provider ou UI
- Criar conta Asaas

## Referencia visual

- nao se aplica

## Resultado da execucao

- Requirements 001/002 atualizados com ciclo de estados e regras Asaas.
- OpenAPI: enum `SubscriptionStatus` expandido; paths `cancel`, `refund`, `webhooks/asaas`; checkout com planos/meios; fake restrito a `PAYMENT_PROVIDER=fake`.
- Payload documenta enums em lowercase (`pending`…`canceled`); descrição usa a nomenclatura canônica PENDING→…→CANCELED.

## Contexto utilizado

- contexto mínimo: raiz, task 419, slice 039, requirements § pagamento
- contexto sob demanda: `contracts/openapi.yaml` paths/schemas subscription
- contexto evitado: front-end, mobile, implementação backend, design-system

## Handoff

- `.agents/state/handoffs/TASK-419.md`

## Arquivos alterados

- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/change-requests/419-contrato-openapi-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-419.md`

## Validacoes executadas

- parse YAML do OpenAPI via `yaml` (Node) — ok
- correção colateral: newline quebrado em `info.description` + quote em `Conflict.description`

## Pendencias pos-task

- Executar Task 420 (provider Asaas + checkout)
- Backend ainda usa enum antigo (`pending|active|refused`) até 420/421

## Status final

done
