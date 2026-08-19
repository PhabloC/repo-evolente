# Handoff - Task 562

## Task

- identificador: `562`
- título: Dashboard analítico web do responsável (gráficos e evolução)
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 052
- objetivo de negócio: painel analítico do responsável na web, com dados dos filhos da conta
- entrega verificável: `/dashboard` com KPIs, gráfico diário de 7 dias, evolução, áreas, hoje e relatórios disponibilizados
- status do slice: done

## Decisões preservadas

- Não chamar `getDashboardSummary()` (usa `listPatients` do profissional)
- Summary do responsável montado no cliente com `GET /guardians/me/children` + trails/progress + contents + reports
- Seletor de filho só nesta página; filho inválido cai no primeiro da lista
- 0 filhos: empty state; 1 filho: sem seletor; 2+: seletor
- CTA do header: Cadastrar filho
- Copy de família; sem carrossel “maior progresso”; sem CTAs de planejamento/biblioteca
- Relatórios: somente disponibilizados (`availableToGuardian`)
- Falha de contents/reports é parcial; falha de trails/progress bloqueia o painel analítico

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/change-requests/562-dashboard-analitico-responsavel-web.md`
- `tasks/slices/052-dashboard-analitico-responsavel-web.md`
- `front-end/docs/ai/ACCESSIBILITY.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| ShellHome | composição | KPIs + gráficos reutilizados |
| `getDashboardSummary` / `buildDashboardPanels` / `buildDailyEvolutionSeries` | dados | builders reusados |
| Guardian Dashboard | substituir conteúdo | página e testes |
| `reportService` / `listContents` | cards e áreas | APIs já liberadas ao responsável |

## Arquivos alterados

- `front-end/src/types/dashboard.ts`
- `front-end/src/services/dashboard/mapChildToPatientListItem.ts`
- `front-end/src/services/dashboard/getGuardianDashboardSummary.ts`
- `front-end/src/services/dashboard/getGuardianDashboardSummary.test.ts`
- `front-end/src/hooks/useGuardianDashboardSummary.ts`
- `front-end/src/pages/Main/Guardian/Dashboard/**`
- `front-end/src/pages/Main/Guardian/styles.module.css`
- `front-end/src/pages/Main/ShellHome/components/EvolutionLineChart.tsx` (`ariaLabel` opcional)
- task 562, slice 052, `tasks/000-index.md`, este handoff

## Validações executadas

- eslint nos arquivos tocados: ok
- vitest (4 testes do dashboard do responsável): ok
- `vite build`: ok

## Pendências

- Nenhuma desta task

## Próxima ação sugerida

- Nenhuma obrigatória. Não avançar outra task nesta execução.

## Próximo contexto recomendado

- Este handoff + `front-end/src/pages/Main/Guardian/Dashboard/` se houver ajuste visual pontual

## Contexto que não deve ser carregado

- Jogos, planejamento profissional, dashboard mobile, OpenAPI completo
