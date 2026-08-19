# Task 555 - Gráfico de evolução diária no perfil da criança

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

- nao se aplica; reutilizar `GET /patients/{patientId}/trails` e `GET /patients/{patientId}/progress`

## Modo de execucao

single-stack

## Slice vertical

- Slice 007 - Gestao de pacientes do profissional
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- linguagem visual atual do perfil do paciente + grafico diario introduzido na Task 554

### Fonte primaria visual

- `front-end/src/pages/Main/Patients/PatientProfile/`
- componente compartilhado da Task 554
- `design-system/front/Design_System_Evolente_Desktop.md`

### Lacunas

- sem print dedicado; o bloco deve parecer um card do perfil, nao uma copia do dashboard

## Objetivo

Incluir no perfil web da crianca (`/pacientes/:patientId`) o grafico de evolucao diaria individual (ultimos 7 dias: planejado, concluido e adesao), reusando o builder e o componente da Task 554.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-554.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI perfil | `front-end/src/pages/Main/Patients/PatientProfile/` | inserir bloco diario | sim |
| Estilo | `front-end/src/pages/Main/Patients/styles.module.css` | card alinhado ao perfil | sim |
| Dados | `front-end/src/services/trails/trailService.ts` | trails + progress do paciente | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | heading e estados vazios | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar ao perfil do paciente e ao componente ja extraido; nao reabrir dashboard nem backend

## Criterios de conclusao

- [x] perfil da crianca exibe grafico diario individual dos ultimos 7 dias
- [x] estados de loading, vazio e erro cobertos
- [x] reusa builder/componente da Task 554
- [x] testes do perfil atualizados

## Dependencias

- Task 554 - grafico diario compartilhado no dashboard

## Fora de escopo

- dashboard agregado
- novos endpoints
- mobile
- score, tempo, tentativas ou qualidade de jogo

## Resultado da execucao

- perfil da criança passou a exibir o gráfico diário individual abaixo do hero
- loading, erro e vazio cobertos no painel local, reusando o componente da Task 554

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/007-gestao-pacientes-profissional.md`, `.agents/state/handoffs/TASK-554.md`

### Sob demanda

- `front-end/src/pages/Main/Patients/PatientProfile/`
- `front-end/src/services/trails/trailService.ts`
- `front-end/docs/ai/ACCESSIBILITY.md`

### Contexto evitado

- backend, mobile, openapi, redesign do dashboard

## Handoff

- `.agents/state/handoffs/TASK-555.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/PatientProfile/DailyEvolutionPanel.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`
- `tasks/change-requests/555-grafico-evolucao-diaria-perfil-paciente.md`
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-555.md`

## Validacoes executadas

- `cd front-end && npx vitest run --pool=threads --maxWorkers=1 src/pages/Main/Patients/PatientProfile/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Patients/PatientProfile/index.tsx src/pages/Main/Patients/PatientProfile/DailyEvolutionPanel.tsx src/pages/Main/Patients/PatientProfile/index.test.tsx` - ok

## Acessibilidade aplicada

- heading `h2` do card, gráfico com `role="img"` e `aria-label` com o nome da criança
- loading com `role="status"` e erro com `role="alert"`
- estado vazio em texto

## Pendencias pos-task

- nenhuma

## Status final

done
