# Task 417 - Quebra-cabeça: catálogo, assets, prévia e runtime

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

- `contracts/openapi.yaml` — `ContentGameType`, `JigsawGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/038-quebra-cabeca.md`

## Referencia visual

- print: `design-system/front/prints/quebra-cabeca-cognicao.png`
- governa: título, tabuleiro parcial, painel de peças, arrastar para encaixar
- lacunas: formato de peça real (MVP tiles); múltiplas cenas (gerar)

## Objetivo

Criar `gameType: jigsaw` com rodadas 3×3, drag-and-drop, assets no S3, bootstrap em `memoria`, prévia web e renderer mobile.

## Comportamento esperado

- Setup com capa modal + Começar jogo
- Cada rodada: tabuleiro com alguns slots já preenchidos + peças no banco
- Arrastar peça até o slot correto (snap); erro devolve ao banco
- Conclui a rodada ao completar a grade

## Contexto mínimo

- AGENTS, GUIDE, context-map, 000-index, esta task, slice 038

## Orçamento de contexto

- risco: medio — MVP 5 cenas 3×3 com tiles retangulares

## Criterios de aceite

- [x] `jigsaw` no contrato e enums
- [x] assets no bucket
- [x] bootstrap em `memoria`
- [x] prévia web com drag-and-drop
- [x] mobile com encaixe peça→slot (tap-to-place)
- [x] testes essenciais

## Status final

done
