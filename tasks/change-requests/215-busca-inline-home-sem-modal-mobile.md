# Task 215 - Busca inline na home sem modal

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Contrato

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Objetivo

Campo de busca na home deve abrir o teclado e filtrar na própria página, sem abrir modal/outra tela.

## Criterios de conclusao

- TextInput real no header
- resultados inline
- sem Modal de busca
- typecheck ok

## Resultado da execucao

- `HomeHeader` usa `TextInput` real (teclado nativo).
- Resultados de atividades/avisos aparecem na própria home ao digitar.
- Modal `ResponsavelSearchModal` removido.

## Handoff

- `.agents/state/handoffs/TASK-215.md`

## Status final

done
