# Task 792 - Remover callback da assinatura PIX Asaas

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `POST /subscriptions/checkout` — sem mudança de contrato; o PIX continua retornando `invoiceUrl`

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Origem da solicitacao

Diagnóstico em produção: pagamento PIX devolve `ASAAS_PIX_SUBSCRIPTION_REJECTED` (503) com a mensagem "Asaas rejeitou a criação da assinatura PIX." A conta Asaas não tem site comercial cadastrado; o `callback.successUrl` faz a API recusar o `POST /subscriptions`. Sem `callback`, a criação funciona. Confirmação segue via webhook.

## Objetivo

Permitir criar assinatura PIX em produção sem depender do site cadastrado na conta Asaas.

## Comportamento esperado

- `POST /subscriptions` do fluxo PIX não envia `callback`.
- Checkout de cartão continua enviando `callback` (success/cancel/expired).
- Confirmação de pagamento PIX permanece por webhook/polling/`invoiceUrl`.
- Teste do provider cobre a ausência de `callback` no PIX.

## Fora de escopo

- Cadastrar o site na conta Asaas (ação no painel)
- Alterar checkout de cartão
- Front-end, mobile ou contrato OpenAPI
- Restaurar `successUrl` automaticamente quando o site for cadastrado

## Criterios de aceite

- [x] Payload PIX de `POST /subscriptions` não contém `callback`
- [x] Payload de cartão continua com `callback.successUrl`
- [x] Teste focado do provider cobre o PIX sem `callback`
- [x] Confirmação continua dependente de webhook/`invoiceUrl`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- esta task

## Contexto sob demanda

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts` — payload PIX
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts` — teste focado
- handoff Task 702 — histórico de fatura PIX hospedada
- `backend/docs/ai/AGENTS.md` — regras locais do backend

## Orçamento de contexto

- baixo — alteração localizada no adapter PIX
- estratégia: não carregar front, mobile, OpenAPI completo nem requirements

## Dependências

- Task 642 (diagnóstico de rejeição PIX)
- Task 702 (fatura PIX hospedada sem autoRedirect)

## Resultado da execucao

O `POST /subscriptions` do PIX deixou de enviar `callback`. A criação da assinatura não depende mais do site comercial cadastrado na conta Asaas. Cartão permanece com checkout hospedado e `callback`. Confirmação do PIX segue por webhook e `invoiceUrl`.

## Contexto utilizado

- Contexto mínimo da raiz, Slice 039 e esta task.
- Provider Asaas, teste unitário e `backend/docs/ai/AGENTS.md`.
- Diagnóstico do chat [Asaas payment errors](c3b4632d-20d7-4e49-9cc6-4b6b1fc576b2): sem `callback` a API aceita; com `successUrl` recusa.

## Handoff

`.agents/state/handoffs/TASK-792.md`

## Arquivos alterados

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts`
- `tasks/change-requests/792-remover-callback-assinatura-pix-asaas.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-792.md`

## Validacoes executadas

- `npm test -- --runInBand src/modules/subscriptions/providers/asaas-payment.provider.spec.ts` — 16 testes aprovados.

## Pendencias pos-task

- Validar PIX em produção após o backend recarregar/deployar.
- Cadastrar o site comercial na conta Asaas se quiser voltar a usar `successUrl` no PIX.
- O checkout de cartão continua no Asaas hospedado; o link enviado no diagnóstico abria PIX, não formulário de cartão.

## Status final

done
