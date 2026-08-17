# Task 496 - Estabilizar elevação do login e baixar um pouco o form

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Slice vertical

- Slice 002 - `tasks/slices/002-autenticacao.md`

## Objetivo

Baixar um pouco o form com teclado aberto; e-mail e senha devem elevar o mesmo tanto; restaurar layout completo só ao fechar o teclado (não ao trocar de campo).

## Criterios de aceite

- [x] form um pouco mais baixo (`paddingTop: 56` no lift)
- [x] hide do teclado com debounce — troca e-mail↔senha mantém o mesmo lift
- [x] layout original só após fechar teclado de fato
- [x] indice/handoff atualizados

## Resultado da execucao

- `useAuthKeyboardLift`: debounce de 200ms no hide; foco cancela hide pendente
- `bottomClusterLifted.paddingTop` 12 → 56

## Arquivos alterados

- `mobile/src/features/auth/hooks/useAuthKeyboardLift.ts`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/496-estabilizar-elevacao-login-baixar-form.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-496.md`

## Status final

done
