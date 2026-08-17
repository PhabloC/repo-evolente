# Handoff - Task 056

## Task

- identificador: 056
- título: Conectar dashboard profissional a dados reais
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 019 - Reproducao de shell dashboard por referencia externa
- objetivo de negócio: remover os mocks restantes do dashboard profissional e usar apenas dados reais
- entrega verificável: `/dashboard` do profissional consolidado a partir de pacientes, trilhas, progresso e relatórios

## Decisões preservadas

- decisão: compor o resumo do dashboard no front-end usando APIs existentes, sem criar endpoint dedicado nesta task
- motivo: o contrato atual já expõe pacientes, trilhas, progresso e relatórios suficientes para substituir os mocks principais
- impacto: a home passou a refletir o estado real do produto sem abrir backend novo

- decisão: remover a noção de agenda clínica futura e trocar por cadência recente
- motivo: o produto ainda não possui fonte real para próximos atendimentos no contrato atual
- impacto: o painel deixou de insinuar dados inexistentes e passou a exibir somente progresso e atualização reais

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/056-dashboard-profissional-dados-reais.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-055.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` (patients, trails, progress, reports) | API existente | validar quais dados reais poderiam sustentar a home |
| `front-end/docs/ai/ARCHITECTURE.md` | front-end | manter a composição em hook + service |
| `front-end/docs/ai/CODE_STYLE.md` | front-end | preservar tipagem e organização |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | manter headings, links e estados de loading/erro claros |
| `front-end/src/services/patients/patientService.ts` | services atuais | base para pacientes e vínculos |
| `front-end/src/services/trails/trailService.ts` | services atuais | base para trilhas e progresso |
| `front-end/src/services/reports/reportService.ts` | services atuais | base para relatórios reais |
| `front-end/src/pages/Main/ShellHome/index.tsx` | implementação atual | ligar a home ao summary real |
| `front-end/src/pages/Main/ShellHome/index.test.tsx` | validação focada | isolar a tela com hook mockado |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `backend/` | sem alteração de contrato ou endpoint |
| `mobile/` | stack fora do escopo |
| outras telas autenticadas | refino restrito à home do profissional |

## Resultado por stack

- front-end: dashboard profissional conectado a dados reais agregados das APIs existentes; painéis sem fonte real foram ajustados
- backend: sem alterações
- mobile: sem alterações

## Arquivos alterados

- `front-end/src/types/dashboard.ts`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.ts`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `tasks/change-requests/056-dashboard-profissional-dados-reais.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`

## Validações executadas

- `cd front-end && npm run lint`: ok
- `cd front-end && npm run build`: ok
- `cd front-end && npm run test -- ShellHome`: ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- abrir task nova apenas se quiser um endpoint dedicado de dashboard profissional para reduzir a composição N+1 do front-end

## Próximo contexto recomendado

- `tasks/change-requests/056-dashboard-profissional-dados-reais.md`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/pages/Main/ShellHome/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- `design-system/mobile/`
- motivo: sem relação com a home web do profissional
