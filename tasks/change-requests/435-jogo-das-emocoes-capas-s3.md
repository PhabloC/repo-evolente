# Task 435 - Jogo das Emoções: capas no S3

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- N/A (EmotionsGameConfig já existente)

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/044-jogo-das-emocoes.md`

## Objetivo

Publicar capas locais de `jogo_das_emocoes/` no S3 e atualizar bootstrap para `coverUrl` / `modalCoverUrl`.

## Criterios de aceite

- [x] script de upload
- [x] arquivos no S3
- [x] bootstrap aponta para as URLs das capas
- [x] nomes alinhados aos arquivos locais

## Resultado da execucao

Capas `capa-jogo-emocoes.webp` e `capa-modal-jogo-emocoes.webp` publicadas em `dev/games/jogo_das_emocoes/` e config do catálogo refreshed.

## Validacoes executadas

- `node scripts/upload-emotions-assets.mjs` — 2 arquivos uploaded
- HEAD S3 capa — HTTP 200
- bootstrap log: `Default emotions game config refreshed`

## Handoff

- `.agents/state/handoffs/TASK-435.md`

## Status final

done
