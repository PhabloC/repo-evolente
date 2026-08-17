# Task 145 - Corrigir overflow da pill de assinatura no perfil mobile

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

Corrigir o vazamento horizontal da pill "Assinatura ativa" no card principal do perfil.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/145-corrigir-overflow-da-pill-de-assinatura-no-perfil-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-144.md`

## Contexto sob demanda

- `mobile/src/features/shell/screens/styles.ts`

## Dependencias

- Task 144

## Validacao esperada

- `npm run lint`

## Resultado da execucao

- As pills de status do perfil passaram a quebrar linha quando necessario, sem vazar pela direita

## Handoff

- `.agents/state/handoffs/TASK-145.md`
