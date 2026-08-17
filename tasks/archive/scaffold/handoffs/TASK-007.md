# Handoff - Task 007

## Task

- identificador: CR-007
- titulo: Reconciliacao de status de task
- tipo: shared
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 007 - Reconciliacao de status de task
- objetivo de negocio: garantir que execucoes de `executar-task` atualizem o status no arquivo da task.
- entrega verificavel: regras da skill exigem reconciliacao entre task, indice, handoff e slice aplicavel.

## Decisões preservadas

- decisao: corrigir a regra raiz da skill, nao uma task isolada.
- motivo: o feedback aponta comportamento recorrente da skill.
- impacto: futuras execucoes passam a validar o status principal da task antes de finalizar.

- decisao: explicitar que `## Status final` nao substitui `## Status`.
- motivo: o bug observado acontece quando o agente preenche resultado/handoff/indice mas nao altera o status do topo.
- impacto: a task so pode ser considerada finalizada quando ambos estiverem alinhados.

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `.agents/skills/executar-task/SKILL.md` | skill afetada | reforcar fluxo obrigatorio |
| `.agents/skills/executar-task/references/regras-atualizacao-task.md` | regra fraca de status | exigir atualizacao de `## Status` |
| `.agents/skills/executar-task/references/regras-de-execucao.md` | rastreabilidade | impedir conclusao com task `in_progress` |
| `.agents/skills/executar-task/references/modelo-relatorio-execucao.md` | evidencia final | adicionar reconciliacao de status |
| `front-end/.agents/skills/executar-task/references/regras-atualizacao-task.md` | regra local ambigua | alinhar status local |
| `backend/.agents/skills/executar-task/references/regras-atualizacao-task.md` | regra local ambigua | alinhar status local |
| `mobile/.agents/skills/executar-task/references/regras-atualizacao-task.md` | regra local ambigua | alinhar status local |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` | nao houve requisito de produto |
| `design-system/` | nao houve UI |
| `contracts/openapi.yaml` | nao houve API |
| stacks de produto | correcao limitada a governanca da skill |

## Resultado por stack

- raiz: skill `executar-task`, referencias, slice, task, indice e handoff atualizados.
- front-end ou next-js: nao se aplica.
- backend: nao se aplica.
- mobile: nao se aplica.

## Arquivos alterados

- `.agents/skills/executar-task/SKILL.md`
- `.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `.agents/skills/executar-task/references/regras-de-execucao.md`
- `.agents/skills/executar-task/references/modelo-relatorio-execucao.md`
- `front-end/.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `backend/.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `mobile/.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `tasks/000-index.md`
- `tasks/slices/007-reconciliacao-status-task.md`
- `tasks/change-requests/007-reconciliacao-status-task.md`
- `.agents/state/handoffs/TASK-007.md`

## Validações executadas

- `rg` por `Reconciliacao obrigatoria de status`: passou.
- `git diff --check`: passou.
- `git status --short`: executado.

## Pendências ou bloqueios

- nenhuma.

## Próxima ação sugerida

- Na proxima execucao de task, conferir se o arquivo da task muda de `in_progress` para `done` ou `blocked` junto com o indice e o handoff.

## Próximo contexto recomendado

- `.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `.agents/skills/executar-task/SKILL.md`
- task atual em execucao
- `tasks/000-index.md`

## Contexto que não deve ser carregado na próxima etapa

- fonte: stacks, requirements, design-system ou contrato sem gatilho na task.
- motivo: a correcao e de governanca da skill.
