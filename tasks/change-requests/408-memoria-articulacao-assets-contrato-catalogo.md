# Task 408 - Memória articulação: assets, contrato e catálogo

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end (tipos de categoria, se necessário)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/components/schemas/MemoryGameConfig`
- `contracts/openapi.yaml#/components/schemas/MemoryGameCardConfig`
- `contracts/openapi.yaml#/components/schemas/ContentCategory`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 034 - Jogo da memória de articulação
- `tasks/slices/034-jogo-memoria-articulacao.md`

## Resultado da execucao

- Print copiado para `design-system/front/prints/jogo-memoria-articulacao-modo-medio.png`
- 16 cartas + capas locais em `jogo_memoria_articulacao/`
- 19 assets publicados no S3 sob `dev/games/memoria_articulacao/`
- Schema da carta com `instruction` / `requiresMaterial`; `articulatorio` no `ContentCategory` do OpenAPI
- Bootstrap cria conteúdo `Jogo da memória — Articulação` (`category: articulatorio`, `difficulty: medio`)
- `findByGameType` / `upsertDefaultGame` passam a considerar categoria
- `STORAGE_BUCKET_MAP.md` atualizado

## Contexto utilizado

- Slice 034, print, memory assets/bootstrap existentes, OpenAPI, STORAGE_BUCKET_MAP

## Handoff

- `.agents/state/handoffs/TASK-408.md`

## Arquivos alterados

- ver handoff 408

## Validacoes executadas

- upload S3 ok (19 arquivos)
- `contents-catalog-bootstrap.service.spec.ts` pass

## Pendencias pos-task

- Task 409 (prévia + runtime com prompt)
- Task 410 (capas dedicadas / polish)

## Status final

done
