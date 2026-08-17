# Task 144 - Refinar card principal do perfil mobile por print

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

Deixar o card principal da tela de perfil mais proximo do print enviado, com avatar maior, hint de edicao e pills de status no mesmo bloco.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/144-refinar-card-principal-do-perfil-mobile-por-print.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-143.md`

## Contexto sob demanda

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`

## Dependencias

- Task 139

## Validacao esperada

- `npm run lint`
- `npm run typecheck`

## Resultado da execucao

- O card principal do perfil foi recomposto para aproximar o layout do print de referencia
- O bloco agora exibe hint visual de editar dados e status com icones dentro do mesmo card

## Handoff

- `.agents/state/handoffs/TASK-144.md`
