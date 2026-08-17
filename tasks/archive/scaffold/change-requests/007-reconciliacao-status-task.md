# CR-007 - Reconciliacao de status de task

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

Feedback em imagem anexada pelo usuario informando que a skill `executar-task` finaliza handoff e indice, mas deixa o arquivo da task como `in_progress`.

## Objetivo

Tornar obrigatoria a atualizacao do status no proprio arquivo da task ao finalizar uma execucao.

## Escopo

- Explicitar no fluxo da skill `executar-task` quais blocos da task devem ser atualizados.
- Reforcar `regras-atualizacao-task.md` com reconciliacao final de status.
- Atualizar regras de rastreabilidade e modelo de relatorio para exigir evidencia dos status.
- Aplicar a mesma regra nas referencias locais de `front-end`, `backend` e `mobile`.
- Registrar slice, task, indice e handoff desta correcao.

## Fora de escopo

- Corrigir tasks antigas fora deste scaffold.
- Alterar codigo de produto.
- Alterar comportamento de planejamento de novas features.

## Entradas

- `.agents/skills/executar-task/SKILL.md`
- `.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `.agents/skills/executar-task/references/regras-de-execucao.md`
- `.agents/skills/executar-task/references/modelo-relatorio-execucao.md`
- `front-end/.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `backend/.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `mobile/.agents/skills/executar-task/references/regras-atualizacao-task.md`
- `tasks/000-index.md`

## Slice vertical

### Identificador do slice

Slice 007 - Reconciliacao de status de task

### Arquivo do slice

- `tasks/slices/007-reconciliacao-status-task.md`

### Objetivo de negocio

Garantir que uma task executada nao fique presa em `in_progress` quando a execucao ja foi finalizada.

### Entrega verificavel do slice

A skill `executar-task` exige que `## Status`, `## Status final`, indice, handoff e slice aplicavel sejam reconciliados antes da resposta final.

### Fora do slice

- Ajustar historico de outros projetos.
- Implementar rotinas automaticas.

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/007-reconciliacao-status-task.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Skill afetada | `.agents/skills/executar-task/SKILL.md` | para ajustar fluxo obrigatorio | sim |
| Regra de status | `.agents/skills/executar-task/references/regras-atualizacao-task.md` | para explicitar status da task | sim |
| Relatorio/rastreabilidade | `.agents/skills/executar-task/references/regras-de-execucao.md` e `modelo-relatorio-execucao.md` | para evidenciar reconciliacao | sim |
| Regras locais | `front-end/.agents/skills/executar-task/references/regras-atualizacao-task.md`, `backend/.agents/skills/executar-task/references/regras-atualizacao-task.md`, `mobile/.agents/skills/executar-task/references/regras-atualizacao-task.md` | para evitar repeticao do bug nas stacks | sim |

## Orçamento de contexto

- Fontes obrigatorias estimadas: 6
- Fontes sob demanda estimadas: 4
- Risco de contexto excessivo: baixo
- Estrategia para reduzir contexto: nao carregar stacks, requirements, design-system ou contrato.

## Dependencias

- Nenhuma

## Criterios de conclusao

- `regras-atualizacao-task.md` proibe finalizar apenas indice/handoff mantendo task `in_progress`.
- `SKILL.md` lista explicitamente os blocos da task que devem ser atualizados.
- `modelo-relatorio-execucao.md` inclui reconciliacao de status.
- `tasks/000-index.md` lista CR-007 como done.
- Handoff `TASK-007` criado.

## Instrucoes de implementacao

- Manter a correcao no escopo da skill raiz.
- Usar linguagem imperativa e verificavel.
- Nao alterar codigo de produto.

## Validacao esperada

- `rg` por `Reconciliacao obrigatoria de status`.
- `git diff --check`.
- `git status --short`.

## Entregaveis esperados

- Skill e referencias atualizadas.
- Slice, CR, indice e handoff registrados.

## Riscos ou ambiguidades

- Nenhum bloqueio identificado.

## Resultado da execucao

- Fluxo da skill `executar-task` passou a exigir atualizacao do bloco `## Status` da task e reconciliacao final.
- `regras-atualizacao-task.md` agora deixa claro que `## Status final` nao substitui `## Status`.
- Relatorio de execucao ganhou secao de reconciliacao de status.
- Regras locais de front-end, backend e mobile receberam a mesma instrucao de status.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`.
- Contexto sob demanda: arquivos da skill `executar-task` citados nesta task.
- Contexto evitado: stacks de produto, requirements, design-system e contrato.

## Handoff

- `.agents/state/handoffs/TASK-007.md`

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

## Validacoes executadas

- `rg` por `Reconciliacao obrigatoria de status`: passou.
- `git diff --check`: passou.
- `git status --short`: executado.

## Pendencias pos-task

- Nenhuma.

## Status final

done
