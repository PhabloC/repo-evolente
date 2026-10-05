# Task 774 - Ocultar card Assinatura no perfil mobile

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

- nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- nao se aplica (somente ocultar render)

### Regra de aderencia visual

- card permanece no código; não é exibido no perfil

## Origem da solicitacao

Pedido do usuário: ocultar o card Assinatura no perfil (não excluir), no contexto de revisão das lojas.

## Objetivo

Ocultar o `SubscriptionManagementCard` no perfil do responsável sem remover o componente do projeto.

## Escopo

- Flag/condição no `ResponsavelProfileScreen` para não renderizar o card Assinatura
- Manter `SubscriptionManagementCard` e import no código

## Fora de escopo

- Excluir o componente
- Alterar backend/web
- Remover pill de assinatura do card do responsável (só o card Assinatura)

## Entradas

- pedido explícito do usuário
- Task 773
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Slice vertical

### Identificador do slice

Slice 010 - App do responsavel: home, perfil e notificacoes

### Arquivo do slice

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

### Objetivo de negocio

Reduzir exposição de gestão de assinatura no app mobile para revisão das lojas.

### Entrega verificavel do slice

Card Assinatura não aparece no perfil; código do componente permanece.

### Fora do slice

- remoção definitiva do fluxo de cancelamento/reembolso mobile

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Perfil | `ResponsavelProfileScreen.tsx` | ocultar render | sim |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 1
- Risco de contexto excessivo: baixo
- Estratégia: só a tela de perfil

## Dependencias

- Task 773

## Criterios de conclusao

- [x] Card Assinatura não aparece no perfil
- [x] Componente `SubscriptionManagementCard` permanece no repositório
- [x] Reativar é só mudar a flag/condição

## Instrucoes de implementacao

- Constante `SHOW_SUBSCRIPTION_CARD = false` no perfil
- Render condicional do `SubscriptionManagementCard`
- Não deletar o arquivo do componente

## Validacao esperada

- eslint na tela do perfil

## Entregaveis esperados

- perfil sem card Assinatura visível
- task, índice, slice e handoff

## Resultado da execucao

- Flag `SHOW_SUBSCRIPTION_CARD = false` em `ResponsavelProfileScreen`; card não renderiza.
- Componente `SubscriptionManagementCard` e import preservados.

## Contexto utilizado

- Task 774, Slice 010, `ResponsavelProfileScreen.tsx`.

## Handoff

- `.agents/state/handoffs/TASK-774.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/774-ocultar-card-assinatura-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-774.md`

## Validacoes executadas

- `npx eslint src/features/shell/screens/ResponsavelProfileScreen.tsx` — passou.

## Pendencias pos-task

- Pill “Assinatura ativa/sem acesso” no card do responsável ainda aparece; ocultar se a loja exigir.
- Para reexibir o card: `SHOW_SUBSCRIPTION_CARD = true`.

## Status final

done
