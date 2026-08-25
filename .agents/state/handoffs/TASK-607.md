# Handoff - Task 607

## Task

- TASK-607 - Recovery mobile aplica elevação do login ao focar input
- status final: done

## Decisões

- A recuperação passou a reutilizar `useAuthKeyboardLift`; não há hook ou regra de teclado duplicada.
- O `onFocus` do e-mail é encaminhado por `PasswordRecoveryForm` para cancelar qualquer fechamento pendente e abrir o estado compacto.
- A tela replica a composição animada do login: hero e ilustração recolhem, e o formulário recebe a mesma elevação.

## Arquivos alterados

- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/components/PasswordRecoveryForm.tsx`

## Validações

- `git -C mobile diff --check` passou.
- Lint, typecheck e Jest foram iniciados, mas ficaram bloqueados sem resultado no ambiente; os processos iniciados foram encerrados.
- Falta conferir em emulador/dispositivo o foco do e-mail, a visibilidade acima do teclado e a restauração após fechá-lo.

## Próxima ação recomendada

- Abrir Recuperar senha em Android/iOS e validar o comportamento com o teclado real; depois repetir `npm run lint`, `npm run typecheck` e `npm run test` em ambiente sem processos bloqueados.
