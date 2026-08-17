# Handoff - Task 075

## Task

- identificador: 075
- titulo: Reduzir pressao no dashboard e higienizar sidebar
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 019 - Reproducao de shell dashboard por referencia externa
- objetivo de negocio: manter a home profissional responsiva e o shell compartilhado mais seguro para testes
- entrega verificavel: fan-out controlado no dashboard, loading inicial coerente e limpeza total do sidebar persistente

## Decisoes preservadas

- foi adotado limitador de concorrencia no cliente em vez de abrir endpoint novo fora do escopo desta task
- o lava persistente continua com reparenting para preservar a animacao; a mudanca ficou restrita a uma rotina explicita de teardown
- o visual aprovado do dashboard e do sidebar foi preservado

## Contexto efetivamente usado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/075-reduzir-pressao-no-dashboard-e-higienizar-sidebar.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-056.md`
- `.agents/state/handoffs/TASK-070.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Arquivos alterados

- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.test.ts`
- `front-end/src/layout/Sidebar/persistentLava.tsx`
- `front-end/src/layout/Sidebar/persistentLava.test.tsx`
- `front-end/src/utils/mapWithConcurrency.ts`
- `front-end/src/utils/mapWithConcurrency.test.ts`
- `tasks/change-requests/075-reduzir-pressao-no-dashboard-e-higienizar-sidebar.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- src/utils/mapWithConcurrency.test.ts src/hooks/useDashboardSummary.test.ts src/layout/Sidebar/persistentLava.test.tsx src/pages/Main/ShellHome/index.test.tsx`
- `cd front-end && npm run lint`
- `cd front-end && npm run build`

## Pendencias ou bloqueios

- nenhuma

## Proximo contexto recomendado

- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/layout/Sidebar/persistentLava.tsx`
- `contracts/openapi.yaml#/paths` apenas se futuramente for aberta task para endpoint agregado de dashboard
