# Task 442 - Alinhar botão gerar relatório na mesma linha dos filtros

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

- print do chat do bloco "Gerar relatório" na pagina `/relatorios`

## Objetivo

Colocar o botao "Gerar relatório" na mesma linha dos campos Paciente / De / Até, imediatamente apos o filtro Até.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 011

## Contexto sob demanda

| Gatilho | Fonte | Obrigatório? |
|---|---|---|
| UI | `front-end/src/pages/Main/Reports/styles.module.css` (+ JSX se preciso) | sim |

## Orçamento de contexto

- baixo

## Criterios de conclusao

- [x] botao na mesma linha, apos Até, no desktop
- [x] responsivo continua utilizavel

## Dependencias

- nenhuma bloqueante

## Resultado da execucao

- `.headerActions` do formulario de geracao deixava o botao em linha propria (`grid-column: 1 / -1`)
- criado `.filtersSubmit` como 4a coluna alinhada aos inputs; em ≤1120px ocupa linha completa

## Handoff

- `.agents/state/handoffs/TASK-442.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

## Validacoes executadas

- revisao visual do CSS/grid; sem teste dedicado da pagina Reports

## Pendencias pos-task

- nenhuma

## Status final

done
