# Task 129 - Aplicar fundo estrelinha no hero da home do responsavel mobile

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

- nao se aplica (ajuste visual local no hero da home)

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

### Telas e estados que a referencia governa

- Hero laranja da home do responsavel com imagem decorativa aplicada no fundo, preservando copy e CTA atuais

### Lacunas da referencia

- O print nao define comportamento tecnico do asset SVG no Expo; manter implementacao pontual sem mexer em navegacao, queries ou tokens

## Restricao explicita do usuario

- Colocar a imagem `mobile/assets/svg/fundo_estrelinha.svg` no background do card hero mostrado na home do responsavel

## Objetivo

Substituir as formas decorativas em `View` do hero da home pelo asset `mobile/assets/svg/fundo_estrelinha.svg`, mantendo o conteudo sobreposto e a composicao visual da home.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/129-aplicar-fundo-estrelinha-hero-home-responsavel-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-128.md`

## Contexto sob demanda

- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Orcamento de contexto

- ~9 fontes
- estrategia de reducao: limitar a mudanca ao componente `HomeHeroBanner`; sem tocar home screen alem da verificacao de uso

## Criterios de aceite

- O hero da home usa o asset `mobile/assets/svg/fundo_estrelinha.svg` como fundo decorativo
- Copy, CTA `Ver trilha`, acessibilidade e comportamento de toque permanecem inalterados
- Nenhuma mudanca em navegacao, tab bar, queries, services ou regras de negocio

## Fora de escopo

- Refinos adicionais de layout no hero
- Mudancas em Perfil, Avisos, Atividades ou outras telas
- Ajustes em Metro, contrato ou dependencias

## Dependencias

- Task 123 (home do responsavel fiel ao print)
- Task 128 (refino visual das telas do responsavel com a linguagem da home)

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- O `HomeHeroBanner` passou a renderizar `mobile/assets/svg/fundo_estrelinha.svg` via `SvgUri`, usando o URI do asset empacotado
- O texto e o CTA permaneceram sobrepostos em uma camada dedicada, preservando a interacao e a hierarquia do hero
- As antigas formas decorativas em `View` foram removidas para evitar conflito visual com o novo fundo

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, `tasks/slices/022-linguagem-visual-print-telas-mobile.md` e handoff `TASK-128`
- Contexto sob demanda carregado: asset `assets/svg/fundo_estrelinha.svg`, `CODE_STYLE.md`, `COMPONENT_REUSE.md`, `HomeHeroBanner` e `ResponsavelHomeScreen`
- Fontes evitadas: demais telas mobile, `requirements/`, `contracts/openapi.yaml`, stacks web/backend

## Handoff

- `.agents/state/handoffs/TASK-129.md`
- Decisoes preservadas: o SVG entra apenas como fundo decorativo do hero; a copy e o CTA continuam governados pelo componente atual
- Proximo contexto recomendado: `mobile/src/features/shell/components/HomeHeroBanner/` para qualquer novo refino localizado do banner

## Arquivos alterados

- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `tasks/change-requests/129-aplicar-fundo-estrelinha-hero-home-responsavel-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-129.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar visual em dispositivo fisico/Expo Go para conferir o enquadramento do SVG no hero

## Status final

done
