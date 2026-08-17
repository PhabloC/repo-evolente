# Task 105 - Layout da recuperacao de senha igual ao login mobile

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
- `tasks/slices/002-autenticacao.md`

## Objetivo

Corrigir a interpretacao da Task 104: a tela de recuperar senha deve usar o mesmo layout visual do login (logo, menina_nuvem, secao de form), mantendo o conteudo textual de recuperacao e apenas o formulario diferente.

## Resultado da execucao

- `PasswordRecoveryScreen` reescrita no shell do login
- Removidos AuthHero/cards dessa tela
- Formulario continua `PasswordRecoveryForm` (e-mail + Enviar link)
- Link "Voltar ao login" em rosa
- lint/typecheck ok

### Nota sobre a Task 104

Na 104 foi alterado apenas o formulario interno da tela antiga (cards). Esta task corrige o layout da pagina inteira.

## Handoff

- `.agents/state/handoffs/TASK-105.md`

## Arquivos alterados

- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `tasks/change-requests/105-layout-recuperacao-igual-login-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-105.md`

## Status final

done
