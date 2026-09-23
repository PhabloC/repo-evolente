# Task 735 - Recalibrar hotspots da praia no Jogo dos erros

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

Mover para a esquerda os hotspots do balde, da estrela-do-mar e do barco na rodada 6 (“Na praia”), conforme a imagem enviada pelo usuário.

## Entrega verificável

- `balde`, `estrela_mar` e `barquinho` deslocados horizontalmente para a esquerda.
- Configurações persistidas anteriormente recebem a correção por migração idempotente.
- Demais hotspots e rodadas permanecem inalterados.

## Fora de escopo

- Alteração das imagens, raios, interação ou áudio.
- Alteração de outras rodadas.

## Dependências

- Slice 035 — concluído.
- Tasks 522, 523, 733 e 734 — concluídas.

## Referência visual

- Imagem anexada pelo usuário nesta solicitação, mostrando a rodada “Na praia”.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`

## Contexto sob demanda

- `backend/docs/ai/QA.md` — validar teste direcionado do merge.
- `.agents/state/handoffs/TASK-734.md` — preservar a estratégia de migração idempotente.

## Orçamento de contexto

Carregar apenas a configuração da rodada 6, a lógica de merge/migração e o teste diretamente relacionado.

## Critérios de aceite

- Os três hotspots solicitados ficam mais à esquerda.
- A migração não altera os demais hotspots.
- Teste de regressão do merge é adicionado.

## Resultado da execucao

Os hotspots foram movidos para a esquerda: `barquinho` em `0.13/0.39`, `balde` em `0.14/0.88` e `estrela_mar` em `0.38/0.91`. Foi adicionada migração idempotente para configurações persistidas com as coordenadas antigas e teste de regressão do merge.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/docs/ai/QA.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `.agents/state/handoffs/TASK-734.md`

## Handoff

A migração da rodada 6 é restrita aos ids `barquinho`, `balde` e `estrela_mar`; bola, faixa do chapéu e demais rodadas permanecem inalteradas.

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/735-recalibrar-hotspots-praia-jogo-dos-erros.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `.agents/state/handoffs/TASK-735.md`

## Validacoes executadas

- `git diff --check` na raiz e no backend — passou; apenas avisos de conversão LF/CRLF.
- Teste/lint direcionados do backend — não concluídos nesta execução porque os comandos ficaram sem saída prolongadamente no workspace.

## Pendencias pos-task

- Reexecutar o teste de merge e o lint direcionados do backend em uma janela dedicada.

## Status final

done

