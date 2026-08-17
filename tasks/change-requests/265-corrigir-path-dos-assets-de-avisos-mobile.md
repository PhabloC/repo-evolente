# Task 265 - Corrigir path dos assets de avisos mobile

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

bugfix incremental sobre assets locais já aplicados

### Fonte primaria visual

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Objetivo

Corrigir o path relativo dos assets `bell.webp`, `bell-off.webp` e `check.webp` na tela de avisos para que o bundler resolva os arquivos corretamente.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-264.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Erro do bundler | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | corrigir `require(...)` dos assets locais | sim |
| Histórico recente | `.agents/state/handoffs/TASK-262.md`, `.agents/state/handoffs/TASK-264.md` | confirmar quais assets foram introduzidos na tela | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter qualidade e validação | sim |

## Orçamento de contexto

- baixo
- estrategia: corrigir apenas os caminhos relativos quebrados em `ResponsavelNotificationsScreen`

## Criterios de conclusao

- [x] `bell.webp`, `bell-off.webp` e `check.webp` resolvem corretamente a partir da tela de avisos
- [x] `eslint` e `typecheck` passam no escopo alterado

## Dependencias

- Task 262 - done
- Task 264 - done

## Resultado da execucao

- Os `require(...)` da tela de avisos passaram de `../../../assets/...` para `../../../../assets/...`
- O bundler volta a localizar os assets locais introduzidos nas tasks anteriores

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-264.md`

### Sob demanda

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `.agents/state/handoffs/TASK-262.md`
- `.agents/state/handoffs/TASK-264.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`

## Handoff

- `.agents/state/handoffs/TASK-265.md`

## Arquivos alterados

- `tasks/change-requests/265-corrigir-path-dos-assets-de-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-265.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/trail/screens/TrailTodayScreen.tsx` - ok
- `cd mobile && npm run typecheck` - ok

## Pendencias pos-task

- `npm run lint` global do mobile segue com débitos preexistentes fora do escopo

## Status final

done
