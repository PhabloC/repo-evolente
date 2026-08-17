# Task 193 - Refinar coluna profissional na tabela de pacientes

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

Melhorar a apresentação da coluna Profissional na aba Pacientes, removendo o badge redundante e alinhando ao padrão visual da tabela.

## Contexto mínimo

- esta task
- `front-end/src/pages/Main/AdminUsers/**`

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- coluna profissional mais limpa e legível
- testes atualizados

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

- Com vínculo: avatar com inicial + nome do profissional.
- Sem vínculo: ícone + texto “Sem vínculo”.

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validacoes executadas

- lint ok
- AdminUsers tests ok

## Handoff

- `.agents/state/handoffs/TASK-193.md`

## Status final

done
