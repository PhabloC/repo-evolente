# Handoff - Task 019

## Task

- identificador: 019
- título: UI de montagem de trilha semanal (profissional)
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas
- objetivo de negócio: Trilhas semanais + evolução
- entrega verificável: Planejamento web (mobile Task 020)
- status do slice: in_progress

## Decisões preservadas

- decisão: `/planejamentos` lista pacientes ativos; `/planejamentos/:patientId` edita a semana
- motivo: menu Planejamentos + montagem no contexto do paciente
- impacto: CTA também no perfil do paciente

- decisão: grade 7 dias com add/remove via modal do catálogo active
- motivo: critérios add/remove por dia; só catálogo master
- impacto: sem editor de atividade nova

- decisão: salvar cria trilha ou `PUT items`; sugerir chama API anamnese
- motivo: contrato Task 018
- impacto: progresso listado abaixo da grade

- decisão: Planejamentos só para `profissional` na sidebar/rotas
- motivo: permissões da task; master admin fica fora
- impacto: master não vê o menu nesta fase

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/019-ui-montagem-trilha-web.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-018.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | planejamentos/sidebar/tabela |
| openapi trails/progress | API | payloads |
| ARCHITECTURE/CODE_STYLE/ACCESSIBILITY | front | estrutura + a11y |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile / backend docs | single-stack front |

## Resultado por stack

- front-end: done

## Arquivos alterados

- `front-end/src/pages/Main/Plans/**`
- `front-end/src/types/trail.ts`
- `front-end/src/services/trails/trailService.ts`
- `front-end/src/utils/week.ts`
- routes/navigation + link no perfil
- task/index/slice/handoff

## Validações executadas

- lint/test/build: ok (20 tests)

## Pendências ou bloqueios

- Task 020 execução mobile
- Sem wireframe de calendário — grade por dia adotada

## Próxima ação sugerida

- Executar Task 020 (`tasks/020-execucao-trilha-mobile.md`)

## Próximo contexto recomendado

- task 020 + DS mobile atividades + openapi progress/trails + mobile docs/ai

## Contexto que não deve ser carregado na próxima etapa

- fonte: design-system front / pages Plans
- motivo: Task 020 é mobile
