# Handoff Task 743

- Slice: `tasks/slices/060-one-signal-push-mobile.md`
- Status final: `done`
- Decisão: usar exatamente `mobile/assets/logo-seal-original.webp` em `notification.icon` e `smallIcons`, sem modificar a logo nem gerar outro asset.
- Validações: configuração Expo carregada com `notification.icon` e `smallIcons` apontando para `logo-seal-original.webp`; lint passou com warning preexistente; typecheck e testes possuem falhas preexistentes registradas na task.
- Pendência: validar visualmente no próximo build nativo Android.
