# Handoff — Task 795

- **Título:** Apontar o mobile de produção para api.evolente.com.br.
- **Slice:** `tasks/slices/057-configuracao-api-publica-mobile.md`.
- **Status final:** done.
- **Decisões preservadas:** a base pública vigente do app de loja é `https://api.evolente.com.br/api`, a mesma do frontend `evolente.com.br`. A URL antiga `https://evolente-api.fasters.app/api` ficou só no site legado `evolente.fasters.app`. Publicação via EAS Update no canal `production` (runtime `1.0.3`); sem build de loja nem bump de `expo.version`.
- **Contexto mínimo lido:** governança da raiz, índice, task e Slice 057.
- **Contexto sob demanda carregado:** `mobile/eas.json`, `mobile/src/config/env.ts`, ambiente EAS `production` e o endpoint `https://api.evolente.com.br/api`.
- **Arquivos alterados:** apenas rastreabilidade (task, slice, índice e este handoff). Nenhum código do app.
- **Validações executadas:** Nest respondeu no prefixo `/api`; `eas env:list` confirmou a URL nova; OTA Android `b920a2fe-8b23-4af8-9753-63830991d7bc` e iOS `dff7e6f9-f6d5-468c-b9d1-91b4c545970a` publicados.
- **Pendências:** reabrir o app da loja para baixar o update; conteúdo da biblioteca não entra sozinho na trilha do dia.
- **Próxima ação sugerida:** abrir o app em produção, puxar para atualizar se preciso, e conferir a Biblioteca.
- **Próximo contexto recomendado:** dashboards EAS dos updates e a biblioteca em `evolente.com.br`.
- **Contexto que não deve ser carregado:** requirements, design-system, OpenAPI, UI web/mobile e código de backend além do prefixo da API.
