# Task 190 - Ajustar largura e footer do modal de inativação

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

Aumentar a largura do modal de inativação, usar fundo cinza claro na div dos botões e remover padding lateral/inferior dessa div (footer full-bleed).

## Contexto mínimo

- esta task
- `front-end/src/pages/Main/AdminUsers/**`

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- modal mais largo
- footer cinza claro sem padding lateral/inferior

## Validacao esperada

- `cd front-end && npm run lint`

## Resultado da execucao

- Modal com largura até `34rem`, footer `#f3f4f6` full-bleed sem padding lateral/inferior.

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`

## Validacoes executadas

- lint ok

## Handoff

- `.agents/state/handoffs/TASK-190.md`

## Status final

done
