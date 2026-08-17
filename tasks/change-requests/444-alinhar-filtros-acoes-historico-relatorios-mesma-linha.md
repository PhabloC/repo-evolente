# Task 444 - Alinhar filtros e ações do histórico de relatórios na mesma linha

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

- print do chat do bloco "Filtrar histórico"

## Objetivo

Colocar Paciente, Gerado de, Gerado até, Limpar filtros e Ir para planejamentos na mesma linha, com espaçamento ajustado.

## Contexto mínimo

- fontes globais, esta task, slice 011

## Contexto sob demanda

- `Reports/styles.module.css` (e JSX se preciso)

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] campos e botoes na mesma linha no desktop
- [x] espaçamento equilibrado; responsivo empilha quando necessario

## Resultado da execucao

- grade do historico com 3 campos + acoes na mesma linha
- botoes em `.historyFilterActions` sem `grid-column: 1 / -1`
- tablet/mobile empilham com espacamento consistente

## Handoff

- `.agents/state/handoffs/TASK-444.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

## Status final

done
