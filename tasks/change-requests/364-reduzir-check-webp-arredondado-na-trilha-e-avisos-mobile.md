# Task 364 - Reduzir check.webp arredondado na trilha e avisos mobile

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

Diminuir o `check.webp` arredondado para não ficar encostando nas bordas na trilha e na página de avisos.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-363.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ajuste fino da imagem | `mobile/src/shared/components/IconPill/index.tsx` | adicionar inset opcional só para imagens que precisem de respiro | sim |
| Check da trilha | `mobile/src/features/trail/screens/TrailTodayScreen.tsx` | reduzir o asset arredondado do dia finalizado | sim |
| Check dos avisos | `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx` | reduzir o asset arredondado do estado lido | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao tamanho interno do `check.webp`, preservando layout, regra funcional e demais imagens

## Criterios de conclusao

- [x] `check.webp` da trilha fica menor dentro da pastilha
- [x] `check.webp` dos avisos fica menor dentro da pastilha
- [x] outras imagens da `IconPill` permanecem inalteradas
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 363 - done

## Resultado da execucao

- a `IconPill` ganhou um inset opcional para imagens
- o `check.webp` arredondado da trilha e dos avisos passou a renderizar com respiro interno, sem encostar nas bordas

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-363.md`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-364.md`

## Arquivos alterados

- `tasks/change-requests/364-reduzir-check-webp-arredondado-na-trilha-e-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-364.md`
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
