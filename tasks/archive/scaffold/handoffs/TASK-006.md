# Handoff - Task 006

## Task

- identificador: CR-006
- titulo: Governanca de contexto para IA
- tipo: shared
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Governanca de contexto para IA
- objetivo de negocio: consolidar praticas de vertical slice, handoff e progressive disclosure no scaffold.
- entrega verificavel: guias, mapa de contexto, templates e backlog deixam explicito como fatiar, carregar contexto sob demanda, gerar handoff e bloquear excesso de contexto.

## Decisões preservadas

- decisão: tratar a melhoria como governança raiz, sem alterar stacks de produto.
- motivo: o documento anexado descreve processo de uso de IA, nao feature de app.
- impacto: requirements, design-system, contrato e codigo das stacks foram evitados.

- decisão: criar `CR-006` e `Slice 006`.
- motivo: a governança do repo exige task raiz e slice antes da implementacao.
- impacto: a execução ficou rastreavel apesar do handoff antigo `TASK-005` apontar task ausente no backlog atual.

- decisão: criar uma referencia sob demanda em `.agents/references/context-engineering.md`.
- motivo: `AGENTS.md` deve ser indice curto, e detalhes longos devem ser carregados apenas quando houver gatilho.
- impacto: futuras execucoes podem consultar a regra sem carregar o documento externo inteiro.

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `README.md`
- `.agents/context-map.md`
- `tasks/000-index.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `C:\Users\gabriel\Downloads\vertical-slice-handoff-progressive-disclosure.md` | documento anexado pelo usuario | extrair melhorias de vertical slice, handoff e progressive disclosure |
| `.agents/skills/gerar-tasks-adicionais/SKILL.md` | criação da CR raiz | alinhar regras de change request |
| `.agents/skills/gerar-tasks-adicionais/references/modelo-change-request-task.md` | modelo incompleto para contexto/slice | adicionar campos obrigatorios |
| `.agents/state/README.md` | divergencia sobre local de slices | corrigir slices para `tasks/slices/` |
| `.agents/state/handoffs/TASK-005.md` | handoff antigo relacionado | preservar decisao sem depender de task ausente |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` | nao houve requisito de produto |
| `design-system/` | nao houve UI |
| `contracts/openapi.yaml` | nao houve API |
| `front-end/`, `next-js/`, `backend/`, `mobile/` | nao houve implementacao de stack |

## Resultado por stack

- raiz: guias, mapa de contexto, modelo de change request, referencia sob demanda, slice, task, indice e handoff atualizados.
- front-end ou next-js: nao se aplica.
- backend: nao se aplica.
- mobile: nao se aplica.

## Arquivos alterados

- `AGENTS.md`
- `GUIDE.md`
- `README.md`
- `.agents/context-map.md`
- `.agents/references/context-engineering.md`
- `.agents/state/README.md`
- `.agents/skills/gerar-tasks-adicionais/SKILL.md`
- `.agents/skills/gerar-tasks-adicionais/references/modelo-change-request-task.md`
- `tasks/000-index.md`
- `tasks/slices/006-governanca-contexto-ia.md`
- `tasks/change-requests/006-governanca-contexto-ia.md`
- `.agents/state/handoffs/TASK-006.md`

## Validações executadas

- revisão textual: passou.
- busca por termos de rastreabilidade: passou.
- `git status --short`: executado para conferir escopo.

## Pendências ou bloqueios

- nenhuma.

## Próxima ação sugerida

- usar `CR-006` e `.agents/references/context-engineering.md` como referencia quando futuras specs longas precisarem ser fatiadas.

## Próximo contexto recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- task atual a executar
- slice atual em `tasks/slices/`
- handoff relacionado em `.agents/state/handoffs/`, quando existir

## Contexto que não deve ser carregado na próxima etapa

- fonte: stacks, requirements, design-system ou contrato sem gatilho na task.
- motivo: progressive disclosure exige menor contexto suficiente para a proxima decisao.
