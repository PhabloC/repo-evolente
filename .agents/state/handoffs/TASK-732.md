# TASK-732

- Slice: `035-jogo-dos-erros`
- Status final: done
- Decisão: erro de toque fora de hotspot no mobile usa `announceRetry()` e o feedback visual diz “Tente novamente.”.
- Contexto usado: renderer SpotDifference, provider GameSessionAudio, docs mobile de estilo/QA e contexto mínimo da raiz.
- Arquivo principal alterado: `mobile/src/features/games/components/SpotDifferenceGameRenderer/index.tsx`.
- Validações: lint direcionado passou; typecheck passou; Jest completo interrompido após duração prolongada sem saída; `git diff --check` passou.
- Pendências: ausência preexistente de `mobile/docs/ai/ACCESSIBILITY.md`; reexecutar Jest completo em janela dedicada.
- Próximo contexto recomendado: nenhum para esta correção; carregar o renderer apenas se houver novo ajuste de feedback do Jogo dos erros.
