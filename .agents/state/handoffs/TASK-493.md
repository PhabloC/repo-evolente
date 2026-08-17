# Handoff - Task 493

## Task

- identificador: TASK-493
- título: Esconder hero do login e subir form ao focar inputs
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 002
- entrega verificável: hero oculto + form no topo com teclado

## Decisões preservadas

- decisão: hero (logo + bem-vindo + subtítulo) recolhe a maxHeight/opacity 0
- decisão: spacer `flex:1` some e `bottomCluster` perde `marginTop: auto` → form sobe ao topo
- decisão: LayoutAnimation no toggle do teclado para transição estrutural
- impacto: recovery continua com `marginTop: auto` no bottomCluster compartilhado

## Arquivos alterados

- `SignInScreen.tsx`, `styles.ts`, task/index/slice/handoff

## Pendências

- validar no device se o form fica bem no topo com o teclado

## Próxima ação sugerida

- focar e-mail/senha e confirmar hero oculto + inputs no topo
