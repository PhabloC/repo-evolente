# Task 415 - Qual está faltando: catálogo, assets, prévia e runtime

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `ContentGameType`, `WhatsMissingGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/036-qual-esta-faltando.md`

## Referencia visual

- print: `design-system/front/prints/qual-esta-faltando-cognicao.png`

## Resultado da execucao

- `gameType: whats-missing` no contrato, entity, validação e bootstrap
- 5 rodadas + 16 itens + capa no S3
- Prévia web com setup + prateleiras + opções
- Runtime mobile com renderer dedicado
- Conteúdo em `category: memoria`

## Criterios de aceite

- [x] `whats-missing` no contrato e enums
- [x] assets no bucket
- [x] bootstrap cria conteúdo em `memoria`
- [x] prévia web com escolha do item
- [x] mobile com escolha do item
- [x] testes essenciais

## Handoff

- `.agents/state/handoffs/TASK-415.md`

## Status final

done
