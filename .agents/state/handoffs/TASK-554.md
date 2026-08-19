# Handoff - Task 554

- task: `554`
- título: Gráfico de evolução diária no dashboard profissional
- slice: `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- status final: done

## Decisões preservadas

- sem novos endpoints; série diária deriva de trails + progress já carregados no summary
- últimos 7 dias locais: planejadas, concluídas e adesão (%), sem pontuação
- adesão só existe quando há itens planejados no dia; excesso de conclusões caps em 100%
- gráfico semanal de 6 semanas permanece
- builder em `services/evolution/` e componente em `components/DailyEvolutionChart` para a Task 555

## Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 554, slice 019, handoff 439

## Contexto sob demanda carregado

- ShellHome, dashboard summary/types, ACCESSIBILITY, COMPONENT_REUSE

## Arquivos alterados

- `front-end/src/types/evolution.ts`
- `front-end/src/types/dashboard.ts`
- `front-end/src/services/evolution/buildDailyEvolutionSeries.ts`
- `front-end/src/services/evolution/buildDailyEvolutionSeries.test.ts`
- `front-end/src/components/DailyEvolutionChart/**`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/hooks/useDashboardSummary.test.ts`

## Validações executadas

- vitest focado (builder, ShellHome, useDashboardSummary) ok
- eslint do escopo ok

## Pendências

- Task 555: reusar o gráfico no perfil da criança

## Próxima ação sugerida

- executar Task 555

## Próximo contexto recomendado

- `front-end/src/pages/Main/Patients/PatientProfile/`
- componente e builder da Task 554

## Contexto que não deve ser carregado

- backend, mobile, openapi, dashboard master
