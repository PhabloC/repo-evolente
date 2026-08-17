# Handoff - Task 121

## Task

- 121 - Login com biometria (digital/Face ID) no mobile
- Slice 021 - `tasks/slices/021-login-biometrico-mobile.md`
- status final: done

## Decisões preservadas

- Biometria só destrava tokens já persistidos no SecureStore; sem endpoint novo
- Após login com senha, Alert oferece ativar biometria (uma vez); "Agora não" marca `offered` e não pergunta de novo
- Com biometria ativa, o boot não autentica automaticamente: sessão fica no SecureStore até unlock, e a navegação só monta após a splash encerrar para o prompt aparecer no momento visível
- Na tela de login: prompt automático + CTA ghost (digital/Face ID) e fallback por e-mail/senha
- Logout limpa sessão e preferência biométrica

## Contexto usado

- Mínimo: AGENTS, GUIDE, context-map, índice, task 121, slice 021
- Sob demanda: auth mobile (service/hooks/screens/store), SecureStore, AppGate, app.json, docs mobile Architecture/Code Style/QA
- Evitado: requirements, OpenAPI, web, design system amplo fora do shell auth

## Arquivos alterados

- `mobile/package.json` / lockfile (`expo-local-authentication`)
- `mobile/app.json`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/biometricService.ts`
- `mobile/src/features/auth/services/biometricService.test.ts`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.test.ts`
- `mobile/src/features/auth/hooks/useBiometricSignIn.ts`
- `mobile/src/features/auth/hooks/useSignInForm.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/components/styles.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- task/slice/índice/handoff

## Validações

- eslint em `src/features/auth/**` ok
- eslint em `src/app/AppGate.tsx` ok
- `npm run typecheck` ok
- `npm run test` ok (19 testes)

## Pendências

- Em dispositivo físico/dev client: validar Face ID/digital nativos (Expo Go cobre a maior parte)
- Tela de perfil para ligar/desligar biometria ficou fora de escopo (CR futuro)

## Próximo contexto recomendado

- `mobile/src/features/auth/services/biometricService.ts` e `useBiometricSignIn.ts` se houver refino de UX ou toggle em perfil
- Não carregar web/backend/OpenAPI para ajustes locais de biometria
