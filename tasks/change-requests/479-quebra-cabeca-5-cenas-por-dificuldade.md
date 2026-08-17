# Task 479 - Quebra-cabeça: 5 cenas por dificuldade

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `JigsawGameConfig.rounds` maxItems 20

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/038-quebra-cabeca.md`

## Objetivo

Ter 5 cenas em cada dificuldade (fácil/médio/difícil = 15 rodadas), com artes novas para as cenas faltantes.

## Criterios de aceite

- [x] 5 cenas fácil, 5 médio, 5 difícil
- [x] 5 artes novas em `round_11`…`round_15`
- [x] Upload S3 (71 assets)
- [x] Contrato/validação aceitam até 20 rounds
- [x] Spec bootstrap atualizado

## Resultado da execucao

Novas cenas: coruja (fácil), panda e trem (médio), dinossauro e pinguim (difícil). Total 15 rodadas.

## Handoff

- `.agents/state/handoffs/TASK-479.md`

## Arquivos alterados

- `jogo_quebra_cabeca/rounds/round_11`…`round_15`
- `backend/src/modules/contents/jigsaw-game-assets.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `contracts/openapi.yaml`

## Status final

done
