# Task 133 - Expandir fundos SVG para preenchimento total nas telas mobile

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

prints de telas + assets locais

### Fonte primaria visual

- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/assets/svg/fundo_trilha_livro.svg`
- `mobile/assets/svg/fundo_perfil.svg`
- `mobile/assets/svg/fundo_balao_fala.svg`

## Restricao explicita do usuario

- Ajustar todas as imagens para ocupar largura e altura totais dos cards hero

## Objetivo

Fazer todos os fundos SVG dos heroes mobile preencherem integralmente o card, sem margem interna nem encaixe parcial.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/133-expandir-fundos-svg-para-preenchimento-total-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-132.md`

## Contexto sob demanda

- `mobile/assets/svg/fundo_trilha_livro.svg`
- `mobile/assets/svg/fundo_perfil.svg`
- `mobile/assets/svg/fundo_balao_fala.svg`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Orcamento de contexto

- ~9 fontes
- estrategia de reducao: limitar a mudanca aos assets SVG e ao modo de encaixe dos `SvgUri`

## Criterios de aceite

- Todos os heroes com SVG ocupam 100% da largura e 100% da altura do card
- Nao resta margem interna criada pelo canvas antigo nem por encaixe proporcional
- Copy e comportamento permanecem inalterados

## Fora de escopo

- Reposicionar texto, CTA ou navegacao
- Alterar cores, copy ou logica das telas

## Dependencias

- Task 129
- Task 131
- Task 132

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Os SVGs de trilha, perfil e avisos passaram a usar o canvas completo em `1200x720`, sem inset interno herdado do desenho original
- Os `SvgUri` dos heroes passaram a renderizar com `preserveAspectRatio="none"` para preencher integralmente o card
- O fundo da home com estrelinha foi alinhado ao mesmo modo de preenchimento total para consistencia

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 022 e handoff `TASK-132`
- Contexto sob demanda carregado: assets SVG e componentes/telas que renderizam esses fundos

## Handoff

- `.agents/state/handoffs/TASK-133.md`

## Arquivos alterados

- `mobile/assets/svg/fundo_trilha_livro.svg`
- `mobile/assets/svg/fundo_perfil.svg`
- `mobile/assets/svg/fundo_balao_fala.svg`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `tasks/change-requests/133-expandir-fundos-svg-para-preenchimento-total-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-133.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar visual em dispositivo fisico/Expo Go para confirmar que o stretch do SVG esta coerente em telas menores

## Status final

done
