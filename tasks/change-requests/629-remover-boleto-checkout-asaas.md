# Task 629 - Remover boleto do checkout Asaas

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end (React/Vite)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora do escopo; checkout permanece web)

## Contrato

- `contracts/openapi.yaml#/paths/~1subscriptions~1checkout`
- schemas `SubscriptionPaymentMethod` e `SubscriptionCheckoutRequest`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 039 — Gateway Asaas e ciclo de assinatura (`tasks/slices/039-gateway-asaas-assinatura.md`)

## Objetivo

Deixar cartão de crédito e PIX como os únicos meios disponíveis para iniciar uma nova assinatura Asaas. Cobranças de boleto já existentes continuam somente legíveis e gerenciáveis, sem criar novas cobranças desse tipo.

## Contexto mínimo

- esta task
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `backend/src/modules/subscriptions/providers/payment-provider.ts`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `front-end/src/pages/Auth/SubscriptionGate/`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Alterar integração cliente-servidor | `contracts/openapi.yaml` — paths/schemas de subscription | remover boleto do contrato de criação |
| Ajustar seleção web | `front-end/docs/ai/ACCESSIBILITY.md` e docs de UI aplicáveis | preservar semântica e foco da opção removida |
| Validar regras de negócio | `requirements/001-escopo-produto.md` seção de pagamento e `requirements/002-regras-de-negocio.md` seção 5 | atualizar decisão de meios aceitos |
| Testar provider | specs de subscriptions/Asaas relacionadas | cobrir rejeição de boleto e cartão/PIX |

## Orçamento de contexto

- médio
- estratégia: alterar apenas o fluxo de criação de checkout e sua apresentação; preservar a leitura de métodos históricos em admin/mobile.

## Dependências

- Tasks 419, 420, 422, 424, 425 e 628 — done

## Critérios de aceite

- [x] API/contrato aceitam apenas `credit_card` e `pix` ao iniciar checkout.
- [x] Provider Asaas não cria novas assinaturas/cobranças em boleto.
- [x] Gate web não oferece boleto.
- [x] Textos e documentação de produto refletem cartão e PIX como meios aceitos.
- [x] Registros históricos de boleto continuam exibíveis em telas administrativas, sem possibilidade de nova criação.
- [x] Testes relevantes passam.

## Fora de escopo

- Cancelar ou migrar assinaturas de boleto já existentes no Asaas.
- Alterar a experiência de gestão/consulta de assinaturas históricas no mobile.
- Mudanças em preços, periodicidade ou regras de reembolso.

## Resultado da execucao

- Criação de checkout passou a aceitar somente `credit_card` e `pix` no DTO, contrato e serviços web.
- Provider Asaas removeu a rota de criação de boleto; PIX continua sendo uma assinatura mensal com QR Code.
- O gate web e os textos de planos exibem somente Cartão e PIX.
- O tipo amplo de método mantém `boleto` apenas nos retornos de checkout, para permitir retomar e exibir cobranças históricas sem autorizar novas criações.

## Contexto utilizado

### Contexto mínimo lido

- Task 629, Slice 039, índice e handoff da Task 628.
- Provider, serviço e DTO de subscriptions; gate web.

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | alteração cliente-servidor | separar enum de criação do enum de retorno histórico |
| `requirements/001-escopo-produto.md` e `requirements/002-regras-de-negocio.md` | regra de meios aceitos | atualizar decisão de produto |
| `front-end/docs/ai/ACCESSIBILITY.md` | alteração no seletor web | preservar botões semânticos e ordem de foco |
| specs de Asaas/subscriptions e gate | validação | remover cenário de criação de boleto e validar fluxos restantes |

## Handoff

- `.agents/state/handoffs/TASK-629.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/subscriptions/{dto,providers,subscriptions.service.ts}` e specs relacionadas
- `front-end/src/{types,services,constants,pages/Auth/SubscriptionGate}`
- `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md` e `ASAAS-CHECKOUT-PAGAMENTO.md`
- `tasks/000-index.md` e `tasks/slices/039-gateway-asaas-assinatura.md`

## Validacoes executadas

- `npm run build` em `backend` — ok.
- `npm run build` em `front-end` — ok.
- `npx jest src/modules/subscriptions/subscriptions.service.spec.ts src/modules/subscriptions/providers/asaas-payment.provider.spec.ts --runInBand --forceExit` — 36 testes ok.
- `npx vitest run src/pages/Auth/SubscriptionGate/index.test.tsx` — 4 testes ok.
- `git diff --check` na raiz e nos worktrees de backend/front-end — ok.

## Pendencias pos-task

- Nenhuma. Cobranças de boleto pré-existentes não foram canceladas ou migradas.

## Status final

done
