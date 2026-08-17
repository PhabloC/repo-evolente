# Task 367 - Voltar check.webp para cover na trilha e avisos mobile

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

ajuste incremental solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Objetivo

Voltar o `check.webp` para `cover` na trilha e na página de avisos.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-366.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste do resizeMode | `mobile/src/features/trail/screens/TrailTodayScreen.tsx`, `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | restaurar `cover` apenas nos dois checks | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas o `imageResizeMode` do `check.webp`, preservando inset, borda arredondada e demais estados

## Criterios de conclusao

- [x] `check.webp` da trilha volta para `cover`
- [x] `check.webp` dos avisos volta para `cover`
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 366 - done

## Resultado da execucao

- o `check.webp` da trilha voltou a usar `cover`
- o `check.webp` da página de avisos voltou a usar `cover`

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-366.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-367.md`

## Arquivos alterados

- `tasks/change-requests/367-voltar-check-webp-para-cover-na-trilha-e-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-367.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npm run lint`
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Pendencias pos-task

- nenhuma

## Status final

done
