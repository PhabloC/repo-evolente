# Handoff - Task 294

## Task

- identificador: 294
- titulo: Integrar progresso real na tabela de pacientes web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 018 - Fidelidade visual dashboard e pacientes web
- objetivo de negocio: fazer a coluna de progresso da tabela de pacientes refletir dados reais sem reabrir backend
- entrega verificavel: cada paciente visivel na pagina passa a exibir percentual real quando houver trilha ativa com itens

## Decisoes preservadas

- a pagina busca progresso apenas dos pacientes visiveis na pagina atual para limitar fan-out
- o percentual usa a mesma regra de trilha de referencia do dashboard profissional: trilha ativa da semana atual ou, na falta dela, a ativa mais recente
- estados sem base de calculo permanecem honestos com labels `Sem trilha`, `Sem atividades` e `Indisponivel`

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/294-integrar-progresso-real-na-tabela-de-pacientes-web.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-067.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/AGENTS.md` | stack front envolvida | alinhar implementacao ao fluxo page -> services -> API |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | manter barra e texto compreensiveis sem depender so de cor |
| `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx}` | pagina de pacientes | integrar a coluna e cobrir comportamento |
| `front-end/src/services/trails/trailService.ts` | endpoints de trilha/progresso | buscar dados reais por paciente |
| `front-end/src/services/dashboard/getDashboardSummary.ts` | regra de negocio existente | reaproveitar a mesma regra de percentual |
| `front-end/src/services/trails/patientProgressSummary.{ts,test.ts}` | extracao de regra compartilhada | evitar divergencia entre dashboard e pacientes |
| `front-end/src/utils/mapWithConcurrency.ts` | fan-out controlado | limitar concorrencia das buscas por paciente |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | contrato nao precisou mudar |
| `backend/` | endpoints existentes ja eram suficientes |
| `design-system/front/` | sem alteracao visual estrutural |

## Resultado por stack

- front-end: coluna `Progresso` da tabela de pacientes integrada a trilhas e conclusoes reais, com estados honestos para ausencia de base de calculo
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/services/trails/patientProgressSummary.ts`
- `front-end/src/services/trails/patientProgressSummary.test.ts`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `tasks/change-requests/294-integrar-progresso-real-na-tabela-de-pacientes-web.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx src/services/trails/patientProgressSummary.test.ts`: ok
- `cd front-end && npm run lint`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido de refinamento visual dos estados da coluna ou necessidade de evitar refetch ao paginar

## Proximo contexto recomendado

- `tasks/change-requests/294-integrar-progresso-real-na-tabela-de-pacientes-web.md`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/services/trails/patientProgressSummary.ts`
