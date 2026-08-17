# Task 056 - Conectar dashboard profissional a dados reais

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

- `contracts/openapi.yaml#/paths` patients
- `contracts/openapi.yaml#/paths` trails
- `contracts/openapi.yaml#/paths` reports

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Tipo

continuacao funcional da home operacional aprovada anteriormente

### Cobertura

- preservar a composicao atual da home do profissional
- substituir mocks por dados vindos das APIs reais ja existentes
- remover ou ajustar paineis cujo conteudo nao tenha fonte real hoje

### Lacunas

- nao existe endpoint dedicado de dashboard profissional no contrato
- decisao: compor o resumo no front-end com `patients`, `trails`, `progress` e `reports`, sem abrir backend novo nesta task

## Objetivo

Remover os mocks do `/dashboard` do profissional e usar dados reais das APIs existentes, mantendo apenas informacoes que possam ser derivadas honestamente do estado atual do produto.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-055.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API existente | `contracts/openapi.yaml` (paths de patients, trails, progress e reports) | validar quais dados reais existem | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | manter estrutura, tipagem e a11y | sim |
| Implementacao atual | `front-end/src/pages/Main/ShellHome/index.tsx`, `styles.module.css`, `index.test.tsx` | integrar os dados reais na home | sim |
| Services atuais | `front-end/src/services/patients/patientService.ts`, `trails/trailService.ts`, `reports/reportService.ts` | compor o dashboard a partir das APIs existentes | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao dashboard profissional, tipos/hook/service relacionados e teste focado

## Criterios de conclusao

- [x] dashboard profissional deixa de usar numeros e textos mockados
- [x] a home usa apenas dados reais derivados das APIs existentes
- [x] paineis sem fonte real sao removidos ou ajustados para refletir dados disponiveis
- [x] lint, build e teste focado aprovados

## Dependencias

- Task 055 - done

## Resultado da execucao

- `ShellHome` deixou de usar valores hardcoded e passou a consumir um summary real agregado no front-end
- o summary foi montado a partir de `patients`, `trails`, `progress` e `reports`, reutilizando services e contrato ja existentes
- o painel de agenda futura foi removido e substituido por cadencia recente, porque nao existe fonte real de proximos atendimentos no contrato atual

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-055.md`

### Sob demanda

- `contracts/openapi.yaml` (patients, trails, progress, reports)
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `front-end/src/services/patients/patientService.ts`
- `front-end/src/services/trails/trailService.ts`
- `front-end/src/services/reports/reportService.ts`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.ts`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`

### Contexto evitado

- backend por nao haver alteracao de endpoint
- mobile por stack fora do escopo
- outras paginas do shell por nao participarem desta integracao

## Handoff

- `.agents/state/handoffs/TASK-056.md`

## Arquivos alterados

- `front-end/src/types/dashboard.ts`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.ts`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `tasks/change-requests/056-dashboard-profissional-dados-reais.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-056.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
