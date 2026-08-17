# Task 111 - Aproximar fundo auth mobile da lava goo do sidebar

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

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Aproximar o fundo animado das telas auth mobile do efeito de lava goo usado no sidebar web, com massas que se fundem visualmente e movimento ascendente irregular.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/111-goo-lava-auth-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-110.md`
- `front-end/src/layout/Sidebar/styles.module.css`
- `front-end/src/layout/Sidebar/persistentLava.tsx`
- `mobile/src/features/auth/components/AuthAnimatedBackground.tsx`
- `mobile/src/features/auth/components/AuthAnimatedBackground.styles.ts`

## Orcamento de contexto

- 10 fontes
- estrategia de reducao: limitar a comparacao ao efeito do sidebar e refinar apenas o componente de background mobile

## Resultado da execucao

- `AuthAnimatedBackground` foi refeito em SVG com blobs elipticos animados, gradientes radiais e filtro goo (`FeGaussianBlur` + `FeColorMatrix`)
- O fundo passou a lembrar mais diretamente a lava do sidebar web, com massas subindo, se fundindo visualmente e retornando em ciclos assimetricos
- O ajuste permaneceu isolado ao background do auth mobile, sem alterar shell, navegacao, formulários ou comportamento de scroll

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md`, `.agents/state/handoffs/TASK-110.md`, `front-end/src/layout/Sidebar/styles.module.css`, `front-end/src/layout/Sidebar/persistentLava.tsx`, `mobile/src/features/auth/components/AuthAnimatedBackground.tsx` e `mobile/src/features/auth/components/AuthAnimatedBackground.styles.ts`
- Fontes evitadas por nao se aplicarem: `requirements/`, `contracts/openapi.yaml`, docs de backend e telas mobile fora do auth
- Reducao de escopo: comparacao visual limitada ao sidebar e implementacao restrita ao componente de background

## Handoff

- `.agents/state/handoffs/TASK-111.md`
- Decisoes preservadas: usar `react-native-svg` com filtro goo para aproximar a fusao visual do sidebar em vez de seguir apenas com `View` deformadas
- Proximo contexto recomendado: `mobile/src/features/auth/components/AuthAnimatedBackground.tsx` se houver ajuste fino de densidade, cores ou amplitudes

## Arquivos alterados

- `mobile/src/features/auth/components/AuthAnimatedBackground.tsx`
- `mobile/src/features/auth/components/AuthAnimatedBackground.styles.ts`
- `tasks/change-requests/111-goo-lava-auth-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-111.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
