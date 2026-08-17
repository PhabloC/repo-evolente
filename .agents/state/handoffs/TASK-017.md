# Handoff - Task 017

## Task

- identificador: 017
- título: Dashboard profissional: pacientes e perfil
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 007 - Pacientes
- objetivo de negócio: Gestão pacientes (API + UI)
- entrega verificável: Dashboard pacientes web
- status do slice: done

## Decisões preservadas

- decisão: rotas `/pacientes` e `/pacientes/:patientId` só para `profissional`
- motivo: API 016 + permissões da task; o vínculo agora ocorre apenas por código e admin master fica para slice 009
- impacto: sidebar do profissional não expõe mais rota de cadastro interno

- decisão: vínculo do profissional apenas pelo modal de código na lista
- motivo: regra de negócio atualizada pelo usuário
- impacto: removidos rota, atalhos e wizard interno de cadastro de paciente

- decisão: inativar/reativar via `PATCH /patients/:id/status`; sem botão excluir
- motivo: regra de produto
- impacto: ações na lista e no perfil

- decisão: perfil mostra dados editáveis + anamnese read-only
- motivo: critérios de aceite (anamnese no perfil)
- impacto: trilha fora de escopo

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/017-dashboard-profissional-pacientes-web.md`
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-016.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | sidebar, tabela, modal, estados |
| openapi patients | API | payloads |
| ARCHITECTURE/CODE_STYLE/ACCESSIBILITY | front | estrutura + a11y |
| requirements 001/002 | regras | listar/vincular/perfil/inativar |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| backend docs / mobile | single-stack front |

## Resultado por stack

- front-end: done

## Arquivos alterados

- `front-end/src/pages/Main/Patients/**`
- `front-end/src/types/patient.ts`
- `front-end/src/services/patients/patientService.ts`
- routes/navigation/age util
- task/index/slice/handoff

## Validações executadas

- lint/test/build: ok (33 tests)
- warning residual: `act(...)` nos testes de auth permanece sem bloquear a suíte

## Pendências ou bloqueios

- Nenhuma no slice 007
- Próximo: Slice 008 / Task 018 (trilhas)

## Próxima ação sugerida

- Executar Task 018 (`tasks/018-api-trilhas-evolucao.md`)

## Próximo contexto recomendado

- task 018 + openapi (trilhas) + backend docs + requirements trilhas

## Contexto que não deve ser carregado na próxima etapa

- fonte: design-system front / pages Patients
- motivo: Task 018 é back
