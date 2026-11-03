# Task 782 - Mobile: paywall StoreKit só iOS

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `POST /subscriptions/apple/confirm` (task 781)

## Modo de execucao

single-stack

## Slice vertical

- Slice 070 — `tasks/slices/070-iap-storekit-ios.md`

## Escopo

- Paywall iOS com `expo-iap`, gate de login sem acesso, restore e confirm no backend.

## Criterios de aceite

- [x] iOS sem assinatura → paywall IAP após login
- [x] Fluxo compra/restore chama confirm no backend
- [x] Android sem UI de IAP (bloqueio web mantido)
- [x] Quem já tem `accessGranted` entra direto
- [x] Doc atualizado
- [ ] Compra Sandbox validada em device (pendente humano + build nativo)

## Resultado da execucao

- Feature `mobile/src/features/iap/` com `SubscribeScreen`, `expo-iap`, store de acesso.
- `authService` no iOS mantém sessão sem acesso; Android continua bloqueando.
- `RootNavigator` mostra `Subscribe` quando `accessGranted === false` no iOS.
- Plugin `expo-iap` no `app.json`.

## Contexto utilizado

- authService, RootNavigator, design tokens mobile, doc ios-iap

## Handoff

- `.agents/state/handoffs/TASK-782.md`

## Arquivos alterados

- `mobile/package.json` / lock (`expo-iap`)
- `mobile/app.json`
- `mobile/src/features/iap/**`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/routes/params.ts`
- `docs/development/ios-iap-storekit.md`

## Validacoes executadas

- Jest `authService.test.ts` — 7 passed

## Pendencias pos-task

- Criar produto no App Store Connect
- Configurar secrets backend
- Novo build EAS iOS + teste Sandbox
- Reenviar App Review

## Status final

done
