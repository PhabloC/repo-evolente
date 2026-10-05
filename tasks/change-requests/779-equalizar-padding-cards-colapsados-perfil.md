# Task 779 - Equalizar padding vertical dos cards colapsados no perfil

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

Pedido do usuário: nos cards do perfil, a margem do topo parece diferente da do bottom.

## Objetivo

Equalizar o padding vertical do `HomeActionCard` no estado colapsado.

## Escopo

- `bodyCollapsed` com padding top e bottom iguais

## Slice vertical

- Slice 010 - `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Criterios de conclusao

- [x] Card colapsado com padding top = bottom
- [x] Estado expandido inalterado

## Resultado da execucao

- `bodyCollapsed` agora usa `paddingTop` e `paddingBottom` = `spacing.md` (antes só o bottom era reduzido, ficando menor que o top do clay).

## Handoff

- `.agents/state/handoffs/TASK-779.md`

## Arquivos alterados

- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `tasks/change-requests/779-equalizar-padding-cards-colapsados-perfil.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-779.md`

## Validacoes executadas

- eslint — passou

## Status final

done
