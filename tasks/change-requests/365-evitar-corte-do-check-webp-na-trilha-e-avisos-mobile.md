# Task 365 - Evitar corte do check.webp na trilha e avisos mobile

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

- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Objetivo

Evitar que o `check.webp` arredondado corte nas bordas na trilha e na página de avisos.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-364.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Controle de crop da imagem | `mobile/src/shared/components/IconPill/index.tsx` | permitir `contain` só onde a imagem precisa preservar a borda | sim |
| Check da trilha | `mobile/src/features/trail/screens/TrailTodayScreen.tsx` | evitar corte do `check.webp` no dia finalizado | sim |
| Check dos avisos | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | evitar corte do `check.webp` no estado lido | sim |

## Orçamento de contexto

- baixo
- estrategia: ajustar apenas o `resizeMode` das imagens de check sem reabrir tamanhos, regra funcional ou layout geral

## Criterios de conclusao

- [x] `check.webp` da trilha não corta nas bordas
- [x] `check.webp` dos avisos não corta nas bordas
- [x] outras imagens da `IconPill` permanecem inalteradas
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 364 - done

## Resultado da execucao

- a `IconPill` ganhou `imageResizeMode` opcional
- o `check.webp` da trilha e dos avisos passou a usar `contain`, preservando a borda arredondada sem crop

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-364.md`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-365.md`

## Arquivos alterados

- `tasks/change-requests/365-evitar-corte-do-check-webp-na-trilha-e-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-365.md`
- `mobile/src/shared/components/IconPill/index.tsx`
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
