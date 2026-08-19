# Handoff - Task 559

## Task

- identificador: `559`
- título: Área web do responsável: shell, dashboard, relatórios e configuração
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 050
- objetivo de negócio: área web do responsável e cadastro de filhos
- entrega verificável: login pago leva ao dashboard; navegação Dashboard / Filhos / Relatórios / Configuração
- status do slice: todo (falta Task 560)

## Decisões preservadas

- Responsável pago vai para `/dashboard`, não mais para `/baixar-app`
- Menu só com 4 destinos; Pacientes/Planejamentos/Biblioteca/Admin ficam fora
- Relatórios do responsável: somente disponibilizados, filtro por filho, download
- `/filhos/cadastrar` é placeholder até a Task 560
- `/baixar-app` permanece como CTA opcional no perfil

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- `tasks/change-requests/559-area-web-responsavel-shell-dashboard.md`
- `tasks/slices/050-area-web-responsavel-multiplos-filhos.md`
- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`
- `.agents/state/handoffs/TASK-558.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS desktop | shell | tokens/empty |
| rotas + `resolvePostAuthPath` | pós-login | destino |
| layout/navigation | menu | filtro por papel |
| Reports/Settings | reuso | responsável |
| OpenAPI children/reports | API | listagem |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| wizard de filho | Task 560 |
| mobile | Task 561 |
| biblioteca/jogos | fora de escopo |

## Resultado por stack

- front-end: shell do responsável no ar
- backend: não alterado
- mobile: não alterado

## Arquivos alterados

- rotas, navigation, resolvePostAuthPath
- `pages/Main/Guardian/**`
- dashboard/reports/settings/shell home
- GuardianAppGate e SubscriptionGate (copy/CTA)

## Validações executadas

- eslint: passou
- testes de navigation, pós-login, dashboard/filhos, shell profissional: passaram
- vite build: passou

## Pendências ou bloqueios

- implementar o wizard em `/filhos/cadastrar` (Task 560)

## Próxima ação sugerida

- executar Task 560

## Próximo contexto recomendado

- `tasks/change-requests/560-cadastro-filho-autenticado-web.md`
- `front-end/src/pages/Main/Guardian/ChildRegister/**`
- `front-end/src/pages/Auth/RegisterGuardian/schemas.ts` (anamnese reuso)
- contrato `POST /guardians/me/children`

## Contexto que não deve ser carregado na próxima etapa

- dashboard profissional
- mobile seletor de filho
- redesign do shell master/profissional
