# Handoff — Task 799

- **Título:** Versão do login segue a versão publicada.
- **Slice:** `tasks/slices/002-autenticacao.md`.
- **Status final:** done.
- **Decisões preservadas:** o rodapé do login usa `getAppVersion()` → `Constants.expoConfig.version`, com fallback para `nativeAppVersion`. Import estático de `app.json` removido. `expo.version` atual é `1.0.3`.
- **Contexto mínimo lido:** governança, índice, task e Slice 002.
- **Contexto sob demanda carregado:** SignInScreen e expo-constants.
- **Arquivos alterados:** `getAppVersion.ts`, teste e SignInScreen.
- **Validações executadas:** 2 testes do util passaram.
- **Pendências:** OTA ainda não inclui este JS; sem o update o login continua mostrando a versão do binário.
- **Próxima ação sugerida:** publicar OTA 1.0.2 (Android) e 1.0.3 (Android/iOS) com este código.
- **Próximo contexto recomendado:** EAS update e a tela de login no aparelho.
- **Contexto que não deve ser carregado:** backend, OpenAPI, biblioteca.
