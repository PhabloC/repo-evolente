# Task 481 - Jogo dos erros: capa modal dedicada

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- n/a (só asset/config)

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/035-jogo-dos-erros.md`

## Objetivo

Usar `jogo_dos_erros/capa-modal-jogo-dos-erros.webp` como capa do modal (separada da capa do card).

## Criterios de aceite

- [x] `SPOT_DIFFERENCE_MODAL_COVER_FILE_NAME` aponta para o arquivo modal
- [x] Asset no S3
- [x] Bootstrap refresca `modalCoverUrl` legado compartilhado com a capa do card

## Resultado da execucao

Modal cover dedicada; upload S3 ok; specs PASS.

## Handoff

- `.agents/state/handoffs/TASK-481.md`

## Status final

done
