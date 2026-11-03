# Handoff - Task 806

## Task

- identificador: 806
- título: Aceitar envelope real do webhook Asaas sem 400
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 039 - Gateway Asaas e ciclo de assinatura
- objetivo de negócio: checkout Asaas libera acesso após confirmação
- entrega verificável: webhook oficial do Asaas não retorna 400 por campos extras

## Decisões preservadas

- decisão: não validar o body do webhook pelo `ValidationPipe` global
- motivo: `forbidNonWhitelisted: true` rejeita `dateCreated` e `account` do envelope oficial
- impacto: Asaas penalizava a fila com 400; o parse local ignora extras e exige só `event`

- decisão: manter autenticação por `asaas-access-token` e 200 quando não houver assinatura local
- motivo: já era o contrato do ciclo; o bug era só a borda HTTP
- impacto: retries antigos (`PAYMENT_CREATED` de cobrança deletada) passam a ser ACK

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, Task 806, Slice 039

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `backend/src/main.ts` | 400 em produção | confirmar `forbidNonWhitelisted` |
| `asaas-webhook.dto.ts` | contrato HTTP | parse sem rejeitar extras |
| `subscriptions.controller.ts` | borda do webhook | receber body cru |
| `contracts/openapi.yaml` | schema do envelope | `additionalProperties: true` |
| `backend/docs/ai/SECURITY.md` | borda pública | manter DTO + class-validator |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end / mobile | sem UI |
| provider Asaas | ciclo de pagamento inalterado |
| requirements | regra já coberta no slice |

## Resultado por stack

- backend: webhook aceita o envelope oficial do Asaas e campos extras de topo

## Arquivos alterados

- `backend/src/modules/subscriptions/dto/asaas-webhook.dto.ts`
- `backend/src/modules/subscriptions/dto/asaas-webhook.dto.spec.ts`
- `backend/src/modules/subscriptions/subscriptions.controller.ts`
- `backend/test/app.e2e-spec.ts`
- `contracts/openapi.yaml`
- task 806, slice 039, índice, este handoff

## Validações executadas

- DTO spec — 4 testes aprovados
- subscriptions.service.spec — 25 testes aprovados
- ESLint dos arquivos alterados — limpo
- e2e completo — bloqueado por `@nestjs/schedule` ESM (preexistente)

## Pendências ou bloqueios

- deploy do backend de produção
- reenvio dos webhooks penalizados no painel Asaas

## Próxima ação sugerida

- publicar o backend e reenviar o evento `PAYMENT_CREATED` no Asaas

## Próximo contexto recomendado

- URL `https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas`
- painel Asaas (fila de webhooks penalizados)

## Contexto que não deve ser carregado na próxima etapa

- fonte: front-end / mobile / jogos
- motivo: fora desta task
