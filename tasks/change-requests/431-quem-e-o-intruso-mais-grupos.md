# Task 431 - Quem é o intruso: mais grupos e imagens

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

- `OddOneOutGameConfig` (sem mudança de schema)

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/041-quem-e-o-intruso.md`

## Objetivo

Ampliar o conteúdo do `odd-one-out` com mais rodadas e novas imagens no S3.

## Contexto mínimo

- Task 430 / handoff TASK-430
- `odd-one-out-game-assets.ts`
- pasta `jogo_quem_e_o_intruso/`

## Orçamento de contexto

- risco: baixo

## Criterios de aceite

- [x] Pelo menos 8 rodadas no bootstrap (9 rodadas)
- [x] Novos assets no bucket (36 arquivos)
- [x] Specs de bootstrap atualizados
- [x] Shuffle continua ao iniciar

## Resultado da execucao

Expandido de 4 para 9 grupos; 13 imagens novas + reuso de figuras do semáforo; upload S3 e refresh de config.

## Handoff

- `.agents/state/handoffs/TASK-431.md`

## Status final

done
