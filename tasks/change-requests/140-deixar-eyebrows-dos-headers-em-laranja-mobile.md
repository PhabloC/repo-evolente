# Task 140 - Deixar eyebrows dos headers em laranja no mobile

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

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Objetivo

Trocar para laranja o texto pequeno que aparece acima do titulo das paginas no header compartilhado.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/140-deixar-eyebrows-dos-headers-em-laranja-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-139.md`

## Contexto sob demanda

- `mobile/src/shared/components/ScreenHeader/`

## Dependencias

- Task 139

## Validacao esperada

- `npm run lint`

## Resultado da execucao

- O `ScreenHeader` compartilhado passou a renderizar o eyebrow em laranja em todas as telas que usam esse header

## Handoff

- `.agents/state/handoffs/TASK-140.md`
