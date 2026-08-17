# Task 476 - Quebra-cabeça: artes novas para níveis 6–10

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- (assets locais + S3)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem mudança de schema (somente assets e sceneId)

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/038-quebra-cabeca.md`

## Objetivo

Criar 5 artes novas (`round_6`–`round_10`) no estilo cartoon infantil das cenas existentes e apontar cada nível 6–10 para a própria cena (sem reuso).

## Contexto mínimo

- Task 475 / handoff TASK-475
- `jigsaw-game-assets.ts`
- pasta `jogo_quebra_cabeca/rounds/`

## Orçamento de contexto

- risco: baixo

## Criterios de aceite

- [x] 5 pastas `round_6`…`round_10` com `full.webp`
- [x] `sceneId` único por nível 6–10
- [x] Upload S3 (57 assets no total do script)
- [x] Handoff gerado

## Resultado da execucao

Cenas novas: parque (coelho), fazenda (vaca), mar (peixe), espaço (astronauta), floresta (raposa). Níveis 6–10 apontam para `round_6`…`round_10`.

## Handoff

- `.agents/state/handoffs/TASK-476.md`

## Arquivos alterados

- `jogo_quebra_cabeca/rounds/round_6/full.webp`
- `jogo_quebra_cabeca/rounds/round_7/full.webp`
- `jogo_quebra_cabeca/rounds/round_8/full.webp`
- `jogo_quebra_cabeca/rounds/round_9/full.webp`
- `jogo_quebra_cabeca/rounds/round_10/full.webp`
- `backend/src/modules/contents/jigsaw-game-assets.ts`
- `tasks/slices/038-quebra-cabeca.md`
- `tasks/000-index.md`

## Validacoes executadas

- Conversão 1024×1024 webp
- Upload S3 via `scripts/upload-jigsaw-assets.mjs` (57 arquivos)

## Pendencias pos-task

- Reiniciar backend para refresh das URLs no catálogo

## Status final

done
