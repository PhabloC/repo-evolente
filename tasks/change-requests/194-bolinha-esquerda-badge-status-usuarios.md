# Task 194 - Bolinha à esquerda no badge de status da tabela de usuários

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

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto de negocio

### O que

Nos badges de status da tabela admin/usuários, exibir a bolinha indicadora à esquerda do texto.

## Contexto mínimo

- esta task
- `front-end/src/pages/Main/Admin/styles.module.css`

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- badge de status com bolinha à esquerda

## Validacao esperada

- `cd front-end && npm run lint`

## Resultado da execucao

- Badges de status usam `::before` circular à esquerda do texto.

## Arquivos alterados

- `front-end/src/pages/Main/Admin/styles.module.css`

## Validacoes executadas

- lint ok

## Handoff

- `.agents/state/handoffs/TASK-194.md`

## Status final

done
