# Task 017 - Dashboard profissional: pacientes e perfil

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

- Dashboard profissional, listas, perfil, sidebar DS.

## Contexto de negocio

### Por que

Operacao diaria.

### O que

Lista, vinculo, perfil+anamnese, editar/inativar.

### Comportamento esperado

- Lista
- Modal vinculo
- Anamnese
- Inativar

### Fora de escopo

- Trilha
- Excluir

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: profissional
- Casos de erro: codigo invalido
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: zero pacientes

## Especificacao tecnica

### Deve

- Sem botao excluir
- Estados vazio/loading

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada


## Entradas

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/docs/ai/`
- `requirements/001-escopo-produto.md`

## Dependencias

- Task 016

## Slice vertical

### Identificador do slice

Slice 007 - Pacientes

### Arquivo do slice

- `tasks/slices/007-gestao-pacientes-profissional.md`

### Objetivo de negócio

UI pacientes.

### Entrega verificável do slice

Dashboard pacientes.

### Fora do slice

- Mobile

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | UI web | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | front | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Vinculo UI
- Anamnese
- Inativar

## Instrucoes de implementacao

- Menu Pacientes/Adicionar

## Validacao esperada

- npm run lint
- npm run build
- npm run test

## Entregaveis esperados

- UI pacientes

## Riscos ou ambiguidades



## Resultado da execucao

UI web de pacientes do profissional entregue:

- `/pacientes` — lista com filtro de status, empty/loading, modal vínculo por código, inativar/reativar, link ao perfil
- Vínculo do profissional ocorre apenas por código único do paciente; sem cadastro interno de responsável/criança
- `/pacientes/:patientId` — perfil com edição de dados, anamnese, inativar
- Sem botão excluir; navegação do profissional mantém apenas acesso à lista de pacientes
- Service `patientService` alinhado ao OpenAPI da Task 016

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-016.md`

### Sob demanda

- `design-system/front/Design_System_Evolente_Desktop.md`
- `contracts/openapi.yaml` (paths patients)
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md`

## Handoff

- `.agents/state/handoffs/TASK-017.md`

## Arquivos alterados

- `front-end/src/types/patient.ts`
- `front-end/src/services/patients/patientService.ts`
- `front-end/src/pages/Main/Patients/**` (lista, modal, perfil, styles, test)
- `front-end/src/constants/routes.ts`
- `front-end/src/constants/navigation.ts`
- `front-end/src/routes/index.tsx`
- `front-end/src/utils/age.ts`
- `tasks/017-dashboard-profissional-pacientes-web.md`
- `tasks/000-index.md`
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-017.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npm run test -- --run` — 21 files / 33 tests ok
- `cd front-end && npm run build` — ok
- Observacao: warnings preexistentes de `act(...)` continuam nos testes de auth, sem falha da suíte

## Aderencia ao design system

- Sidebar com acesso a Pacientes para o profissional
- Tabela com filtros, pills de status e ações no fim
- Modal de vínculo; estados vazio/loading/erro/sucesso
- Acessibilidade: labels, `role="status"/"alert"`, headings, botões nomeados

### Desvios

- Menu Pacientes/Adicionar oculto para master nesta fase (admin master = slice 009); DS lista master, mas API/task são do profissional

## Pendencias pos-task

- Nenhuma no Slice 007
- Próximo: Task 018 (API trilhas)

## Status final

done
