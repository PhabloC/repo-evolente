# Task 188 - Refinar modal de confirmação de inativação de usuários

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

### Por que

O modal de confirmar inativação estava espaçado demais e visualmente genérico para uma ação destrutiva.

### O que

Refinar o modal de confirmação: layout mais compacto, card do usuário, tom de alerta e CTAs mais claros.

## Contexto mínimo

- esta task
- `front-end/src/ui/Modal/**`
- `front-end/src/pages/Main/AdminUsers/**`

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- modal de inativação com hierarquia visual mais clara
- lint e testes AdminUsers ok

## Validacao esperada

- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/AdminUsers/index.test.tsx`

## Resultado da execucao

- Modal base ganhou `size="sm"`, `tone="danger"` e espaçamento mais compacto.
- Confirmação de inativação mostra card do usuário (avatar/nome/e-mail), texto mais claro e CTA coral com ícone Power.

## Arquivos alterados

- `front-end/src/ui/Modal/index.tsx`
- `front-end/src/ui/Modal/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validacoes executadas

- lint ok
- AdminUsers tests ok

## Handoff

- `.agents/state/handoffs/TASK-188.md`

## Status final

done
