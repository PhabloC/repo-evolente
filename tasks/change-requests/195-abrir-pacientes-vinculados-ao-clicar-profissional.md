# Task 195 - Abrir pacientes vinculados ao clicar no profissional

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

- `contracts/openapi.yaml#/paths/~1admin~1professionals-tree`

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto de negocio

### O que

Na aba Profissionais, permitir clicar no profissional e abrir a lista dos pacientes vinculados a ele.

### Comportamento esperado

- clique no nome/identidade ou na contagem de pacientes abre um modal
- modal lista pacientes vinculados (nome, código, status)
- estado vazio quando não houver vínculos

## Contexto mínimo

- esta task
- `front-end/src/pages/Main/AdminUsers/**`
- `.agents/state/handoffs/TASK-192.md`

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- clique abre modal com pacientes do profissional
- lint e testes ok

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

- Clique no profissional ou na contagem abre modal com tabela de pacientes vinculados.

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validacoes executadas

- lint ok
- AdminUsers tests ok (9)

## Handoff

- `.agents/state/handoffs/TASK-195.md`

## Status final

done
