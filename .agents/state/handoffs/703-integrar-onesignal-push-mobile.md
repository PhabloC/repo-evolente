# Handoff Task 703

- Slice: 060 — Push OneSignal no mobile
- Status final: done
- Decisões: SDK inicializado no bootstrap; identificação usa `session.user.id`; App ID é `EXPO_PUBLIC_ONESIGNAL_APP_ID`; secrets não entram no mobile.
- Arquivos: configuração Expo, env, serviço OneSignal, AppBootstrap/AppGate e dependências mobile.
- Validação: typecheck possui falhas preexistentes fora da integração; lint executado.
- Pendências: adapter backend REST, credenciais APNs/FCM, entitlements production e teste em EAS development build.
- Próximo contexto: backend notifications adapter + secrets/configuração OneSignal.
