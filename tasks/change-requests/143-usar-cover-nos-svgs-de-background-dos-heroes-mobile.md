# Task 143 - Usar cover nos SVGs de background dos heroes mobile

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

Trocar o preenchimento dos SVGs de background dos heroes para comportamento equivalente a `cover`.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/143-usar-cover-nos-svgs-de-background-dos-heroes-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-142.md`

## Contexto sob demanda

- `mobile/src/shared/components/CachedHeroBackgroundSvg.tsx`

## Dependencias

- Task 138

## Validacao esperada

- `npm run lint`

## Resultado da execucao

- Os SVGs dos heroes passaram a usar `preserveAspectRatio="xMidYMid slice"`, equivalendo a `cover` no preenchimento do card

## Handoff

- `.agents/state/handoffs/TASK-143.md`
