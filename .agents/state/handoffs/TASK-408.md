# Handoff — Task 408

## Identificador

- task: 408
- título: Memória articulação: assets, contrato e catálogo
- slice: Slice 034 - Jogo da memória de articulação
- status final: done

## Decisões preservadas

- Reutilizar `gameType: memory` (sem novo gameType)
- Conteúdo separado no catálogo com `category: articulatorio` e `difficulty: medio`
- Lookup de default games passou a ser `gameType + category` para permitir dois conteúdos `memory`
- Cartas com `instruction` e `requiresMaterial` opcionais
- Assets em prefixo `games/memoria_articulacao/` (não misturar com memória cognitivo)
- 16 cartas do modo médio extraídas do print; capa = print completo; verso reusa `capinha_jogo`

## Contexto mínimo lido

- AGENTS.md, GUIDE.md, context-map, 000-index, task 408, slice 034

## Contexto sob demanda carregado

- print + crops em `jogo_memoria_articulacao/`
- memory-game-assets / bootstrap / openapi MemoryGame*
- STORAGE_BUCKET_MAP.md
- script upload memória cognitivo como modelo

## Arquivos alterados

- `tasks/slices/034-jogo-memoria-articulacao.md`
- `tasks/change-requests/408-*.md`, `409-*.md`, `410-*.md`
- `design-system/front/prints/jogo-memoria-articulacao-modo-medio.png`
- `jogo_memoria_articulacao/**`
- `backend/src/modules/contents/memory-articulation-game-assets.ts`
- bootstrap, repositories, entity, contents.service, specs
- `contracts/openapi.yaml`
- `backend/scripts/upload-memory-articulation-assets.mjs`
- `STORAGE_BUCKET_MAP.md`
- tipos front/mobile + parse memoryGame

## Validações executadas

- Upload S3: 19 assets (`dev/games/memoria_articulacao/...`)
- `contents-catalog-bootstrap.service.spec.ts` (após ajuste length 5)

## Pendências

- Task 409: prévia web + prompt pós-par no mobile
- Task 410: capas dedicadas refinadas + polish do prompt
- Recortes das cartas ainda vêm do print composto (qualidade WhatsApp); trocar por artes individuais se necessário

## Próxima ação sugerida

Executar Task 409.

## Próximo contexto recomendado

- handoff 408
- `front-end/src/pages/Main/Library/` (preview memory)
- `mobile/src/features/games/` (renderer memory)
- print modo médio

## Não carregar

- requirements inteiros
- design-system mobile completo
- jogos alphabet/word-search além do padrão de preview já existente
