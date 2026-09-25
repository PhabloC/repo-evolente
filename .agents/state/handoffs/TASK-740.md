# Handoff Task 740

- Slice: `tasks/slices/060-one-signal-push-mobile.md`
- Status final: `done`
- Decisões: usar `mobile/assets/logo-seal.png` como ícone pequeno OneSignal/Android; remover mídia do payload push comum.
- Contexto usado: configuração Expo, plugin OneSignal local, adapter REST backend e QA mobile/backend.
- Arquivos alterados: `mobile/app.json`, adapter OneSignal backend, teste do adapter, task/índice/slice.
- Validações: configuração Expo development/production, lint/test focados, build backend e `git diff --check` passaram; falhas amplas preexistentes estão registradas na task.
- Pendência: instalar novo build nativo Android e conferir o ícone no dispositivo.
- Próximo contexto: EAS/build Android e teste de entrega OneSignal; não recarregar telas do app.
