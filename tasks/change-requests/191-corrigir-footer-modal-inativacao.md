# Task 191 - Corrigir footer do modal de inativação

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

Remover scroll horizontal do modal, dar gap entre botões, eliminar margem lateral da div de ações e afastar os botões do fundo do modal.

## Contexto mínimo

- esta task
- `front-end/src/pages/Main/AdminUsers/**`

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- sem scrollbar horizontal
- gap entre botões
- footer full-bleed nas laterais
- padding inferior afastando botões do fundo

## Validacao esperada

- `cd front-end && npm run lint`

## Resultado da execucao

- Removidas margens negativas (causa do scroll).
- Footer full-bleed com `gap` entre botões e `padding` inferior.

## Arquivos alterados

- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/styles.module.css`

## Validacoes executadas

- lint ok
- AdminUsers tests ok

## Handoff

- `.agents/state/handoffs/TASK-191.md`

## Status final

done
