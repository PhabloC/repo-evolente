# Slice 007 - Reconciliacao de status de task

## Status

done

## Objetivo de negocio

Garantir que execucoes da skill `executar-task` finalizem a task no proprio arquivo da task, no indice e no handoff com status consistente.

## Entrega verificavel

A regra de atualizacao da skill raiz e das referencias locais passa a exigir reconciliacao final entre `## Status`, `## Status final`, `tasks/000-index.md`, handoff e slice aplicavel.

## Fora de escopo

- Corrigir tasks antigas ja executadas em outros projetos.
- Alterar codigo de produto nas stacks.
- Mudar o modelo de planejamento de produto.

## Perfil do projeto

- stack web escolhida: nao se aplica
- mobile: nao se aplica

## Stacks envolvidas

- raiz

## Contrato

- nao se aplica

## Referencia visual por stack

### Web

- tipo: nao se aplica
- fonte primaria: `nao se aplica`

### Mobile

- tipo: nao se aplica
- fonte primaria: `nao se aplica`

## Permissoes e atores

- nao se aplica

## Casos de erro e borda

- Task marcada como `done` no indice, mas ainda `in_progress` no arquivo da task.
- Handoff criado com status final, mas task sem status final aplicado.
- Slice finalizado sem refletir status quando a task conclui o slice.

## Decisoes humanas confirmadas

- Feedback recebido na imagem: a execucao cria handoff e atualiza o indice, mas mantem a task como `in_progress`.

## Premissas adotadas

- O problema vem de instrucao ambigua na regra de atualizacao da task, que nao exigia explicitamente alterar o bloco `## Status`.

## Tasks relacionadas

- `tasks/change-requests/007-reconciliacao-status-task.md` - fortalece as regras da skill `executar-task`.

## Dependencias do slice

- Nenhuma

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task relacionada

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Skill afetada | `.agents/skills/executar-task/SKILL.md` | para ajustar o fluxo obrigatorio | sim |
| Regra afetada | `.agents/skills/executar-task/references/regras-atualizacao-task.md` | para explicitar status da task | sim |
| Rastreabilidade | `.agents/skills/executar-task/references/regras-de-execucao.md` e `modelo-relatorio-execucao.md` | para reforcar fechamento verificavel | sim |
| Regras locais | `front-end/.agents/skills/executar-task/references/regras-atualizacao-task.md`, `backend/.agents/skills/executar-task/references/regras-atualizacao-task.md`, `mobile/.agents/skills/executar-task/references/regras-atualizacao-task.md` | para evitar repeticao nas stacks | sim |

## Risco de contexto

- baixo
- estrategia de fatiamento ou reducao de contexto: limitar a leitura aos arquivos da skill `executar-task` e ao backlog raiz.

## Observacoes de rastreabilidade

- Esta correcao foi motivada por feedback externo mostrado em imagem anexada pelo usuario.

## Status final

done
