# Task 148 - Remover folga inferior da tabbar apos ocultar nav bar mobile

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

Remover o espaço em branco inferior deixado pela tab bar após a tentativa de ocultar a barra nativa do Android.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/148-remover-folga-inferior-da-tabbar-apos-ocultar-nav-bar-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-147.md`

## Contexto sob demanda

- `mobile/src/shared/components/ShellTabBar/index.tsx`

## Dependencias

- Task 147

## Validacao esperada

- `npm run lint`

## Resultado da execucao

- A `ShellTabBar` deixou de reservar `bottom inset` no Android, removendo a faixa em branco inferior quando a nav bar nativa está oculta

## Handoff

- `.agents/state/handoffs/TASK-148.md`
