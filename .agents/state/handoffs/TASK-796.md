# Handoff — Task 796

- **Título:** Restaurar login mobile de produção.
- **Slice:** `tasks/slices/057-configuracao-api-publica-mobile.md`.
- **Status final:** done.
- **Decisões preservadas:** o app da loja voltou para `https://evolente-api.fasters.app/api`. `api.evolente.com.br` responde no desktop, mas o aparelho não completa a conexão (erro sem HTTP response). Não trocar de novo sem unificar DNS/Cloudflare/WAF.
- **Contexto mínimo lido:** governança, índice, task, Slice 057 e handoff 795.
- **Contexto sob demanda carregado:** EAS production, `createAppError.ts`, probes axios/TLS dos dois hosts.
- **Arquivos alterados:** só rastreabilidade (task, slice, índice e este handoff).
- **Validações executadas:** variável revertida; OTA Android `93183394-a4bc-41f5-b2e7-91e4fb6633e4` e iOS `7898af5f-3d24-4919-9406-b71a1b1873f7`; bundle contém `evolente-api.fasters.app`.
- **Pendências:** o usuário precisa fechar e abrir o app duas vezes; unificar os hosts da API antes de repetir a Task 795.
- **Próxima ação sugerida:** validar o login no aparelho após o segundo reopen.
- **Próximo contexto recomendado:** Cloudflare/DNS de `api.evolente.com.br` e o dashboard EAS dos updates.
- **Contexto que não deve ser carregado:** design-system, OpenAPI, UI e código de jogos.
