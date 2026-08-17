# Task 131 - Remover folga do SVG no hero da home mobile

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

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas + asset local

### Fonte primaria visual

- `design-system/mobile/prints/home-responsavel-referencia.png`
- `mobile/assets/svg/fundo_estrelinha.svg`

## Restricao explicita do usuario

- Tirar a margem/folga em volta do SVG no hero da home do responsavel

## Objetivo

Fazer o fundo SVG do hero ocupar o card sem borda interna perceptivel.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/131-remover-folga-do-svg-no-hero-home-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-129.md`

## Contexto sob demanda

- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`

## Orcamento de contexto

- ~7 fontes
- estrategia de reducao: limitar a mudanca ao asset e ao componente do hero

## Criterios de aceite

- O fundo SVG encosta visualmente nos limites do card
- Nao resta margem interna criada pelo próprio asset
- Copy e CTA permanecem inalterados

## Fora de escopo

- Refino de copy, layout ou navegacao
- Alteracoes em outras telas

## Dependencias

- Task 129

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- O asset `fundo_estrelinha.svg` foi expandido para usar o canvas inteiro, removendo o inset interno do background
- O `SvgUri` passou a renderizar com `preserveAspectRatio="xMidYMid slice"` para cobrir o card sem letterboxing

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 022 e handoff `TASK-129`
- Contexto sob demanda carregado: asset SVG e componente `HomeHeroBanner`

## Handoff

- `.agents/state/handoffs/TASK-131.md`

## Arquivos alterados

- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `tasks/change-requests/131-remover-folga-do-svg-no-hero-home-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-131.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar visual em dispositivo fisico/Expo Go

## Status final

done
