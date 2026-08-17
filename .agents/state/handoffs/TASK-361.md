# Handoff - Task 361

## Task

- identificador: 361
- título: Liberar dias anteriores e marcar dia finalizado na trilha mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 008

## Decisões preservadas

- decisão: liberar todos os dias da semana até o dia atual na tela da trilha
- motivo: atender o fluxo pedido pelo usuário sem alterar API ou persistência
- impacto: somente dias futuros continuam bloqueados na UI

- decisão: marcar o dia como `Finalizado` quando todas as atividades dele forem concluídas
- motivo: tornar o estado diário explícito no cabeçalho do accordion
- impacto: o ícone verde existente passa a ter texto coerente com a conclusão total do dia

## Contexto utilizado

- `TrailTodayScreen.tsx`
- `computeTrailWeekdayState.ts` (+ teste)
- handoff `TASK-293`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/utils/computeTrailWeekdayState.ts`
- `mobile/src/features/trail/utils/computeTrailWeekdayState.test.ts`
- task/index/slice/handoff 361

## Validações executadas

- `cd mobile && npx jest src/features/trail/utils/computeTrailWeekdayState.test.ts` - ok (`1` suite, `5` testes)
- `cd mobile && npm run lint` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run typecheck` - falhou por débitos preexistentes fora do escopo
- `cd mobile && npm run test` - ok (`27` suites, `95` testes)

## Pendências ou bloqueios

- `lint` e `typecheck` do mobile continuam com débitos antigos fora da regra da trilha

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-361.md`
