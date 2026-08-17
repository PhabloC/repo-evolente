# Task 414 - Jogo dos erros: catálogo, assets, prévia e runtime

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

- `contracts/openapi.yaml` — `ContentGameType`, `SpotDifferenceGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/035-jogo-dos-erros.md`

## Referencia visual

- print: `design-system/front/prints/jogo-dos-erros-articulacao.png`
- governa: layout comparação IMAGEM 1/2, banner de instrução, bloco “Faça o exercício”, checks de repetição
- lacunas: coordenadas dos hotspots estimadas — calibrar em QA

## Objetivo

Criar `gameType: spot-difference` com 5 rodadas, diferenças clicáveis, exercício oral pós-rodada, assets no S3, bootstrap, prévia web e renderer mobile.

## Resultado da execucao

- 5 pares A/B em `jogo_dos_erros/rounds/` + capas
- Upload S3 `dev/games/jogo_dos_erros/`
- Bootstrap `Jogo dos erros` em `articulatorio`
- Prévia web com cliques nos hotspots + exercício
- Runtime mobile com cliques + exercício

## Criterios de aceite

- [x] `spot-difference` no contrato e enums
- [x] 5 pares de imagens + hotspots no bucket
- [x] bootstrap cria conteúdo em `articulatorio`
- [x] prévia web com cliques nos erros
- [x] mobile com cliques nos erros + exercício
- [x] testes essenciais

## Handoff

- `.agents/state/handoffs/TASK-414.md`

## Status final

done
