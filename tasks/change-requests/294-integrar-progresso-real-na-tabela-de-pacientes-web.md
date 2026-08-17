# Task 294 - Integrar progresso real na tabela de pacientes web

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

- nao se aplica; o contrato existente ja expõe `/patients/{patientId}/trails` e `/patients/{patientId}/progress`

## Modo de execucao

single-stack

## Slice vertical

- Slice 018 - Fidelidade visual dashboard e pacientes web
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre a pagina `/pacientes`

### Cobertura

- tornar funcional a coluna `Progresso` da tabela de pacientes

### Lacunas

- sem nova referencia visual em arquivo; a composicao atual da tabela permanece e o ajuste e funcional

## Objetivo

Substituir o estado fixo `Sem dado` da coluna de progresso por percentual real baseado na trilha ativa e nos registros de conclusao ja disponiveis para cada paciente.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-067.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/AGENTS.md` | confirmar padrao page -> services -> API | sim |
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | manter texto e barra compreensiveis sem depender so de cor | sim |
| Integracao front | `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}` | conectar a coluna e validar estados | sim |
| Regra de progresso | `front-end/src/services/trails/trailService.ts` | reaproveitar endpoints ja existentes | sim |
| Regra de progresso | `front-end/src/services/dashboard/getDashboardSummary.ts` | alinhar calculo do percentual com o dashboard profissional | sim |
| Tipos e concorrencia | `front-end/src/types/{patient.ts,trail.ts}` e `front-end/src/utils/mapWithConcurrency.ts` | tipar resumo por paciente e evitar fan-out descontrolado | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao modulo `Patients` e a um util local de resumo de progresso, sem reabrir backend ou outras paginas

## Criterios de conclusao

- [x] a coluna `Progresso` deixa de renderizar valor fixo
- [x] cada paciente exibe percentual real quando houver trilha ativa com itens
- [x] pacientes sem trilha ativa ou sem itens continuam com estado honesto
- [x] teste focado da pagina cobre pelo menos um caso com progresso real e um sem base de calculo

## Dependencias

- Task 067 - done
- Task 157 - done

## Resultado da execucao

- a pagina `/pacientes` passou a buscar trilhas e conclusoes reais apenas dos pacientes visiveis na pagina atual
- a coluna `Progresso` agora mostra percentual calculado com a mesma regra de trilha de referencia usada no dashboard profissional
- estados sem base de calculo permaneceram honestos com labels `Sem trilha`, `Sem atividades` e `Indisponivel`

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `.agents/state/handoffs/TASK-067.md`

### Sob demanda

- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx}`
- `front-end/src/services/trails/trailService.ts`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/services/trails/patientProgressSummary.{ts,test.ts}`
- `front-end/src/types/{patient.ts,trail.ts}`
- `front-end/src/utils/mapWithConcurrency.ts`

### Contexto evitado

- `contracts/openapi.yaml`, porque os endpoints necessarios ja estavam integrados no front e nao exigiram mudanca de contrato
- `backend/`, porque a coluna passou a funcionar apenas com os endpoints ja existentes
- `design-system/front/`, porque nao houve alteracao de composicao visual, apenas ativacao funcional da coluna

## Handoff

- `.agents/state/handoffs/TASK-294.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/services/trails/patientProgressSummary.ts`
- `front-end/src/services/trails/patientProgressSummary.test.ts`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `tasks/change-requests/294-integrar-progresso-real-na-tabela-de-pacientes-web.md`
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-294.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx src/services/trails/patientProgressSummary.test.ts` - ok
- `cd front-end && npm run lint` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
