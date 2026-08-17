# Task 180 - Capa do jogo Escreva a letra no bucket

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

- `contracts/openapi.yaml#/components/schemas/AlphabetGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

### Identificador do slice

Slice 030 - Escrita guiada de letras

### Arquivo do slice

- `tasks/slices/030-escrita-guiada-de-letras.md`

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| asset local | `games/escreva_letra/capa_escreva_letra.webp` | upload | sim |
| bootstrap | `contents-catalog-bootstrap.service.ts` | coverUrl | sim |
| storage | `STORAGE_BUCKET_MAP.md` | documentação | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- capa em `{prefix}/games/escreva_letra/capa_escreva_letra.webp`
- bootstrap publica `coverUrl` no jogo Escreva a letra
- card da biblioteca usa a capa

## Dependencias

- Task 169
- Task 174

## Resultado da execucao

- Script de upload da capa criado e executado
- Bootstrap anexa `coverUrl` em criação e em jogos existentes sem capa
- Contrato, mapa do bucket e demo mobile atualizados

## Arquivos alterados

- `backend/src/modules/contents/alphabet-game-assets.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/scripts/upload-escreva-letra-cover.mjs`
- `backend/package.json`
- `contracts/openapi.yaml`
- `STORAGE_BUCKET_MAP.md`
- `mobile/src/features/trail/services/trailService.ts`
- `tasks/change-requests/180-capa-jogo-escreva-a-letra-no-bucket.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-180.md`

## Validacoes executadas

- `npm run upload:escreva-letra-cover`
- `npm test -- contents-catalog-bootstrap.service.spec.ts`

## Pendencias pos-task

- reiniciar backend para o bootstrap anexar a capa no banco local, se ainda nao refletir

## Status final

done
