# Handoff - Task 777

## Task

- identificador: 777
- título: Alinhar cards de Últimos avisos ao Resumo rápido
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010
- entrega verificável: Últimos avisos com HomeActionCard clay

## Decisões preservadas

- decisão: reutilizar `HomeActionCard` (mesmo do Resumo rápido)
- motivo: pedido de mesmo design
- impacto: lista deixa de usar Pressable/noticeItemCard custom

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- docs task/index/slice/handoff

## Pendências

- estilos `noticeItem*` órfãos em `styles.ts`

## Próxima ação sugerida

- Conferir visualmente a tela Avisos no app
