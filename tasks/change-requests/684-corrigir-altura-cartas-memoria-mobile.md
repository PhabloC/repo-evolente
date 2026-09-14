## Status

done

## Título

Corrigir altura das cartas do jogo da memória mobile

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/032-jogo-memoria.md`

## Objetivo

Impedir que a imagem do verso expanda indefinidamente as cartas do jogo da memória.

## Entrega verificável

As cartas ficam com dimensões regulares e a grade permanece utilizável no mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `mobile/src/features/games/components/MemoryGameRenderer/styles.ts`

## Contexto sob demanda

- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`: estrutura das cartas e imagens.

## Orçamento de contexto

Baixo; renderer e estilos do jogo.

## Resultado da execucao

A altura da carta e da imagem de verso foram fixadas em 148px, removendo o ciclo de dimensionamento causado por `height: '100%'`.

## Contexto utilizado

- Renderer e estilos do jogo da memória mobile.

## Handoff

Cartas do jogo corrigidas para altura fixa.

## Arquivos alterados

- `mobile/src/features/games/components/MemoryGameRenderer/styles.ts`
- `tasks/change-requests/684-corrigir-altura-cartas-memoria-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-684.md`

## Validacoes executadas

- Revisão estática dos estilos.

## Pendencias pos-task

- Nenhuma.

## Status final

done
