# Handoff - Task 381

## Task

- identificador: 381
- título: Remover faixa superior residual em jogo e vídeo mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas semanais e evolução

## Decisões preservadas

- jogo e vídeo usam um `contentStyle` próprio sem `paddingTop`
- áudio mantém o `contentStyle` anterior com respiro superior
- a correção ficou local na `TrailActivityScreen`, sem alterar a `Screen` compartilhada

## Contexto utilizado

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/shared/components/Screen/styles.ts`

## Arquivos alterados

- tela, estilos, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npm run typecheck` — sem diagnósticos

## Pendências ou bloqueios

- nenhuma

## Próximo contexto recomendado

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
