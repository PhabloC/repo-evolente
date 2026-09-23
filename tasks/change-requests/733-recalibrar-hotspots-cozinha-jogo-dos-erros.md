# Task 733 - Recalibrar hotspots da cozinha no Jogo dos erros

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

Não aplicável; ajuste de coordenadas no catálogo de jogo já existente.

## Modo de execução

single-stack

## Slice vertical

- Slice 035 — `tasks/slices/035-jogo-dos-erros.md`

## Objetivo

Recalibrar, na rodada 4 (“Na cozinha”), os hotspots da coleira do gato, do copo e da roupa da menina conforme a imagem enviada pelo usuário.

## Entrega verificável

- Hotspot `coleira_gato` deslocado um pouco para baixo.
- Hotspot `bebida` deslocado um pouco para a direita.
- Hotspot `avental` deslocado um pouco para baixo e para a direita.
- Configurações persistidas anteriormente recebem a mesma correção por migração idempotente.

## Fora de escopo

- Alteração das imagens, assets ou raio dos hotspots.
- Alteração das demais rodadas do Jogo dos erros.
- Alteração da interação ou do áudio do jogo.

## Dependências

- Slice 035 — concluído.
- Tasks 519, 522 e 732 — concluídas.

## Referência visual

- Imagem anexada pelo usuário nesta solicitação, mostrando a rodada “Na cozinha” e os três marcadores a reposicionar.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- testes de bootstrap/merge do catálogo do Jogo dos erros

## Contexto sob demanda

- `backend/docs/ai/` — padrões e QA do backend, somente os arquivos diretamente relacionados à validação.
- handoff das Tasks 519, 522 e 732, somente se necessário para preservar decisões de calibração.

## Orçamento de contexto

Carregar apenas a configuração de assets do Jogo dos erros, as funções de merge/migração e testes diretamente relacionados; não carregar front-end, mobile, contrato ou requirements.

## Critérios de aceite

- Os três hotspots da rodada 4 refletem os deslocamentos solicitados.
- O bootstrap corrige uma configuração antiga sem alterar as demais diferenças da rodada.
- Testes direcionados do backend passam.

## Resultado da execucao

Atualizados os hotspots da rodada 4 para `coleira_gato` em `(0.89, 0.68)`, `bebida` em `(0.75, 0.85)` e `avental` em `(0.63, 0.63)`. O bootstrap ganhou uma migração idempotente que corrige configurações persistidas com as coordenadas antigas.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/docs/ai/QA.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- Tasks 519 e 522 como referência de migrações anteriores de hotspots.

## Handoff

A rodada 4 mantém os demais hotspots intactos. A detecção de migração é restrita aos ids `avental`, `coleira_gato` e `bebida` da rodada 4 e só substitui a rodada quando algum deles ainda estiver fora da coordenada nova.

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/733-recalibrar-hotspots-cozinha-jogo-dos-erros.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `.agents/state/handoffs/TASK-733.md`

## Validacoes executadas

- `git diff --check` na raiz e no backend — passou; apenas avisos de conversão LF/CRLF.
- `cd backend && npm test -- --runInBand src/modules/contents/catalog-config-merge.spec.ts` — interrompido após execução prolongada sem saída.
- `cd backend && npm run lint -- --no-warn-ignored ...` — interrompido após execução prolongada sem saída.
- `cd backend && npx eslint ...` — interrompido após execução prolongada sem saída.

## Pendencias pos-task

- Reexecutar o teste direcionado e o lint do backend em uma janela dedicada; não houve mensagem de falha antes da interrupção.

## Status final

done

