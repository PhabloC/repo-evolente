# Task 494 - Corrigir overshoot do login com Samsung Pass / pan

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

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - `tasks/slices/002-autenticacao.md`

## Objetivo

Com teclado/Samsung Pass, o form não pode ir para o topo absoluto (corta e-mail e sobe demais). Esconder hero/menina, mas manter o bloco dos inputs ancorado embaixo para o `pan` do Android posicionar acima do teclado.

## Criterios de aceite

- [x] hero/menina ocultos com teclado
- [x] e-mail e senha visíveis sem corte no topo
- [x] Samsung Pass não empurra o form para fora da tela (sem segundo deslocamento ao topo)
- [x] indice/handoff atualizados

## Resultado da execucao

Removido spacer collapse + `bottomClusterLifted` + LayoutAnimation. Hero/menina continuam recolhendo; form permanece com `marginTop: auto` e o `pan` do Android faz o ajuste fino (incluindo Samsung Pass).

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/494-corrigir-overshoot-login-samsung-pass-pan.md`
- `tasks/000-index.md`
- `tasks/slices/002-autenticacao.md`
- `.agents/state/handoffs/TASK-494.md`

## Status final

done
