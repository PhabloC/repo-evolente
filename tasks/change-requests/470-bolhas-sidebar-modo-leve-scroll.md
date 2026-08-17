# Task 470 - Bolhas do sidebar animam no scroll em modo leve

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

Manter as bolhas do sidebar em movimento durante o scroll, sem o custo do filtro goo e do wobble de border-radius.

## Criterios de conclusao

- [x] scroll ativa modo leve (`data-lava-lite`), não pausa total
- [x] aba oculta continua com pausa total
- [x] testes de persistentLava atualizados

## Resultado da execucao

- `scroll` → sem filtro goo + wobble pausado; `translateY` segue
- `hidden` → `animation-play-state: paused`

## Arquivos alterados

- `front-end/src/layout/Sidebar/persistentLava.tsx`
- `front-end/src/layout/Sidebar/styles.module.css`
- `front-end/src/layout/Sidebar/persistentLava.test.tsx`
- `tasks/000-index.md`

## Status final

done
