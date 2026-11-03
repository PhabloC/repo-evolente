# Task 806 - Aceitar envelope real do webhook Asaas sem 400

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

- `POST /subscriptions/webhooks/asaas`
- `contracts/openapi.yaml#/components/schemas/AsaasSubscriptionWebhookRequest`

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Origem da solicitacao

Painel Asaas de produção penalizou `https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas` com `400 Bad Request` no evento `PAYMENT_CREATED`. O envelope oficial inclui `dateCreated` e `account`, rejeitados pelo `ValidationPipe` global (`forbidNonWhitelisted: true`). Confirmação: o mesmo host responde `401` para `{ event, payment }` sem extras e `400` com o envelope real.

## Objetivo

Fazer o webhook Asaas aceitar o envelope oficial (e campos extras futuros) e responder 2xx para eventos válidos, evitando nova penalização.

## Comportamento esperado

- `POST /subscriptions/webhooks/asaas` aceita `dateCreated`, `account` e demais propriedades de topo do Asaas.
- Continua exigindo `event` string e autenticando por `asaas-access-token`.
- Evento sem assinatura local continua `200` com `{ received: true }`.
- Contrato OpenAPI documenta o envelope com `additionalProperties: true`.

## Fora de escopo

- Alterar ciclo de assinatura ou matching de checkout.
- Configurar o painel Asaas ou fazer deploy.
- Front-end e mobile.

## Criterios de aceite

- [x] Envelope real do Asaas (`dateCreated` + `account` + `payment`) não retorna 400.
- [x] Campos extras de topo não derrubam o webhook.
- [x] Sem `event` válido ainda retorna 400.
- [x] E2E cobre o payload penalizado em produção.
- [x] OpenAPI marca `additionalProperties: true` no envelope.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- esta task

## Contexto sob demanda

- `backend/src/main.ts` — `ValidationPipe` com `forbidNonWhitelisted`
- `backend/src/modules/subscriptions/dto/asaas-webhook.dto.ts` — contrato HTTP
- `backend/src/modules/subscriptions/subscriptions.controller.ts` — borda do webhook
- `backend/test/app.e2e-spec.ts` — regressão da rota pública
- `contracts/openapi.yaml#/components/schemas/AsaasSubscriptionWebhookRequest`
- `backend/docs/ai/SECURITY.md` — DTO + class-validator na borda

## Orçamento de contexto

- baixo — correção localizada na borda HTTP do webhook
- estratégia: não carregar front, mobile, requirements nem o provider Asaas

## Dependências

- Task 421 (webhook e ciclo)
- Task 639 (rota pública `/api/subscriptions/webhooks/asaas`)
- Task 652 (URL de produção; permanece blocked na configuração do painel)

## Resultado da execucao

O 400 da penalização vinha do `ValidationPipe` global (`forbidNonWhitelisted: true`), não do ciclo de assinatura. O envelope oficial do Asaas traz `dateCreated` e `account`, que o DTO antigo não declarava. A rota agora lê o body sem essa rejeição, valida só `event`/objetos conhecidos e ignora extras de topo. Produção ainda responde 400 até o backend ser publicado com este patch.

## Contexto utilizado

- Contexto mínimo da raiz, Slice 039 e esta task.
- `backend/src/main.ts`, DTO/controller do webhook, e2e da rota, OpenAPI do envelope.
- `backend/docs/ai/SECURITY.md`, `CODE_STYLE.md` e `ARCHITECTURE.md`.
- POST real em `https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas`: envelope oficial → 400; `{ event, payment }` → 401.

## Handoff

`.agents/state/handoffs/TASK-806.md`

## Arquivos alterados

- `backend/src/modules/subscriptions/dto/asaas-webhook.dto.ts`
- `backend/src/modules/subscriptions/dto/asaas-webhook.dto.spec.ts`
- `backend/src/modules/subscriptions/subscriptions.controller.ts`
- `backend/test/app.e2e-spec.ts`
- `contracts/openapi.yaml`
- `tasks/change-requests/806-aceitar-envelope-real-webhook-asaas.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-806.md`

## Validacoes executadas

- `npm test -- --runInBand src/modules/subscriptions/dto/asaas-webhook.dto.spec.ts` — 4 testes aprovados, inclusive regressão do `ValidationPipe` global.
- `npm test -- --runInBand src/modules/subscriptions/subscriptions.service.spec.ts` — 25 testes aprovados.
- ESLint dos arquivos alterados — sem warnings.
- `npm run test:e2e` — falhou ao carregar `@nestjs/schedule` (ESM `export`); preexistente, fora desta task.

## Pendencias pos-task

- Publicar o backend de produção para a URL do webhook deixar de responder 400.
- No painel Asaas, reenviar os eventos penalizados após o deploy.

## Status final

done
