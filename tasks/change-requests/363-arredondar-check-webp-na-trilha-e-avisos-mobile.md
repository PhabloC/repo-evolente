# Task 363 - Arredondar check.webp na trilha e avisos mobile

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

Aplicar borda arredondada ao `check.webp` usado no dia finalizado da trilha e no estado lido da página de avisos.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-362.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Reuso controlado da pastilha | `mobile/src/shared/components/IconPill/index.tsx`, `styles.ts` | adicionar prop para arredondar imagens sem afetar todo o app | sim |
| Check da trilha | `mobile/src/features/trail/screens/TrailTodayScreen.tsx` | aplicar arredondamento só no dia finalizado | sim |
| Check dos avisos | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | aplicar arredondamento só no estado lido | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter organização e registrar validações | sim |

## Orçamento de contexto

- baixo
- estrategia: estender `IconPill` com uma prop opcional e consumir apenas nos dois checks pedidos

## Criterios de conclusao

- [x] `check.webp` da trilha fica com borda arredondada
- [x] `check.webp` da página de avisos fica com borda arredondada
- [x] outras imagens da `IconPill` permanecem inalteradas
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 362 - done

## Resultado da execucao

- a `IconPill` ganhou uma prop opcional para arredondar imagens localmente
- o `check.webp` do dia finalizado da trilha passou a usar borda arredondada
- o `check.webp` do estado lido na página de avisos também passou a usar borda arredondada

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-362.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/shared/components/IconPill/styles.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-363.md`

## Arquivos alterados

- `tasks/change-requests/363-arredondar-check-webp-na-trilha-e-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-363.md`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/shared/components/IconPill/styles.ts`
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
