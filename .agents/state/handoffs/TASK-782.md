# Handoff — Task 782

## Status

done

## Decisões

- `expo-iap` para StoreKit
- Paywall só iOS via `Platform.OS` + `accessGranted === false`
- Android mantém bloqueio sem checkout in-app

## Pendências humanas

1. App Store Connect: produto `br.com.evolente.responsavel.monthly`
2. Env backend `APPLE_IAP_*`
3. `eas build` iOS (plugin nativo) + Sandbox
4. Reenvio review (junto com fix UIBackgroundModes audio já no app.json)

## Próximo contexto

- `docs/development/ios-iap-storekit.md` seção 4 e 8
