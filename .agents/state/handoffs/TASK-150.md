# Handoff - Task 150

## Identificador

- Task 150 - Hardening de auth, storage e acessibilidade mobile
- `tasks/change-requests/150-hardening-auth-acessibilidade-mobile.md`

## Slice vertical

- Slice 024 - Hardening de auth, storage e acessibilidade mobile
- `tasks/slices/024-hardening-auth-acessibilidade-mobile.md`

## Status final

done

## Decisoes preservadas

- `TextField` passou a expor `ref` do `TextInput` para permitir foco programatico nos fluxos de auth
- Login e reset de senha passaram a encadear foco entre campos pelo teclado nativo
- `biometricPreferenceStorage` retorna a preferencia padrao quando `AsyncStorage` falha
- `sessionStorage` manteve compatibilidade com a chave legada `mobile:auth:session` e migra para `mobile.auth.session` quando possivel
- Cards/atalhos da home anunciam descricao e badges por default quando nenhuma `accessibilityLabel` explicita for fornecida
- `expo-status-bar` permanece como dependencia/componente, mas nao mais como plugin de configuracao

## Contexto efetivamente usado

- `ajustes_mobile.md`
- Task 150 e Slice 024
- handoffs `TASK-127` e `TASK-149`
- `mobile/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `COMPONENT_REUSE.md`, `QA.md`
- `mobile/app.json`
- `mobile/src/shared/components/TextField/index.tsx`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/screens/PasswordResetScreen.tsx`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeShortcutTile/index.tsx`

## Arquivos alterados

- `mobile/app.json`
- `mobile/src/shared/components/TextField/index.tsx`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/screens/PasswordResetScreen.tsx`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.test.ts`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeShortcutTile/index.tsx`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/shared/storage/secureStorage.test.ts`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok (12 suites, 30 testes)

## Pendencias

- Validar em device/emulador o foco entre campos de auth ao usar a acao `next/done` do teclado

## Proximo contexto recomendado

- `mobile/src/shared/components/TextField/index.tsx` e `mobile/src/features/auth/` para novos ajustes de ergonomia no auth
- `mobile/src/shared/storage/secureStorage.ts` para qualquer nova evolucao de sessao legada ou boot de auth

## Contexto que nao deve ser carregado

- `requirements/`, `contracts/openapi.yaml`, design system completo e stacks web/backend
