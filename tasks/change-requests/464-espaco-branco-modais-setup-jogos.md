# Task 464 - Preencher espaço em branco dos modais de setup dos jogos

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Contexto mínimo

- CSS compartilhado `memorySetupPanel` / `memorySetupFooter`
- print do modal Diálogos em Ação no chat

## Contexto sob demanda

- `front-end/src/pages/Main/Library/styles.module.css`

## Orçamento de contexto

- baixo; ajuste de layout compartilhado

## Objetivo

Eliminar o vão branco no painel direito dos modais de setup dos jogos, ancorando o CTA no rodapé.

## Criterios de conclusao

- [x] painel em flex column (margin-top auto do footer funciona)
- [x] botão Jogar/Começar no rodapé do painel
- [x] título/copy no topo; seções intermediárias preservadas

## Resultado da execucao

- `.memorySetupPanel`: `display: flex; flex-direction: column`
- footers com `margin-top: auto` efetivo

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/000-index.md`

## Status final

done
