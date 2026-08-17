# Task 366 - Aumentar respiro do check.webp na trilha e avisos mobile

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

Aumentar o respiro interno do `check.webp` para evitar que a borda direita pareça cortada na trilha e nos avisos.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-365.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste fino do asset | `mobile/src/features/trail/screens/TrailTodayScreen.tsx`, `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | aumentar apenas o inset do `check.webp` | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar só o inset do `check.webp`, sem reabrir `IconPill` nem os demais estados

## Criterios de conclusao

- [x] `check.webp` da trilha ganha mais respiro interno
- [x] `check.webp` dos avisos ganha mais respiro interno
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 365 - done

## Resultado da execucao

- o inset do `check.webp` passou de `6` para `8` na trilha e nos avisos
- o asset ganhou mais folga lateral dentro da pastilha

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-365.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-366.md`

## Arquivos alterados

- `tasks/change-requests/366-aumentar-respiro-do-check-webp-na-trilha-e-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-366.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo em `WordSearchGameRenderer`, `EditChildProfileScreen`, `EditGuardianProfileScreen`, `HomeHeader`, `AppBackgroundBubbles` e `Screen`
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` - ok (`27` suites, `95` testes)

## Pendencias pos-task

- `npm run lint` do mobile segue com débitos preexistentes fora do escopo desta mudança
- `npm run typecheck` do mobile segue com débitos preexistentes fora do escopo desta mudança

## Status final

done
