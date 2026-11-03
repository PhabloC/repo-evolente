# Handoff - Task 792

## Task

- identificador: 792
- título: Remover callback da assinatura PIX Asaas
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 039 - Gateway Asaas e ciclo de assinatura
- objetivo de negócio: checkout Asaas (cartão ou PIX) libera acesso após confirmação
- entrega verificável: `POST /subscriptions` PIX sem `callback`

## Decisões preservadas

- decisão: omitir `callback.successUrl` no PIX
- motivo: a conta Asaas de produção recusa `successUrl` sem site comercial cadastrado
- impacto: criação da assinatura PIX deixa de retornar 503 `ASAAS_PIX_SUBSCRIPTION_REJECTED`

- decisão: cartão mantém checkout hospedado com `callback`
- motivo: fora do escopo desta task
- impacto: o gate de cartão continua redirecionando para a sessão Asaas

- decisão: confirmação PIX permanece por webhook/`invoiceUrl`
- motivo: sem redirect automático do Asaas
- impacto: o usuário conclui na fatura hospedada e o acesso sobe pelo webhook

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, Task 792, Slice 039

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `asaas-payment.provider.ts` | payload PIX | remover `callback` |
| `asaas-payment.provider.spec.ts` | teste | asserção sem `callback` |
| `backend/docs/ai/AGENTS.md` | stack back | regras locais |
| Handoff Task 702 | histórico PIX | fatura hospedada sem autoRedirect |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end / mobile / OpenAPI | contrato e UI inalterados |
| requirements | regra de negócio já coberta no slice |

## Resultado por stack

- backend: PIX mensal cria assinatura sem `callback`; cartão inalterado

## Arquivos alterados

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts`
- task 792, slice 039, índice, este handoff

## Validações executadas

- suíte do provider — 16 testes aprovados

## Pendências ou bloqueios

- validar PIX em produção após reload/deploy do backend
- cadastrar site comercial no Asaas se quiser restaurar `successUrl`

## Próxima ação sugerida

- tentar de novo o pagamento PIX no gate de assinatura

## Próximo contexto recomendado

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- painel Asaas (dados comerciais / site) se for restaurar callback

## Contexto que não deve ser carregado na próxima etapa

- fonte: front-end / mobile / jogos
- motivo: fora desta task
