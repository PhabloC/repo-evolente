# Task 362 - Usar check.webp no dia finalizado da trilha mobile

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
- `mobile/assets/check.webp`

## Objetivo

Usar o asset `check.webp` no ícone do cabeçalho do dia finalizado na trilha mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-361.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Ícone do dia concluído | `mobile/src/features/trail/screens/TrailTodayScreen.tsx` | trocar o ícone vetorial concluído pelo asset local | sim |
| Asset local | `mobile/assets/check.webp` | aplicar a imagem no estado finalizado | sim |
| Padrões locais | `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter organização e registrar validações | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao `IconPill` do cabeçalho do dia finalizado, sem reabrir a regra funcional de desbloqueio

## Criterios de conclusao

- [x] dia finalizado da trilha usa `check.webp`
- [x] dias pendentes e vazios mantêm seus assets/ícones atuais
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 361 - done

## Resultado da execucao

- o cabeçalho do dia 100% concluído na trilha mobile passou a usar `check.webp` no `IconPill`
- os estados de dia pendente e dia sem atividade foram preservados

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-361.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/assets/check.webp`

## Handoff

- `.agents/state/handoffs/TASK-362.md`

## Arquivos alterados

- `tasks/change-requests/362-usar-check-webp-no-dia-finalizado-da-trilha-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-362.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`

## Validacoes executadas

- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo em `WordSearchGameRenderer`, `EditChildProfileScreen`, `EditGuardianProfileScreen`, `HomeHeader`, `AppBackgroundBubbles` e `Screen`
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` - ok (`27` suites, `95` testes)

## Pendencias pos-task

- `npm run lint` do mobile segue com débitos preexistentes fora do escopo desta mudança
- `npm run typecheck` do mobile segue com débitos preexistentes fora do escopo desta mudança

## Status final

done
