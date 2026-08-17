# Handoff - Task 005

## Task

- identificador: Task 005
- título: Progressive disclosure, vertical slice e handoff
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 005 - Controle incremental de contexto
- objetivo de negócio: permitir planejamento, execução e retomada de tasks com menos contexto preventivo e mais rastreabilidade.
- entrega verificável: skills e modelos passam a exigir contexto mínimo, contexto sob demanda, vertical slices e handoff.

## Decisões preservadas

- decisão: manter backlog único da raiz como fonte de verdade.
- motivo: regra central do scaffold.
- impacto: handoff não cria escopo e não substitui task.

- decisão: não alterar código de produto.
- motivo: plano pediu mudanças de governança, skills e modelos.
- impacto: nenhuma stack de produto foi implementada.

- decisão: criar task raiz `tasks/change-requests/005-progressive-disclosure-vertical-slice-handoff.md`.
- motivo: a governança exige task da raiz antes de implementação.
- impacto: esta mudança fica rastreável no backlog único.

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `tasks/000-index.md`
- `tasks/change-requests/005-progressive-disclosure-vertical-slice-handoff.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `C:\Users\gabriel\Downloads\plano-progressive-disclosure-vertical-slice-handoff.md` | plano externo | definir escopo e critérios de aceite |
| `.agents/skills/planejar-tasks/...` | skills raiz | atualizar planejamento por vertical slices |
| `.agents/skills/executar-task/...` | skills raiz | atualizar execução por contexto mínimo e handoff |
| `.agents/skills/gerar-tasks-adicionais/SKILL.md` | change requests | declarar contexto incremental |
| `front-end/.agents/skills/executar-task/SKILL.md` | skill local | limitar contexto local da stack |
| `backend/.agents/skills/executar-task/SKILL.md` | skill local | limitar contexto local da stack |
| `mobile/.agents/skills/executar-task/SKILL.md` | skill local | limitar contexto local da stack |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` | não se aplica a mudança documental |
| `design-system/` | não houve UI |
| `contracts/openapi.yaml` | não houve integração cliente-servidor |
| `front-end/src`, `backend/src`, `mobile/` código de produto | fora do slice |
| `next-js/` | não foi citado na lista de skills locais do plano |

## Resultado por stack

- front-end: skill local de execução agora exige progressive disclosure local.
- backend: skill local de execução agora exige progressive disclosure local.
- mobile: skill local de execução agora exige progressive disclosure local.
- raiz: AGENTS, GUIDE, context-map, state, handoff-task, planejar-tasks, executar-task e gerar-tasks-adicionais atualizados.

## Arquivos alterados

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `.agents/state/README.md`
- `.agents/state/handoffs/.gitkeep`
- `.agents/state/slices/.gitkeep`
- `.agents/skills/handoff-task/SKILL.md`
- `.agents/skills/handoff-task/references/modelo-handoff.md`
- `.agents/skills/planejar-tasks/SKILL.md`
- `.agents/skills/planejar-tasks/references/regras-de-planejamento.md`
- `.agents/skills/planejar-tasks/references/modelo-task.md`
- `.agents/skills/planejar-tasks/references/modelo-index-tasks.md`
- `.agents/skills/executar-task/SKILL.md`
- `.agents/skills/executar-task/references/regras-de-execucao.md`
- `.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `.agents/skills/executar-task/references/modelo-relatorio-execucao.md`
- `.agents/skills/gerar-tasks-adicionais/SKILL.md`
- `front-end/.agents/skills/executar-task/SKILL.md`
- `backend/.agents/skills/executar-task/SKILL.md`
- `mobile/.agents/skills/executar-task/SKILL.md`
- `tasks/000-index.md`
- `tasks/change-requests/005-progressive-disclosure-vertical-slice-handoff.md`
- `.agents/state/handoffs/TASK-005.md`

## Validações executadas

- revisão textual dos fluxos: passou
- busca por termos obrigatórios: passou
- verificação de arquivos criados: passou

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- usar os novos modelos na próxima task planejada ou change request.

## Próximo contexto recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- task atual a executar
- handoff relacionado em `.agents/state/handoffs/`, se existir

## Contexto que não deve ser carregado na próxima etapa

- fonte: stacks não envolvidas na task.
- motivo: progressive disclosure exige carregar apenas fontes com gatilho explícito.
