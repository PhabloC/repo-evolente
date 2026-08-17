# Handoff - Task 384

## Task

- identificador: 384
- título: Restaurar botões nativos da nav bar Android mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 022 - Linguagem visual do print aplicada as telas mobile

## Decisões preservadas

- o app não esconde mais a nav bar nativa do Android no runtime
- `app.json` foi ajustado para não pedir mais `hidden: true` ao plugin `expo-navigation-bar`
- a mudança do plugin pode exigir novo build nativo para refletir integralmente em aparelho Android

## Contexto utilizado

- `mobile/app.json`
- `mobile/src/app/providers/AppProviders.tsx`

## Arquivos alterados

- config do app, provider global, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npm run typecheck` — sem diagnósticos

## Pendências ou bloqueios

- validar em device Android após rebuild se o comportamento do plugin persistir

## Próximo contexto recomendado

- `mobile/app.json`
