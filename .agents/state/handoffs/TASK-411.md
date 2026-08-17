# Handoff — Task 411

## Identificador

- task: 411
- slice: 034
- status final: done

## Decisões

- Unicidade de jogos default: `(game_type, category)`, não só `game_type`
- Permite `memory` + `memoria` e `memory` + `articulatorio`

## Arquivos

- `backend/src/database/migrations/1840000000000-ReplaceContentsGameTypeUniqueWithCategory.ts`
- `backend/src/modules/contents/entities/content.entity.ts`

## Validações

- migration:run ok

## Próxima ação

Reiniciar `npm run start:dev` para o bootstrap criar o jogo de articulação.
