# Task 660 - Exibir versão do app no login mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile (Expo)

## Contrato

Não aplicável.

## Modo de execução

single-stack

## Slice vertical

- Slice 002 — autenticação mobile

## Resultado da execucao

Exibida a versão oficial do app no rodapé do formulário de login, lendo `expo.version` de `mobile/app.json`.

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`

## Validacoes executadas

- Revisão do valor oficial em `mobile/app.json` (`1.0.1`).

## Pendencias pos-task

- Incrementar `expo.version` em `mobile/app.json` a cada release do app.

## Status final

done
