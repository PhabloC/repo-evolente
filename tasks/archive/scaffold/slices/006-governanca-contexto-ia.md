# Slice 006 - Governanca de contexto para IA

## Status

done

## Objetivo de negocio

Consolidar no scaffold as praticas de vertical slice, handoff e progressive disclosure descritas no documento anexado, para reduzir contexto preventivo e tornar execucoes futuras mais rastreaveis.

## Entrega verificavel

Guias, mapa de contexto, templates de change request e backlog raiz deixam explicito como fatiar specs grandes, quando carregar referencias sob demanda, como usar handoff e quando bloquear por excesso de contexto.

## Fora de escopo

- Alterar codigo de produto em `front-end/`, `next-js/`, `backend/` ou `mobile/`.
- Planejar backlog de um produto especifico.
- Criar ou alterar contrato OpenAPI.

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

- Change request sem slice correspondente deve ser considerada incompleta.
- Spec longa nao deve virar task unica executavel.
- Handoff ausente ou contraditorio deve ser registrado como lacuna, sem substituir a task.
- Excesso de fontes obrigatorias deve bloquear ou provocar fatiamento.

## Decisoes humanas confirmadas

- Solicitacao do usuario: analisar o repositorio, ler `GUIDE.md` e `README.md`, entender o scaffold e implementar as melhorias do documento anexado.

## Premissas adotadas

- A melhoria é de governança/documentacao do scaffold, sem impacto em UI, API ou codigo de produto.
- Como o backlog estava sem task executavel para esta solicitacao, a execucao criou uma change request raiz antes de implementar.

## Tasks relacionadas

- `tasks/change-requests/006-governanca-contexto-ia.md` - aplica as melhorias de governanca e rastreabilidade.

## Dependencias do slice

- Nenhuma

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `README.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task relacionada

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Documento anexado | `C:\Users\gabriel\Downloads\vertical-slice-handoff-progressive-disclosure.md` | para extrair melhorias de contexto, slice e handoff | sim |
| Skills raiz | `.agents/skills/gerar-tasks-adicionais/...` | para ajustar modelo e regra de change request | sim |
| Skills raiz | `.agents/skills/executar-task/...` e `.agents/skills/handoff-task/...` | somente se a execucao exigir mudança adicional nesses fluxos | nao |
| Produto/stacks | `front-end/`, `next-js/`, `backend/`, `mobile/` | nao carregar nesta task | nao |

## Risco de contexto

- baixo
- estrategia de fatiamento ou reducao de contexto: restringir a leitura aos guias raiz, mapa de contexto, skills raiz relacionadas e documento anexado.

## Observacoes de rastreabilidade

- A execucao atual recompõe uma task raiz porque havia handoff antigo de `Task 005`, mas o arquivo de task e o slice correspondente não estavam presentes no backlog atual.

## Status final

done
