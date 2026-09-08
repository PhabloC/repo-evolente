# Handoff — Task 631

- **Título:** Configurar API pública no EAS para mobile.
- **Slice:** `tasks/slices/057-configuracao-api-publica-mobile.md`.
- **Status final:** done.
- **Decisões preservadas:** a base pública válida é `https://evolente-api.fasters.app/api`; ela foi registrada como `EXPO_PUBLIC_API_URL` no ambiente EAS `production`. A variável é pública e deve conter somente a URL da API, nunca credenciais.
- **Contexto mínimo lido:** governança da raiz, índice, task e Slice 057.
- **Contexto sob demanda carregado:** `mobile/eas.json`, `mobile/src/config/env.ts`, `backend/src/main.ts`, endpoint público e documentação EAS.
- **Arquivos alterados:** `mobile/eas.json` e os arquivos de rastreabilidade da Task 631.
- **Validações executadas:** endpoint retornou JSON do Nest; EAS confirmou a criação e o carregamento da variável; build Android `749c5b96-ced8-4da2-8931-5c8f043dc276` (versionCode 4) foi iniciada.
- **Pendências:** aguardar a build, baixar o AAB e publicar no teste interno.
- **Próxima ação sugerida:** abrir o link da build EAS, baixar o AAB concluído e subir a versão 4 na Google Play.
- **Próximo contexto recomendado:** página/logs da build EAS e a faixa Teste interno do Play Console.
- **Contexto que não deve ser carregado:** requisitos, design system, contrato OpenAPI completo, telas web e código de backend além do prefixo da API.
