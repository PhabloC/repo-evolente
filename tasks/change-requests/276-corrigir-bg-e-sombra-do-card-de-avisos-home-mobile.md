# Task 276 - Corrigir bg e sombra do card de avisos home mobile

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

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

refino incremental solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`

## Objetivo

Fazer o `trilha.webp` aparecer com clareza no card "Avisos da trilha" e aumentar a sombra sem deixar pontas quadradas visíveis nas laterais inferiores.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-275.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Estrutura visual do card | `mobile/src/features/shell/components/HomeActionCard/index.tsx`, `styles.ts` | separar shadow da camada clipada e reforçar o background | sim |
| Uso do card na home | `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx` | aumentar a opacidade do fundo apenas no card de avisos | sim |
| Asset local | `mobile/assets/trilha.webp` | manter o mesmo background solicitado | sim |

## Orçamento de contexto

- baixo
- estrategia: corrigir apenas a composição do `HomeActionCard` e o uso do card de avisos

## Criterios de conclusao

- [x] `trilha.webp` ficou mais evidente no card de avisos
- [x] shadow do card foi aumentada
- [x] sombra deixou de compartilhar a mesma camada com `overflow: hidden`, reduzindo as pontas quadradas aparentes

## Dependencias

- Task 275 - done

## Resultado da execucao

- a sombra foi movida para um container externo sem clipping
- o card interno manteve borda, radius e `overflow: hidden`
- o background `trilha.webp` ficou maior, mais à esquerda, com `resizeMode="cover"` e opacidade maior

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-275.md`

### Sob demanda

- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/trilha.webp`

## Handoff

- `.agents/state/handoffs/TASK-276.md`

## Arquivos alterados

- `tasks/change-requests/276-corrigir-bg-e-sombra-do-card-de-avisos-home-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-276.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- validação visual dependente de execução do app

## Pendencias pos-task

- confirmar no app se a opacidade e o crop atual do `trilha.webp` estão no ponto desejado

## Status final

done
