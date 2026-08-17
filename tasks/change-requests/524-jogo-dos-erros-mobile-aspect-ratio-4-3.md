# Task 524 - Jogo dos erros mobile: aspect ratio 4/3

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

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/035-jogo-dos-erros.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- este arquivo

## Contexto sob demanda

- `mobile/src/features/games/components/SpotDifferenceGameRenderer/` (layout das imagens no runtime)
- referência de alinhamento: Task 516 (`aspect-ratio: 4 / 3` no front-end)

## Orçamento de contexto

- baixo — apenas styles/renderer do Spot Difference no mobile

## Objetivo

No runtime mobile do Jogo dos erros, as imagens usam container quadrado (`aspectRatio: 1`), o que aumenta demais a altura e corta o conteúdo das artes 4:3. Alinhar ao web: proporção 4/3 (altura menor, sem crop indevido).

## Criterios de aceite

- [x] `imageWrap` com `aspectRatio: 4/3` (não 1)
- [x] `Image` com `resizeMode` compatível com o preenchimento do painel
- [x] Hotspots continuam normalizados pelo layout do `Pressable`

## Resultado da execucao

- `imageWrap` passou de `aspectRatio: 1` para `4 / 3`, reduzindo a altura do painel e alinhando às artes
- `resizeMode="cover"` explícito no `Image` (mesmo comportamento do web `object-fit: cover`)
- Coordenadas de hotspot seguem o layout do `Pressable` via `onLayout` — sem mudança de lógica

## Contexto utilizado

- mínimo: backlog + slice 035
- sob demanda: `SpotDifferenceGameRenderer` (styles + index) e critério da Task 516

## Handoff

- `.agents/state/handoffs/TASK-524.md`

## Arquivos alterados

- `mobile/src/features/games/components/SpotDifferenceGameRenderer/styles.ts`
- `mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx`
- `tasks/change-requests/524-jogo-dos-erros-mobile-aspect-ratio-4-3.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-524.md`

## Validacoes executadas

- revisão estática do layout (proporção alinhada ao front-end Task 516)
- hotspots: `locationX/Y` normalizados pelo tamanho do `Pressable` — independente da mudança de aspect ratio

## Pendencias pos-task

- Conferir visualmente no app (Expo) com uma rodada aberta

## Status final

done
