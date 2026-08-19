# Task 554 - Gráfico de evolução diária no dashboard profissional

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

- nao se aplica; reutilizar `patients`, `trails` e `progress` já carregados pelo summary do dashboard, sem novos endpoints

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- linguagem visual atual do dashboard profissional e padrao recharts ja usado em ShellHome / PatientTrail

### Fonte primaria visual

- `front-end/src/pages/Main/ShellHome/`
- `design-system/front/Design_System_Evolente_Desktop.md` (tokens da area interna)

### Lacunas

- sem print dedicado do grafico diario; seguir cards/graficos existentes, sem gamificacao nem pontuacao

## Objetivo

Incluir no `/dashboard` do profissional um grafico de evolucao diaria da carteira (todas as criancas ativas), com planejado vs concluido e adesao dos ultimos 7 dias. Extrair o builder e o componente de grafico para reuso no perfil da crianca (Task 555).

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-439.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI dashboard | `front-end/src/pages/Main/ShellHome/` | inserir painel diario | sim |
| Summary | `front-end/src/services/dashboard/`, `front-end/src/types/dashboard.ts` | serie diaria no payload | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | heading, aria-label, nao depender so de cor | sim |
| Reuso | `front-end/docs/ai/COMPONENT_REUSE.md` | componente de dominio compartilhado | sim |

## Orçamento de contexto

- medio
- estrategia: limitar ao summary, tipos, componente compartilhado e ShellHome; nao abrir backend, mobile, openapi nem perfil do paciente

## Criterios de conclusao

- [x] serie diaria dos ultimos 7 dias agregada de todas as criancas ativas
- [x] grafico mostra atividades planejadas, concluidas e adesao (%)
- [x] grafico semanal de 6 semanas permanece
- [x] builder e componente reutilizaveis extraidos (sem pontuacao/gamificacao)
- [x] testes focados do builder e do ShellHome passam

## Dependencias

- Task 439 - done
- Task 056 - done

## Fora de escopo

- novos endpoints
- perfil individual da crianca (Task 555)
- mobile
- score, tempo, tentativas ou qualidade de jogo

## Resultado da execucao

- dashboard profissional ganhou painel de evolução diária da carteira (últimos 7 dias: planejadas, concluídas e adesão)
- o gráfico semanal de 6 semanas foi preservado
- builder e componente extraídos para reuso na Task 555

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`, `.agents/state/handoffs/TASK-439.md`

### Sob demanda

- `front-end/src/pages/Main/ShellHome/`
- `front-end/src/services/dashboard/`, `front-end/src/types/dashboard.ts`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`

### Contexto evitado

- backend, mobile, openapi, perfil do paciente

## Handoff

- `.agents/state/handoffs/TASK-554.md`

## Arquivos alterados

- `front-end/src/types/evolution.ts`
- `front-end/src/types/dashboard.ts`
- `front-end/src/services/evolution/buildDailyEvolutionSeries.ts`
- `front-end/src/services/evolution/buildDailyEvolutionSeries.test.ts`
- `front-end/src/components/DailyEvolutionChart/index.tsx`
- `front-end/src/components/DailyEvolutionChart/styles.module.css`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/hooks/useDashboardSummary.test.ts`
- `tasks/change-requests/554-grafico-evolucao-diaria-dashboard-profissional.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-554.md`

## Validacoes executadas

- `cd front-end && npx vitest run --pool=threads --maxWorkers=1 src/services/evolution/buildDailyEvolutionSeries.test.ts src/pages/Main/ShellHome/index.test.tsx src/hooks/useDashboardSummary.test.ts` - ok
- `cd front-end && npx eslint` no escopo da task - ok

## Acessibilidade aplicada

- painel com heading `h2` e `aria-label` de seção
- gráfico com `role="img"` e `aria-label` descritivo
- séries distinguíveis por traço contínuo vs tracejado, não só por cor
- estado vazio em texto

## Pendencias pos-task

- Task 555 - gráfico diário no perfil da criança

## Status final

done
