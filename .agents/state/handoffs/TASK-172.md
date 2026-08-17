# Handoff - Task 172

## Task

- identificador: 172
- título: Distinguir O de U na validacao de escrita
- status final: done

## Decisões preservadas

- decisão: `O` exige gap ≤ 0.2 até o centro do topo (topo fechado)
- motivo: `U` largo passava no template de `O`
- impacto: `U` quando a letra é `O` é rejeitado; `O` fechado continua aceito

## Validações

- testes web/mobile de escrita — ok

## Pendências

- smoke manual no preview

## Próxima ação sugerida

- pedir `O`, escrever `U` → deve falhar; escrever `O` → deve passar
