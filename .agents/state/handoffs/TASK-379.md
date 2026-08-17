# Handoff - Task 379

## Task

- identificador: 379
- título: Mover descrição e objetivo para card abaixo do vídeo mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas semanais e evolução

## Decisões preservadas

- o vídeo agora mostra um card de detalhes logo abaixo do player
- o campo `therapeuticObjective` foi movido para esse card
- como não existe um campo de descrição dedicado no modelo da trilha, o card usa o `title` atual da atividade em `Descrição`

## Contexto utilizado

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/trail/types/trail.ts`

## Arquivos alterados

- tela, estilos, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npm run typecheck` — sem diagnósticos

## Pendências ou bloqueios

- descrição textual dedicada para vídeo exige expansão do modelo/contrato

## Próximo contexto recomendado

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
