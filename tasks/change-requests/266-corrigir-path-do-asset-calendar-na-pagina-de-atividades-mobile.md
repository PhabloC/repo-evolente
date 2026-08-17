# Task 266 - Corrigir path do asset calendar na página de atividades mobile

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

- Slice 008 - Trilhas semanais e evolucao
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

bugfix incremental sobre asset local já aplicado

### Fonte primaria visual

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`

## Objetivo

Corrigir o path relativo de `calendar.webp` na tela de atividades para que o bundler resolva o asset corretamente.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-263.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Erro do bundler | `mobile/src/features/trail/screens/TrailTodayScreen.tsx` | corrigir `require(...)` do asset de calendário | sim |
| Histórico recente | `.agents/state/handoffs/TASK-263.md` | confirmar onde o asset foi introduzido | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter qualidade e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: corrigir apenas o caminho relativo quebrado em `TrailTodayScreen`

## Criterios de conclusao

- [x] `calendar.webp` resolve corretamente a partir da tela de atividades
- [x] `eslint` e `typecheck` passam no escopo alterado

## Dependencias

- Task 263 - done

## Resultado da execucao

- O `require(...)` da tela de atividades passou de `../../../assets/calendar.webp` para `../../../../assets/calendar.webp`
- O bundler volta a localizar o asset local de calendário aplicado no accordion e no estado vazio

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-263.md`

### Sob demanda

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `.agents/state/handoffs/TASK-263.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-266.md`

## Arquivos alterados

- `tasks/change-requests/266-corrigir-path-do-asset-calendar-na-pagina-de-atividades-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-266.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/trail/screens/TrailTodayScreen.tsx` - ok
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo

## Status final

done
