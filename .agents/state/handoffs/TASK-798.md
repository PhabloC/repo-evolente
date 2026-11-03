# Handoff — Task 798

- **Título:** Publicar OTA da API nova no runtime 1.0.2.
- **Slice:** `tasks/slices/057-configuracao-api-publica-mobile.md`.
- **Status final:** done.
- **Decisões preservadas:** o Android da loja está em `1.0.2`; OTA `1.0.3` não chega nele. Android 1.0.2 recebeu `https://api.evolente.com.br/api` no grupo `134b3cec-09d7-4361-83cb-8699b2622b63`. `app.json` voltou para `policy: appVersion`.
- **Contexto mínimo lido:** governança, índice, task e Slice 057.
- **Contexto sob demanda carregado:** `mobile/app.json`, EAS production.
- **Arquivos alterados:** só rastreabilidade (runtimeVersion foi temporário).
- **Validações executadas:** `eas update` Android runtime 1.0.2 publicado.
- **Pendências:** fechar o app Android duas vezes; Task 799 ainda precisa de OTA com o novo texto da versão.
- **Próxima ação sugerida:** publicar OTA 1.0.2/1.0.3 com `getAppVersion`.
- **Próximo contexto recomendado:** feedback de login/biblioteca no aparelho.
- **Contexto que não deve ser carregado:** design-system, OpenAPI, UI web.
