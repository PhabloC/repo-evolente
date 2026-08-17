# Handoff - Task 113

## Task

- 113 - Exibir erro de login em modal central no mobile
- status final: done

## Decisões

- O erro de login saiu do `SignInForm` e passou a ser exibido pela `SignInScreen`
- O feedback agora usa `Modal` nativo com mensagem central e botão `OK`
- O hook `useSignInForm` expõe `clearSubmitError` para o fechamento explícito do modal

## Validacoes

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok
