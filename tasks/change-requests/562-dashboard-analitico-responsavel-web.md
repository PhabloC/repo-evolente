# Task 562 - Dashboard analítico web do responsável (gráficos e evolução)

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /guardians/me/children`
- `GET /patients/{patientId}/trails`
- `GET /patients/{patientId}/progress`
- paths de reports já liberados ao responsável (somente disponibilizados)

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `front-end/src/pages/Main/ShellHome/` (KPIs, `DailyEvolutionChart`, `EvolutionLineChart`, `ActivitiesByAreaChart`, `TodayActivitiesCard`, `WeeklyReportsCard`)
- `design-system/front/Design_System_Evolente_Desktop.md` (tokens da área interna)
- reuso de `DailyEvolutionChart` e `buildDailyEvolutionSeries` (Tasks 554/555)

### Regra de aderencia visual

- Composição semelhante ao dashboard profissional (faixa de indicadores + gráfico diário + grade de gráficos + atividades/relatórios)
- Copy de família, não “painel clínico” / “carteira”
- Sem print dedicado: não inventar visual novo; reutilizar cards e gráficos existentes
- Não copiar CTAs de planejamento, biblioteca ou cadência profissional
- CTA do header: Cadastrar filho

## Origem da solicitacao

Pedido humano: a página de dashboard do responsável precisa ficar parecida com a do profissional, com gráfico de evolução do filho cadastrado e outras informações e gráficos.

## Contexto de negocio

### Por que

Hoje o `/dashboard` do responsável só lista filhos e o status da trilha. O profissional já tem visão analítica (adesão, evolução diária, áreas, atividades de hoje).

### O que

Montar o mesmo tipo de painel para o responsável, com dados dos filhos da conta e foco no filho selecionado.

### Comportamento esperado

- 0 filhos: empty state atual
- 1 filho: painel analítico desse filho (sem seletor)
- 2+ filhos: seletor acessível no dashboard; gráficos, atividades de hoje e relatórios da semana usam o `childId` escolhido
- KPIs adaptados: filhos na conta, atividades de hoje, engajamento/adesão do filho (ou da conta, se documentado), relatórios disponibilizados
- Gráfico de evolução diária (últimos 7 dias: planejado vs concluído e adesão)
- Gráfico de evolução geral e atividades por área
- Card de atividades de hoje e card de relatórios disponibilizados
- Lista/atalho para o perfil do(s) filho(s) pode permanecer, sem substituir os gráficos

### Fora de escopo

- Novos endpoints
- Editar trilha na web
- Dashboard mobile
- Carrossel “maior progresso” da carteira profissional
- Relatórios pendentes de compartilhar (papel do profissional)

## Slice vertical

### Identificador do slice

Slice 052 - Dashboard analítico web do responsável

### Arquivo do slice

- `tasks/slices/052-dashboard-analitico-responsavel-web.md`

## Permissoes

- `responsavel` com `accessGranted`

## Casos de erro mapeados

- Loading / erro de lista de filhos
- Filho sem trilha
- Falha de trails/progress
- Relatórios vazios

## Decisoes humanas confirmadas

- Dashboard do responsável alinhado ao do profissional
- Gráfico de evolução do filho + demais gráficos/informações

## Premissas adotadas pela IA

- Reusar builders de `services/dashboard/` e `services/evolution/` em um summary do responsável (não chamar `getDashboardSummary` do profissional, que usa `listPatients`)
- Seletor de filho é só nesta página (não persiste como o seletor mobile)
- Isolamento já garantido pelas APIs de `patients/{id}` do responsável

## Criterios de aceite

- [x] Dashboard do responsável visualmente na mesma família do ShellHome (KPIs + gráficos)
- [x] Evolução diária de 7 dias do filho em foco
- [x] Demais gráficos/cards listados no comportamento esperado
- [x] Seletor com 2+ filhos; 1 filho sem seletor; 0 filhos empty state
- [x] Sem CTAs de planejamento/biblioteca
- [x] Lint, testes do dashboard do responsável e build ok
- [x] Acessibilidade: seletor, headings, `aria-label` nos gráficos, empty states

## Casos de borda

- Vários filhos
- Sem atividades nos últimos 7 dias
- Conta antiga com um filho já na trilha

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 052
- `front-end/docs/ai/ACCESSIBILITY.md`
- Tasks 554/559 (reuso vs o que não copiar)

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Layout | `front-end/src/pages/Main/ShellHome/**`, `styles.module.css` | composição | sim |
| Summary | `getDashboardSummary.ts`, `buildDashboardPanels.ts`, `buildDailyEvolutionSeries` | adaptar para filhos | sim |
| Página atual | `front-end/src/pages/Main/Guardian/Dashboard/**` | substituir conteúdo | sim |
| Relatórios | service de reports do responsável | card semanal | sim |
| DS | `design-system/front/Design_System_Evolente_Desktop.md` | tokens | sim |

## Orçamento de contexto

- medio
- estrategia de reducao: não abrir jogos, planejamento profissional, mobile nem OpenAPI completo

## Dependencias

- Task 559 (shell do responsável)
- Task 554 (gráfico diário extraído)
- Task 560 (filhos cadastrados na conta)

## Resultado da execucao

`/dashboard` do responsável passou a montar um painel analítico no cliente (filhos da conta + trilha/progresso/relatórios/conteúdos já existentes), reusando os gráficos do ShellHome. CTA do header permanece “Cadastrar filho”. Sem novos endpoints e sem carrossel de maior progresso.

Acessibilidade aplicada: `label` no seletor; `h1` da página + `h2` nos painéis + `h3` nos cards de filho; `role="status"`/`role="alert"`; `aria-label` no gráfico diário e na evolução geral; empty states em texto.

## Contexto utilizado

- Contexto mínimo: AGENTS.md, GUIDE.md, context-map, tasks/000-index.md, esta task, Slice 052, ACCESSIBILITY.md
- Sob demanda: ShellHome (layout/componentes), getDashboardSummary/buildDashboardPanels/buildDailyEvolutionSeries, Guardian Dashboard atual, reportService, tokens via reuso do CSS do ShellHome

## Handoff

`.agents/state/handoffs/TASK-562.md`

## Arquivos alterados

- `front-end/src/types/dashboard.ts`
- `front-end/src/services/dashboard/mapChildToPatientListItem.ts`
- `front-end/src/services/dashboard/getGuardianDashboardSummary.ts`
- `front-end/src/services/dashboard/getGuardianDashboardSummary.test.ts`
- `front-end/src/hooks/useGuardianDashboardSummary.ts`
- `front-end/src/pages/Main/Guardian/Dashboard/index.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/index.test.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/GuardianDashboardPanels.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/GuardianChildrenGrid.tsx`
- `front-end/src/pages/Main/Guardian/styles.module.css`
- `front-end/src/pages/Main/ShellHome/components/EvolutionLineChart.tsx`
- `tasks/change-requests/562-dashboard-analitico-responsavel-web.md`
- `tasks/slices/052-dashboard-analitico-responsavel-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-562.md`

## Validacoes executadas

- eslint nos arquivos tocados: ok
- vitest: `getGuardianDashboardSummary.test.ts` + `Guardian/Dashboard/index.test.tsx` — 4 testes ok
- `vite build`: ok
- `tsc --noEmit` do front-end falha em `tsconfig.json` (`ignoreDeprecations: "6.0"`) — pré-existente, fora desta task

## Pendencias pos-task

- Nenhuma desta task. Dashboard mobile permanece fora de escopo.

## Status final

done
