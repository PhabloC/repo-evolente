# Task 019 - UI de montagem de trilha semanal (profissional)

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

- `contracts/openapi.yaml#/paths` trails

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- Planejamentos/biblioteca DS.

## Contexto de negocio

### Por que

Profissional monta rotina.

### O que

No perfil, montar semana e ver progresso.

### Comportamento esperado

- Add/remove por dia
- Salvar
- Status

### Fora de escopo

- Mobile
- Gamificacao

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: profissional
- Casos de erro: catalogo vazio
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: sem trilha

## Especificacao tecnica

### Deve

- So catalogo master

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Editor de atividade nova

## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`

## Dependencias

- Task 018

## Slice vertical

### Identificador do slice

Slice 008 - Trilhas

### Arquivo do slice

- `tasks/slices/008-trilhas-semanais-evolucao.md`

### Objetivo de negócio

UI montagem.

### Entrega verificável do slice

Planejamento web.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |
| API | `contracts/openapi.yaml` | API | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- Salvar semana
- Progresso visivel

## Instrucoes de implementacao

- Menu Planejamentos

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- UI trilhas

## Riscos ou ambiguidades

- Sem wireframe calendario

## Resultado da execucao

UI web de montagem de trilha entregue:

- `/planejamentos` — lista pacientes ativos com CTA “Montar trilha”
- `/planejamentos/:patientId` — grade semanal (7 dias), add/remove do catálogo, sugerir pela anamnese, salvar semana, inativar trilha, progresso/evolução
- Link “Montar trilha” no perfil do paciente
- Menu Planejamentos restrito a `profissional`
- Service `trailService` + utils de semana ISO

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-018.md`

### Sob demanda

- `design-system/front/Design_System_Evolente_Desktop.md`
- `contracts/openapi.yaml` (trails/progress)
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`

## Handoff

- `.agents/state/handoffs/TASK-019.md`

## Arquivos alterados

- `front-end/src/types/trail.ts`
- `front-end/src/services/trails/trailService.ts`
- `front-end/src/utils/week.ts`, `week.test.ts`
- `front-end/src/pages/Main/Plans/**`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/constants/routes.ts`, `navigation.ts`
- `front-end/src/routes/index.tsx`
- `tasks/019-ui-montagem-trilha-web.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-019.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npm run test` — 16 files / 20 tests ok
- `cd front-end && npm run build` — ok

## Aderencia ao design system

- Menu Planejamentos; tabela de pacientes; botões primário/secundário; cards; estados vazio/loading/erro/sucesso
- Grade semanal adotada na ausência de wireframe de calendário

### Desvios

- Sem calendário visual detalhado (risco da task); grade por dia da semana
- Planejamentos oculto para master nesta fase (API/task = profissional)

## Pendencias pos-task

- Task 020 — execução da trilha no mobile

## Status final

done
