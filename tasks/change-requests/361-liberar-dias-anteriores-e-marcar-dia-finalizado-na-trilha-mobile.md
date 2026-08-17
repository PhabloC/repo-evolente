# Task 361 - Liberar dias anteriores e marcar dia finalizado na trilha mobile

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

ajuste funcional solicitado pelo usuário

### Fonte primaria visual

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`

## Objetivo

Na tela da trilha, manter liberados os dias anteriores e o dia atual, bloquear apenas dias futuros e marcar o dia como finalizado quando todas as atividades dele forem concluídas.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-293.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Regra de desbloqueio semanal | `mobile/src/features/trail/screens/TrailTodayScreen.tsx` | ajustar expansão, bloqueio e rótulos por dia | sim |
| Lógica reutilizável/testável | `mobile/src/features/trail/types/trail.ts`, `mobile/src/features/trail/utils/` | extrair o cálculo de estado de cada dia para utilitário | sim |
| Padrões locais | `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md` | manter fronteiras e registrar validações | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à regra local da tela de trilha e a um utilitário testado, sem reabrir contrato, backend ou execução da atividade

## Criterios de conclusao

- [x] dias anteriores ao atual ficam liberados mesmo se houver pendência
- [x] o dia atual continua liberado
- [x] apenas dias futuros ficam bloqueados
- [x] dia 100% concluído aparece como finalizado
- [x] teste focado da nova regra passa
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 020 - done
- Task 293 - done

## Resultado da execucao

- a tela de atividades da trilha passou a liberar qualquer dia da semana até hoje, incluindo dias anteriores pendentes
- dias futuros continuam bloqueados
- dias com todas as atividades concluídas agora exibem o status "Finalizado"
- a regra de disponibilidade por dia foi extraída para um utilitário testado

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-293.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/trail/utils/computeTrailWeekdayState.ts`

## Handoff

- `.agents/state/handoffs/TASK-361.md`

## Arquivos alterados

- `tasks/change-requests/361-liberar-dias-anteriores-e-marcar-dia-finalizado-na-trilha-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-361.md`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/utils/computeTrailWeekdayState.ts`
- `mobile/src/features/trail/utils/computeTrailWeekdayState.test.ts`

## Validacoes executadas

- `cd mobile && npx jest src/features/trail/utils/computeTrailWeekdayState.test.ts` - ok (`1` suite, `5` testes)
- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo em `WordSearchGameRenderer`, `EditChildProfileScreen`, `EditGuardianProfileScreen`, `HomeHeader`, `AppBackgroundBubbles` e `Screen`
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` - ok (`27` suites, `95` testes)

## Pendencias pos-task

- `npm run lint` do mobile segue com débitos preexistentes fora do escopo desta mudança
- `npm run typecheck` do mobile segue com débitos preexistentes fora do escopo desta mudança

## Status final

done
