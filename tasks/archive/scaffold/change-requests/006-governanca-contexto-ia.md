# CR-006 - Governanca de contexto para IA

## Status

done

## Tipo

shared

## Stacks envolvidos

- raiz

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Perfil do projeto

- stack web escolhida: nao se aplica
- mobile: nao se aplica

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- nao se aplica

### Regra de aderencia visual

- nao se aplica

## Origem da solicitacao

Documento anexado `C:\Users\gabriel\Downloads\vertical-slice-handoff-progressive-disclosure.md` e pedido do usuario para analisar o repositorio, ler `GUIDE.md` e `README.md`, entender o scaffold e implementar as melhorias descritas.

## Objetivo

Consolidar no scaffold regras mais executaveis de vertical slice, handoff, progressive disclosure e orçamento de contexto.

## Escopo

- Atualizar guias raiz para explicitar `AGENTS.md` como indice e referencias sob demanda.
- Registrar referencia operacional curta sobre context engineering.
- Atualizar `context-map` com gatilhos de leitura sob demanda e regras de orçamento.
- Corrigir a orientacao de slices para `tasks/slices/`.
- Atualizar modelo/regra de change requests para exigir slice, contexto mínimo, contexto sob demanda e orçamento.
- Registrar slice, task, indice e handoff desta execucao.

## Fora de escopo

- Alterar codigo de produto.
- Planejar features de um produto especifico.
- Ler ou modificar requirements, design-system, contrato ou docs locais de stack.

## Entradas

- `AGENTS.md`
- `GUIDE.md`
- `README.md`
- `.agents/context-map.md`
- `.agents/skills/gerar-tasks-adicionais/SKILL.md`
- `.agents/skills/gerar-tasks-adicionais/references/modelo-change-request-task.md`
- `.agents/state/README.md`
- `C:\Users\gabriel\Downloads\vertical-slice-handoff-progressive-disclosure.md`

## Slice vertical

### Identificador do slice

Slice 006 - Governanca de contexto para IA

### Arquivo do slice

- `tasks/slices/006-governanca-contexto-ia.md`

### Objetivo de negocio

Consolidar praticas de contexto para que agentes futuros trabalhem por fatias menores, com memoria curta e menos leitura preventiva.

### Entrega verificavel do slice

As regras e modelos do scaffold orientam explicitamente como fatiar specs, carregar contexto sob demanda, produzir handoff e bloquear excesso de contexto.

### Fora do slice

- Implementacao em stacks de produto.
- Planejamento de produto real.

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `README.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-governanca-contexto-ia.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Documento anexado | `C:\Users\gabriel\Downloads\vertical-slice-handoff-progressive-disclosure.md` | para extrair melhorias solicitadas | sim |
| Skill de change request | `.agents/skills/gerar-tasks-adicionais/...` | para atualizar regras/modelo afetados | sim |
| Estado de agentes | `.agents/state/README.md` e `.agents/state/handoffs/TASK-005.md` | para verificar rastreabilidade anterior e evitar conflito | sim |
| Skills de execucao/handoff | `.agents/skills/executar-task/...`, `.agents/skills/handoff-task/...` | somente se surgir lacuna nesses fluxos | nao |

## Orçamento de contexto

- Fontes obrigatorias estimadas: 7
- Fontes sob demanda estimadas: 4
- Risco de contexto excessivo: baixo
- Estrategia para reduzir contexto: nao carregar requirements, design-system, contratos nem docs/codigo das stacks; usar o handoff antigo apenas para rastreabilidade.

## Dependencias

- Nenhuma

## Criterios de conclusao

- `README.md`, `GUIDE.md`, `AGENTS.md` e `.agents/context-map.md` apontam o fluxo de contexto incremental.
- Existe referencia sob demanda curta em `.agents/references/context-engineering.md`.
- Modelo de change request exige slice, contexto mínimo, contexto sob demanda e orçamento.
- `tasks/000-index.md` lista o novo slice/task e o handoff atualizado.
- Handoff da execucao existe em `.agents/state/handoffs/TASK-006.md`.

## Instrucoes de implementacao

- Manter mudanças no escopo documental e de governança.
- Nao carregar nem alterar stacks de produto.
- Preservar backlog unico na raiz.
- Evitar copiar integralmente o documento anexado; sintetizar regras operacionais.

## Validacao esperada

- Revisao textual dos arquivos alterados.
- Busca por termos de rastreabilidade (`context-engineering`, `CR-006`, `Slice 006`, `TASK-006`).
- `git status --short` para confirmar escopo de mudanças.

## Entregaveis esperados

- Arquivos de governança atualizados.
- Referencia sob demanda criada.
- Slice/task/handoff registrados.

## Riscos ou ambiguidades

- O handoff antigo de `Task 005` referencia uma task que nao existe mais no backlog; esta execucao registra uma nova CR para preservar rastreabilidade sem reescrever historico.

## Resultado da execucao

- Guias raiz atualizados para tratar `AGENTS.md` como indice e reforçar vertical slice, handoff e orçamento de contexto.
- `context-map` passou a exigir gatilho, motivo e menor fonte suficiente antes de leituras sob demanda.
- Modelo de change request passou a conter slice, contexto mínimo, contexto sob demanda, orçamento, contexto utilizado e handoff.
- `.agents/state/README.md` corrigido para registrar slices em `tasks/slices/`.
- Criada referencia operacional em `.agents/references/context-engineering.md`.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `README.md`, `.agents/context-map.md`, `tasks/000-index.md`.
- Contexto sob demanda: documento anexado, skill/modelo de `gerar-tasks-adicionais`, `.agents/state/README.md`, handoff antigo `TASK-005`.
- Contexto evitado: `requirements/`, `design-system/`, `contracts/openapi.yaml`, docs e codigo das stacks de produto.

## Handoff

- `.agents/state/handoffs/TASK-006.md`

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

## Validacoes executadas

- Revisao textual dos arquivos alterados: passou.
- Busca por termos de rastreabilidade: passou.
- `git status --short`: executado para conferir escopo.

## Pendencias pos-task

- Nenhuma.

## Status final

done
