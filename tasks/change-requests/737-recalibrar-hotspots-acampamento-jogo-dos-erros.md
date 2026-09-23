# Task 737 - Recalibrar hotspots do acampamento no Jogo dos erros

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- web: front-end
- mobile: sim

## Contrato

Não aplicável; ajuste de coordenadas no catálogo de jogo existente.

## Modo de execução

single-stack

## Slice vertical

- Slice 035 — `tasks/slices/035-jogo-dos-erros.md`

## Objetivo

Recalibrar, na rodada 10 (“No acampamento”), a coleira do cachorro para a direita e o lampião para a esquerda, conforme a imagem enviada pelo usuário.

## Entrega verificável

- Hotspot `coleira` da rodada 10 deslocado para a direita.
- Hotspot `lampiao` da rodada 10 deslocado para a esquerda.
- Configurações persistidas anteriormente recebem a correção por migração idempotente.

## Fora de escopo

- Alteração das imagens, raios, interação ou áudio.
- Alteração dos demais hotspots e rodadas.

## Dependências

- Slice 035 — concluído.
- Tasks 522, 733, 734, 735 e 736 — concluídas.

## Referência visual

- Imagem anexada pelo usuário nesta solicitação, mostrando a rodada “No acampamento”.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`

## Contexto sob demanda

- `backend/docs/ai/QA.md` — validar o teste direcionado do merge.
- `.agents/state/handoffs/TASK-736.md` — preservar a estratégia de migração idempotente.

## Orçamento de contexto

Carregar somente a configuração da rodada 10, a lógica de merge/migração e o teste diretamente relacionado.

## Critérios de aceite

- Coleira fica mais à direita e lampião mais à esquerda.
- Migração não altera os demais hotspots.
- Teste de regressão do merge é adicionado.

## Resultado da execucao

Na rodada 10, `coleira` foi movida de `0.73` para `0.78` e `lampiao` de `0.10` para `0.05`, mantendo as posições verticais. Foi adicionada migração idempotente e teste de regressão.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/docs/ai/QA.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `.agents/state/handoffs/TASK-736.md`

## Handoff

A migração da rodada 10 é restrita aos ids `coleira` e `lampiao`; os demais hotspots e rodadas permanecem inalterados.

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/737-recalibrar-hotspots-acampamento-jogo-dos-erros.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `.agents/state/handoffs/TASK-737.md`

## Validacoes executadas

- `git diff --check` na raiz e no backend — passou; apenas avisos de conversão LF/CRLF.
- Teste/lint direcionados do backend — não concluídos nesta execução porque os comandos ficaram sem saída prolongadamente no workspace.

## Pendencias pos-task

- Reexecutar o teste de merge e o lint direcionados do backend em uma janela dedicada.

## Status final

done

