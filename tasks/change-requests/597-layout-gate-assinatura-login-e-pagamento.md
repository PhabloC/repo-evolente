# Task 597 - Layout do gate de assinatura (login e pagamento)

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica.

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Melhorar o layout das duas etapas principais do gate `/assinatura`: (1) autenticar após cadastro e (2) escolher meio de pagamento (cartão/PIX/boleto), reduzindo ruído visual e hierarquia repetida.

## Origem da solicitacao

Pedido humano com prints das duas telas do gate (login pós-cadastro e seleção de pagamento).

## Referencia visual

- tipo: refinamento visual solicitado pelo usuário + tokens do auth existente
- fonte primaria: `front-end/src/pages/Auth/SubscriptionGate/` e `AuthLayout`
- lacunas: prints mostram hierarquia repetida (preço no subtítulo + box) e seletor de meios em 3 colunas apertadas no card

## Dependencias

- Tasks 422 / 425 / 558 — done

## Contexto mínimo

- esta task
- `front-end/src/pages/Auth/SubscriptionGate/`
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Tokens auth | `front-end/src/layout/AuthLayout/` | manter shell |

## Orçamento de contexto

- baixo
- estrategia: só CSS/JSX do gate; sem backend, mobile ou OpenAPI

## Criterios de aceite

- [x] Etapa de login pós-cadastro com hierarquia mais clara (sucesso, plano, formulário) sem texto redundante excessivo
- [x] Etapa de pagamento com seletor de meios mais legível no card estreito (lista vertical com ícone)
- [x] Preservar fluxos, copy de negócio Asaas e valores oficiais
- [x] Responsivo no card de auth

## Fora de escopo

- Backend / webhook Asaas
- Mudança de preços ou meios
- Mobile

## Resultado da execucao

- Banner de sucesso pós-cadastro mais curto.
- Resumo do plano em linha (nome + preço + meta Asaas).
- Login e pagamento agrupados em painel com lead curto.
- Meios de pagamento em lista vertical (ícone + label + hint), em vez de 3 colunas.

## Contexto utilizado

### Contexto mínimo lido

- task 597, slice 039, SubscriptionGate

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| AuthLayout props | shell | wide/compact sem mudança |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| backend / openapi / mobile | fora do escopo |

## Handoff

- `.agents/state/handoffs/TASK-597.md`

## Arquivos alterados

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/styles.module.css`
- `tasks/change-requests/597-layout-gate-assinatura-login-e-pagamento.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-597.md`

## Validacoes executadas

- validação: ReadLints no SubscriptionGate — sem erros

## Pendencias pos-task

- Conferência visual no browser nas duas etapas

## Status final

done
