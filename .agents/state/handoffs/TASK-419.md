# Handoff - Task 419

## Task

- identificador: 419
- título: Contrato OpenAPI Asaas e ciclo de assinatura
- tipo: shared
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 039 - Gateway Asaas e ciclo de assinatura
- objetivo de negócio: Substituir fake pelo Asaas com ciclo de vida completo
- entrega verificável: Contrato OpenAPI alinhado às regras confirmadas
- status do slice: todo (419 done; 420–423 pendentes)

## Decisões preservadas

- decisão: Ciclo canônico `PENDING → ACTIVE → OVERDUE → SUSPENDED → CANCELED` (payload lowercase)
- motivo: decisão humana explícita
- impacto: enum OpenAPI + requirements; implementação em 420/421

- decisão: `accessGranted=true` só em `active` e `overdue`; `suspended` inativa conta; `canceled` bloqueia na hora
- motivo: carência de 3 dias + regras de cancel/refund
- impacto: gate e webhooks

- decisão: Planos profissional 7900 / responsável 4900; mensal; BRL; meios credit_card, pix, boleto
- motivo: decisão comercial confirmada
- impacto: checkout e `SubscriptionPlan` no contrato

- decisão: `refused` permanece como caminho lateral de `pending`
- motivo: checkout recusado / fake confirm
- impacto: não faz parte do ciclo feliz

- decisão: `/subscriptions/confirm` e `/webhooks/fake` só com `PAYMENT_PROVIDER=fake`; Asaas usa `/webhooks/asaas`
- motivo: progressive cutover
- impacto: Task 420/421

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/419-contrato-openapi-asaas-assinatura.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | API | evoluir paths/schemas subscription |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end / mobile / backend src | fora do escopo da 419 |
| design-system | sem UI |

## Resultado por stack

- contrato OpenAPI: done
- backend código: não alterado
- front/mobile: não alterados

## Arquivos alterados

- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/change-requests/419-contrato-openapi-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-419.md`

## Validações executadas

- parse YAML OpenAPI (Node `yaml`) — ok

## Pendências ou bloqueios

- Task 420 implementar provider Asaas alinhado ao contrato
- enum backend ainda legado até 420/421

## Próxima ação sugerida

- Executar Task 420 (`tasks/change-requests/420-provider-asaas-checkout-mensal.md`)

## Próximo contexto recomendado

- handoff TASK-419
- task 420 + slice 039
- `backend/src/modules/subscriptions/`
- `contracts/openapi.yaml` paths subscription
- docs oficiais Asaas (clientes/cobranças)

## Contexto que não deve ser carregado na próxima etapa

- front-end UI / mobile / jogos — só na 422/423
- design-system — só na 422
