# TASK-737

- Slice: `035-jogo-dos-erros`
- Status final: done
- Decisão: rodada 10 usa `coleira` x `0.78` e `lampiao` x `0.05`, mantendo os valores verticais.
- Contexto usado: configuração de assets do Jogo dos erros, merge do bootstrap, teste de catálogo e handoff da Task 736.
- Arquivos alterados: `backend/src/modules/contents/spot-difference-game-assets.ts` e `backend/src/modules/contents/catalog-config-merge.spec.ts`.
- Validações: `git diff --check` passou; teste e lint direcionados ficaram sem saída prolongadamente e não foram concluídos.
- Pendência: reexecutar validações do backend.
- Próximo contexto recomendado: configuração da rodada 10 e teste de merge para nova calibração visual.
