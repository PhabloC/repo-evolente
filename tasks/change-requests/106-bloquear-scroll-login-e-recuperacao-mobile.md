# Task 106 - Bloquear scroll nas telas de login e recuperacao mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao

## Objetivo

Impedir scroll nas telas de login e esqueci a senha; conteudo deve caber na viewport.

## Resultado

- Removido `ScrollView` de SignIn e PasswordRecovery
- Canvas com `flex: 1` (sem `minHeight: 860`)
- Espacamentos/logo/nuvem/form compactados para caber na tela
- lint/typecheck ok

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/styles.ts`
- `tasks/change-requests/106-bloquear-scroll-login-e-recuperacao-mobile.md`
- `tasks/000-index.md`

## Status final

done
