# Task 778 - Remover borda dos ícones nos cards de avisos

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

## Origem da solicitacao

Pedido do usuário: os ícones dos cards em Avisos estão com borda em volta.

## Objetivo

Remover a pastilha com sombra/borda dos ícones nos cards da tela de Avisos via `flatIconPill`.

## Escopo

- `flatIconPill` em Resumo rápido, empty state e Últimos avisos

## Slice vertical

- Slice 010 - `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Criterios de conclusao

- [x] Ícones sem anel/sombra de borda
- [x] Fundo colorido da pastilha permanece

## Resultado da execucao

- Todos os `HomeActionCard` da tela de Avisos passaram a usar `flatIconPill` (mesmo padrão da Task 624 no perfil).

## Handoff

- `.agents/state/handoffs/TASK-778.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `tasks/change-requests/778-remover-borda-icones-cards-avisos.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-778.md`

## Validacoes executadas

- eslint — passou

## Status final

done
