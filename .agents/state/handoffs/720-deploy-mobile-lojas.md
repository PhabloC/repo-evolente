# Handoff Task 720

- Slice: `tasks/slices/061-deploy-lojas-mobile.md`
- Status final: blocked.
- Decisão: reutilizar as builds de produção já concluídas, sem gerar duplicatas.
- Builds prontas: Android 1.0.1 (13), ID `3adcf8fe-8905-476b-bcd0-0da86dbecd67`; iOS 1.0.1 (12), ID `6aa1a823-f671-4c2d-823f-e3baa88aae89`.
- Validações: lint passou com warning; typecheck tem falhas preexistentes; Jest 40/41 suítes passaram; EAS autenticado como `phabloc`.
- Bloqueios: Google Service Account ausente para Play Store; `ascAppId` ausente para App Store Connect.
- Próximo passo: executar `eas submit` pelo ID iOS; o fluxo interativo sugeriu `taliviasilva@gmail.com` e aguarda confirmação/autenticação Apple com 2FA.


