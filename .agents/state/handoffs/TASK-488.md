# Handoff - Task 488

## Task

- identificador: 488
- título: Hardening do bootstrap e dos assets de jogos no backend
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- Slice 006

## Decisões preservadas

- builders de jogo agora usam a configuração persistida como fonte principal
- entradas ausentes do template são apenas adicionadas, não substituem edições
- scripts de upload passaram a respeitar extensão e MIME do arquivo real

## Contexto efetivamente usado

- task 488, índice, slice 006
- handoff `TASK-486`
- builders `fluency`, `dialogue`, `emotions`, `jigsaw`
- scripts de upload dos jogos

## Arquivos alterados

- `backend/src/modules/contents/fluency-game-assets.ts`
- `backend/src/modules/contents/dialogue-game-assets.ts`
- `backend/src/modules/contents/emotions-game-assets.ts`
- `backend/src/modules/contents/jigsaw-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `backend/scripts/upload-fluency-assets.mjs`
- `backend/scripts/upload-dialogue-assets.mjs`
- `backend/scripts/upload-emotions-assets.mjs`

## Validações executadas

- suíte focada de testes backend — ok
- eslint focado dos arquivos alterados — ok

## Pendências ou bloqueios

- sem conversão automática para WebP; o pipeline atual apenas publica corretamente o tipo/extensão existente

## Próxima ação sugerida

- só reabrir esse contexto se surgir necessidade de normalização automática de imagens

## Próximo contexto recomendado

- task 488
- `contents/*game-assets.ts`
- scripts `upload-*.mjs`

## Contexto que não deve ser carregado na próxima etapa

- Asaas
- admin mobile
