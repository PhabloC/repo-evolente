# Task 142 - Corrigir cache dos SVGs dos heroes no Android mobile

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

Corrigir o preload em cache dos backgrounds SVG dos heroes, evitando erro 404 ao ler arquivo local no Android.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/142-corrigir-cache-dos-svgs-dos-heroes-no-android-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-141.md`

## Contexto sob demanda

- `mobile/src/shared/assets/heroBackgroundSvgCache.ts`

## Dependencias

- Task 138

## Validacao esperada

- `npm run lint`
- `npm run typecheck`

## Resultado da execucao

- O preload deixou de usar `fetch(file://...)` e passou a ler o SVG diretamente do filesystem local com `expo-file-system/legacy`
- Isso evita o 404 observado no Expo/Android ao trocar de pagina

## Handoff

- `.agents/state/handoffs/TASK-142.md`
