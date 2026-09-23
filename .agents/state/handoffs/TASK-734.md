# TASK-734

- Slice: `035-jogo-dos-erros`
- Status final: done
- Decisão: hotspot `bola` da rodada 5 foi movido para `(0.10, 0.82)`.
- Contexto usado: configuração de assets do Jogo dos erros, merge do bootstrap, teste de catálogo e handoff da Task 733.
- Arquivos alterados: `backend/src/modules/contents/spot-difference-game-assets.ts` e `backend/src/modules/contents/catalog-config-merge.spec.ts`.
- Validações: `git diff --check` passou; teste e lint direcionados ficaram sem saída prolongadamente e não foram concluídos.
- Pendência: reexecutar validações do backend.
- Próximo contexto recomendado: configuração da rodada 5 e teste de merge para nova calibração visual.
