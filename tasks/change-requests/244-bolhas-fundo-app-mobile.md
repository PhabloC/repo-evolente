# Task 244 - Bolhas decorativas no fundo do app mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

mobile

## Modo de execucao

single-stack

## Slice vertical

`tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Objetivo

Reproduzir no fundo do app mobile as bolhas/lava decorativas do sidebar web.

## Entrega verificavel

- Bolhas pink/orange animadas no fundo global do app
- Sem interceptar toques
- Telas com fundo sólido (ex. atividade branca) cobrem as bolhas

## Resultado da execucao

Componente `AppBackgroundBubbles` no `AppGate`, com shells/navigator transparentes para revelar o fundo.

## Contexto utilizado

- Sidebar web (`persistentLava` + CSS blobs)
- `AppGate`, `Screen`, shell navigators

## Handoff

`.agents/state/handoffs/TASK-244.md`

## Arquivos alterados

- `mobile/src/shared/components/AppBackgroundBubbles/index.tsx`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/shared/components/Screen/index.tsx`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/shell/navigators/styles.ts`

## Validacoes executadas

- `npm run typecheck` (mobile) — pass

## Pendencias pos-task

- Ajustar densidade/opacidade se o usuário achar forte ou fraca no device

## Status final

done
