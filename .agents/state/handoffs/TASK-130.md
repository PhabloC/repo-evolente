# Handoff - Task 130

## Identificador

- Task 130 - Habilitar alias `@/` nas rotas do mobile
- `tasks/change-requests/130-habilitar-alias-arroba-nas-rotas-mobile.md`

## Slice vertical

- Slice 001 - Fundacao e contrato base
- `tasks/slices/001-fundacao-contrato-base.md`

## Status final

done

## Decisoes preservadas

- O mobile passou a declarar `@/* -> ./src/*` no `tsconfig.json`, sem `baseUrl`
- O alias foi aplicado apenas ao eixo `routes/linking/app gate` e aos tipos de rota usados nas telas auth
- Nao houve limpeza global dos imports relativos da stack

## Contexto efetivamente usado

- Task 130, slice 001, handoff `TASK-129`, `mobile/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `mobile/tsconfig.json`, `src/routes`, `src/config/linking.ts`, `src/app/AppGate.tsx` e telas auth relacionadas

## Arquivos alterados

- `mobile/tsconfig.json`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/config/linking.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/PasswordResetScreen.tsx`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok (11 suites, 22 testes)

## Pendencias

- Decidir em task futura se a padronizacao com `@/` deve ser estendida para toda a stack mobile

## Proximo contexto recomendado

- `mobile/src/routes/` e `mobile/src/app/` para novos ajustes de infraestrutura de navegacao
