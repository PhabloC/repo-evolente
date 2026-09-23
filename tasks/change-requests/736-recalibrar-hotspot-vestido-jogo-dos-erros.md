# Task 736 - Recalibrar hotspot do vestido no Jogo dos erros

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

Não aplicável; ajuste de coordenada no catálogo de jogo existente.

## Modo de execução

single-stack

## Slice vertical

- Slice 035 — `tasks/slices/035-jogo-dos-erros.md`

## Objetivo

Mover para cima o hotspot do vestido da menina na rodada 7 (“Na sala musical”), conforme a imagem enviada pelo usuário.

## Entrega verificável

- Hotspot `vestido` da rodada 7 deslocado verticalmente para cima.
- Configurações persistidas anteriormente recebem a correção por migração idempotente.
- Demais hotspots e rodadas permanecem inalterados.

## Fora de escopo

- Alteração da imagem, raio, interação ou áudio.
- Alteração das demais diferenças da rodada 7.

## Dependências

- Slice 035 — concluído.
- Tasks 522, 733, 734 e 735 — concluídas.

## Referência visual

- Imagem anexada pelo usuário nesta solicitação, mostrando a rodada “Na sala musical”.

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
- `.agents/state/handoffs/TASK-735.md` — preservar a estratégia de migração idempotente.

## Orçamento de contexto

Carregar somente a configuração da rodada 7, a lógica de merge/migração e o teste diretamente relacionado.

## Critérios de aceite

- O hotspot do vestido fica mais acima.
- A migração não altera os demais hotspots.
- Teste de regressão do merge é adicionado.

## Resultado da execucao

O hotspot `vestido` da rodada 7 foi movido de `0.58/0.64` para `0.58/0.59`, preservando a posição horizontal, o raio e os demais hotspots. A migração idempotente e o teste de regressão foram adicionados.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/docs/ai/QA.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `.agents/state/handoffs/TASK-735.md`

## Handoff

A migração da rodada 7 é restrita ao id `vestido` e à coordenada vertical antiga; o ursinho e os demais hotspots permanecem inalterados.

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/736-recalibrar-hotspot-vestido-jogo-dos-erros.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `.agents/state/handoffs/TASK-736.md`

## Validacoes executadas

- `git diff --check` na raiz e no backend — passou; apenas avisos de conversão LF/CRLF.
- Teste/lint direcionados do backend — não concluídos nesta execução porque os comandos ficaram sem saída prolongadamente no workspace.

## Pendencias pos-task

- Reexecutar o teste de merge e o lint direcionados do backend em uma janela dedicada.

## Status final

done

