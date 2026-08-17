# Task 368 - Voltar check.webp para contain na trilha e avisos mobile

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

Voltar o `check.webp` para `contain` na trilha e na página de avisos.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-367.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste do resizeMode | `mobile/src/features/trail/screens/TrailTodayScreen.tsx`, `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | restaurar `contain` apenas nos dois checks | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas o `imageResizeMode` do `check.webp`, preservando inset, borda arredondada e demais estados

## Criterios de conclusao

- [x] `check.webp` da trilha volta para `contain`
- [x] `check.webp` dos avisos volta para `contain`
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 367 - done

## Resultado da execucao

- o `check.webp` da trilha voltou a usar `contain`
- o `check.webp` da página de avisos voltou a usar `contain`

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-367.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-368.md`

## Arquivos alterados

- `tasks/change-requests/368-voltar-check-webp-para-contain-na-trilha-e-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-368.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npm run lint` — falhou por erros preexistentes em `WordSearchGameRenderer`, `EditChildProfileScreen`, `EditGuardianProfileScreen`, `HomeHeader`, `AppBackgroundBubbles` e `Screen`
- `cd mobile && npm run typecheck` — falhou por erros preexistentes em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` — passou (`27` suítes, `95` testes)

## Pendencias pos-task

- erros preexistentes de lint e typecheck no app mobile seguem fora do escopo desta task

## Status final

done
