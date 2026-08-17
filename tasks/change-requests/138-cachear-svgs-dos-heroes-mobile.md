# Task 138 - Cachear SVGs dos heroes mobile

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

assets locais estaveis

### Fonte primaria visual

- `mobile/assets/svg/fundo_estrelinha.svg`
- `mobile/assets/svg/fundo_trilha_livro.svg`
- `mobile/assets/svg/fundo_perfil.svg`
- `mobile/assets/svg/fundo_balao_fala.svg`

## Restricao explicita do usuario

- Colocar cache nessas imagens de background dos cards porque elas nao vao mudar

## Objetivo

Pre-carregar e manter em memoria os SVGs dos heroes mobile para evitar atraso visual quando o usuario troca de pagina.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/138-cachear-svgs-dos-heroes-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-137.md`

## Contexto sob demanda

- `mobile/src/app/AppGate.tsx`
- `mobile/src/shared/assets/`
- `mobile/src/shared/components/`
- heroes em `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- telas shell/trail com hero SVG

## Orcamento de contexto

- ~9 fontes
- estrategia de reducao: limitar a mudanca ao preload dos SVGs e ao renderer compartilhado dos heroes

## Criterios de aceite

- Os SVGs dos heroes sao pre-carregados durante o bootstrap do app
- As telas reutilizam o XML em memoria ao trocar de pagina
- Fallback para `SvgUri` permanece disponivel se o preload falhar

## Fora de escopo

- Alterar copy, layout ou comportamento das telas
- Refatorar outros assets do app que nao sejam esses heroes

## Dependencias

- Task 129
- Task 132
- Task 137

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Foi criado um cache em memoria para os SVGs de hero e um preload no bootstrap do app
- Os heroes passaram a usar um renderer compartilhado que prioriza `SvgXml` com XML em memoria e mantem `SvgUri` como fallback
- A troca entre paginas deixa de depender de novo fetch/parsing do asset a cada mount

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 022 e handoff `TASK-137`
- Contexto sob demanda carregado: `AppGate`, cache compartilhado de SVG e telas dos heroes

## Handoff

- `.agents/state/handoffs/TASK-138.md`

## Arquivos alterados

- `mobile/src/app/AppGate.tsx`
- `mobile/src/shared/assets/heroBackgroundSvgCache.ts`
- `mobile/src/shared/components/CachedHeroBackgroundSvg.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `tasks/change-requests/138-cachear-svgs-dos-heroes-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-138.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok (11 suites, 22 testes)

## Pendencias pos-task

- Validar em dispositivo fisico/Expo Go a reducao perceptivel do atraso na troca de telas

## Status final

done
