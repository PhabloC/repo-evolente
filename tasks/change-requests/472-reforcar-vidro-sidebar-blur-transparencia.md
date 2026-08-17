# Task 472 - Reforçar vidro do sidebar (blur + transparência)

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Tornar o efeito de vidro do sidebar perceptível, no mesmo espírito do login (capa borrada + véu translúcido).

## Criterios de conclusao

- [x] fundo do sidebar translúcido (não cream opaco)
- [x] bolhas mais visíveis e levemente borradas
- [x] overlay com `backdrop-filter`
- [x] blur do vidro desligado no scroll/aba oculta

## Resultado da execucao

- base ~22% cream; lava opacity 0.78 + blur 6px
- `::after` com backdrop-filter 16px; desliga via `:has([data-lava-lite/paused])`

## Arquivos alterados

- `front-end/src/layout/Sidebar/styles.module.css`
- `tasks/000-index.md`

## Status final

done
