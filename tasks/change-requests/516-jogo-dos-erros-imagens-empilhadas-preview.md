# Task 516 - Jogo dos erros: imagens empilhadas no modal de prévia

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

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/035-jogo-dos-erros.md`

## Objetivo

No modal de visualizar o Jogo dos erros, exibir as duas imagens uma abaixo da outra (largura total) para dar mais espaço de clique/visualização.

## Criterios de aceite

- [x] Comparação em coluna única no desktop e mobile
- [x] Proporção 4/3 alinhada às artes (sem quadrado 1:1)

## Resultado da execucao

- `.spotDiffCompare` em uma coluna
- `.spotDiffImageButton` com `aspect-ratio: 4 / 3`
- media query mobile redundante removida

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`

## Validacoes executadas

- revisão visual do CSS (cliques continuam normalizados no botão com `object-fit: cover`)

## Pendencias pos-task

- Conferir no browser com o modal aberto

## Handoff

- `.agents/state/handoffs/TASK-516.md`

## Status final

done
