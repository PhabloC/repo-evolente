# Task 147 - Tentar ocultar barra de navegacao nativa no Android mobile

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

Tentar ocultar a barra de navegacao nativa do Android no app mobile usando a API oficial do Expo.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/147-tentar-ocultar-barra-de-navegacao-nativa-no-android-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-146.md`

## Contexto sob demanda

- `mobile/package.json`
- `mobile/src/app/providers/AppProviders.tsx`

## Dependencias

- Task 146

## Validacao esperada

- `npm run lint`
- `npm run typecheck`

## Resultado da execucao

- Foi adicionada a dependencia `expo-navigation-bar`
- O app passou a solicitar `hidden` para a navigation bar no Android durante o bootstrap
- Um listener reaplica a ocultacao quando o sistema voltar a exibir a barra

## Observacao

- A ocultacao depende de comportamento do Android/dispositivo e pode ser temporaria em alguns aparelhos ou no Expo Go

## Handoff

- `.agents/state/handoffs/TASK-147.md`
