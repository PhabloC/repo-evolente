# Handoff — Task 475

## Identificador

- task: 475
- título: Quebra-cabeça: 10 níveis com dificuldade progressiva
- slice: 038
- status final: done

## Decisões

- 10 rodadas: 4× fácil 3×3, 3× médio 4×4, 3× difícil 5×5
- Campo opcional `difficulty`: `facil` | `medio` | `dificil`
- Reuso das 5 cenas via `sceneId` (sem arte nova)
- Peças em grades > 3×3 usam `full.webp` (UI já clipa pela grade)
- Bootstrap usa template como fonte da estrutura (não só merge do `current`)

## Contexto utilizado

- Task 475, slice 038, handoff 417
- `jigsaw-game-assets.ts`, openapi `JigsawRound`, preview web e renderer mobile

## Arquivos alterados

- `backend/src/modules/contents/jigsaw-game-assets.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `contracts/openapi.yaml`
- `front-end` + `mobile` types/parsers/UI jigsaw
- task/slice/index/handoff

## Validações

- `contents-catalog-bootstrap.service.spec.ts` PASS (10 rounds)

## Pendências

- Reiniciar backend para refresh do catálogo no banco local
- Validar prévia web nos níveis 5–10 (grades 4×4 e 5×5)

## Próxima ação

Abrir Quebra-cabeça na biblioteca e percorrer um nível fácil, um médio e um difícil.

## Contexto que não carregar

- design-system completo, outros jogos, Slice 034 memória
