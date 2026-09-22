# Handoff Task 714

- Slice: `tasks/slices/060-one-signal-push-mobile.md`
- Status final: done
- Decisão: builds `preview`/`production` falham cedo sem `EXPO_PUBLIC_ONESIGNAL_APP_ID`; segredo REST permanece apenas no backend.
- Arquivos: `mobile/app.config.js`, exemplos `.env`, task 714, slice, índice.
- Validação: perfil development sem App ID passou; production sem App ID falhou explicitamente; production configurado resultou em plugin/entitlement de produção; App IDs locais coincidem; diff check passou.
- Pendência: configurar variáveis EAS, especialmente `EXPO_PUBLIC_API_URL` público (o `.env` local usa `192.168.2.143`), gerar novos builds e confirmar subscription/external_id no OneSignal.
- Próximo contexto: painel OneSignal, variáveis EAS/backend e logs do adapter durante um envio real.
