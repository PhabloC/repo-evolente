# Handoff Task 705

- Slice: 059/060 — estabilidade nativa Expo iOS e OneSignal mobile
- Status final: done
- Decisões: `app.config.js` deriva modo OneSignal e entitlement APNs do `EAS_BUILD_PROFILE`; versão Expo incrementada para `1.0.1`.
- Arquivos: `mobile/app.json`, `mobile/app.config.js`, `ajustes.md`, task 705 e índice.
- Validações: Expo config em development/production, lint, typecheck e Jest passaram.
- Pendências: credenciais APNs/OneSignal e build TestFlight devem ser validados manualmente.
