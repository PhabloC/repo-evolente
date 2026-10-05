# Handoff - Task 776

## Task

- identificador: 776
- título: Ocultar badge de assinatura no card do responsável
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010
- entrega verificável: pill Assinatura oculta no card do responsável

## Decisões preservadas

- decisão: `SHOW_SUBSCRIPTION_BADGE = false` (não excluir código)
- impacto: pill e texto de pagamento ocultos; reativar = `true`

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- docs task/index/slice/handoff

## Pendências

- status "Acesso liberado/pendente" ainda visível no card

## Próxima ação sugerida

- Conferir no app ao expandir o nome do responsável
