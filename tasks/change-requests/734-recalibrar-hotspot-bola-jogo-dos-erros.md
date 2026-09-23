# Task 734 - Recalibrar hotspot da bola no Jogo dos erros

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

Mover mais para a esquerda o hotspot do erro da bola na rodada 5 (“No quarto”), conforme a imagem enviada pelo usuário.

## Entrega verificável

- Hotspot `bola` da rodada 5 deslocado horizontalmente para a esquerda.
- Configurações persistidas anteriormente recebem a mesma correção por migração idempotente.
- Demais hotspots e rodadas permanecem inalterados.

## Fora de escopo

- Alteração da imagem, raio do hotspot ou demais diferenças da rodada 5.
- Alteração de interação, áudio ou outras rodadas.

## Dependências

- Slice 035 — concluído.
- Tasks 522, 523 e 733 — concluídas.

## Referência visual

- Imagem anexada pelo usuário nesta solicitação, mostrando a rodada “No quarto” e o marcador da bola.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`

## Contexto sob demanda

- `backend/docs/ai/QA.md` — validar teste direcionado e qualidade do backend.
- handoff da Task 733 — preservar a estratégia de migrações idempotentes do catálogo.

## Orçamento de contexto

Carregar somente a configuração de assets da rodada 5, a lógica de merge/migração e o teste diretamente relacionado; não carregar front-end, mobile, contrato ou requirements.

## Critérios de aceite

- O hotspot da bola fica mais à esquerda na rodada 5.
- O bootstrap corrige a coordenada antiga sem alterar os demais hotspots.
- Teste direcionado do merge é adicionado.

## Resultado da execucao

O hotspot `bola` da rodada 5 foi movido de `(0.17, 0.82)` para `(0.10, 0.82)`. O bootstrap agora detecta a coordenada antiga e reaplica a configuração atualizada sem alterar os demais hotspots.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/docs/ai/QA.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `.agents/state/handoffs/TASK-733.md`

## Handoff

A migração da rodada 5 é restrita ao id `bola` e à coordenada horizontal antiga, preservando `y`, raio e os demais hotspots. A referência visual enviada foi usada para o deslocamento para a esquerda.

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/734-recalibrar-hotspot-bola-jogo-dos-erros.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `.agents/state/handoffs/TASK-734.md`

## Validacoes executadas

- `git diff --check` na raiz e no backend — passou; apenas avisos de conversão LF/CRLF.
- Teste/lint direcionados do backend — não concluídos nesta execução porque os comandos ficaram sem saída prolongadamente no workspace.

## Pendencias pos-task

- Reexecutar o teste de merge e o lint direcionados do backend em uma janela dedicada.

## Status final

done

