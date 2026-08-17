# Task 497 - Igualar fundo do sidebar ao background da página

## Status

done/reverted

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Fazer o fundo do sidebar usar a mesma cor do background da página (shell), sem o véu de vidro que deixava o tom diferente.

## Criterios de aceite

- [x] sidebar com `background: var(--color-bg)` (igual à página)
- [x] véu de vidro do sidebar removido
- [x] indice/handoff atualizados

## Resultado da execucao

- `.sidebar` usa `var(--color-bg)`; `::after` de vidro desativado
- lava permanece como filho (ainda visível sobre o fundo)

## Arquivos alterados

- `front-end/src/layout/Sidebar/styles.module.css`
- `tasks/change-requests/497-igualar-fundo-sidebar-background-pagina.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-497.md`

## Status final

done/reverted
