# Task 187 - Botão inativar só ícone na página de usuários

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

Na tabela de usuários, o botão Inativar/Reativar deve exibir apenas o ícone, com `aria-label` para acessibilidade.

## Contexto mínimo

- esta task
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- botão de status só com ícone Power
- testes atualizados

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

- Botão Inativar/Reativar ficou só com ícone Power, circular, com `aria-label`.

## Arquivos alterados

- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`

## Validacoes executadas

- lint ok
- AdminUsers tests ok

## Handoff

- `.agents/state/handoffs/TASK-187.md`

## Status final

done
