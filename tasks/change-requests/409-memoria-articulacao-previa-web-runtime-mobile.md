# Task 409 - Memória articulação: prévia web e runtime mobile

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- mobile

## Slice vertical

- Slice 034 - Jogo da memória de articulação
- `tasks/slices/034-jogo-memoria-articulacao.md`

## Resultado da execucao

- Prévia web (`MemoryPreviewModal`) exibe prompt “Faça o exercício” após acertar par com `instruction`
- Runtime mobile (`MemoryGameRenderer`) idem, com aviso de material quando `requiresMaterial`
- Parse de `memoryGame` (web/mobile) preserva `instruction` / `requiresMaterial`
- Jogo de articulação reutiliza o renderer `memory` existente e aparece na aba Articulação via `category: articulatorio` (bootstrap Task 408)

## Handoff

- `.agents/state/handoffs/TASK-409.md`

## Validacoes executadas

- `mobile` memoryGame utils + MemoryGameRenderer tests

## Pendencias pos-task

- Task 410 (capas dedicadas / polish)
- Reiniciar backend para bootstrap criar o conteúdo no banco local, se ainda não existir

## Status final

done
