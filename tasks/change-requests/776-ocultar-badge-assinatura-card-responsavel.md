# Task 776 - Ocultar badge de assinatura no card do responsável

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

- nao se aplica

## Modo de execucao

single-stack

## Origem da solicitacao

Pedido do usuário: ao expandir o card do responsável, a badge "Assinatura ativa/sem acesso" deve ficar oculta (não excluir).

## Objetivo

Ocultar a pill de assinatura (e o texto de regularizar pagamento associado) no card do responsável no perfil.

## Escopo

- Flag `SHOW_SUBSCRIPTION_BADGE = false`
- Ocultar pill e texto de pagamento
- Ajustar accessibilityLabel

## Fora de escopo

- Excluir estilos/código da pill
- Status "Acesso liberado/pendente"

## Slice vertical

- Slice 010 - `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Criterios de conclusao

- [x] Badge oculta
- [x] Texto de pagamento oculto
- [x] Código permanece
- [x] Reativar via flag

## Resultado da execucao

- `SHOW_SUBSCRIPTION_BADGE = false` oculta a pill e o texto de regularizar pagamento.
- accessibilityLabel sem menção a assinatura.

## Handoff

- `.agents/state/handoffs/TASK-776.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/776-ocultar-badge-assinatura-card-responsavel.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-776.md`

## Validacoes executadas

- eslint no perfil — passou

## Pendencias pos-task

- Status "Acesso liberado/pendente" ainda aparece no card expandido; ocultar se a loja exigir.

## Status final

done
