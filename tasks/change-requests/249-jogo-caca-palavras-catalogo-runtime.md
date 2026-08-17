# Task 249 - Jogo caça-palavras (catálogo + runtime)

## Status

done

## Tipo

shared

## Stacks envolvidos

backend, contracts, front-end, mobile

## Slice vertical

`tasks/slices/031-jogo-caca-palavras.md`

## Resultado da execucao

- `gameType: word-search` no contrato, backend, bootstrap com categorias/dificuldades e capa
- Capa enviada ao storage: `games/caca_palavras/capa_caca_palavra.webp`
- Biblioteca web: opção, card, prévia
- Mobile: setup categoria+dificuldade, grade H/V/diagonal, seleção por duas extremidades

## Arquivos principais

- `backend/src/modules/contents/**`
- `contracts/openapi.yaml`
- `front-end/src/pages/Main/Library/**`
- `mobile/src/features/games/**`

## Validacoes executadas

- bootstrap + contents service tests
- mobile typecheck + wordSearchGame tests
- upload capa S3 ok

## Status final

done
