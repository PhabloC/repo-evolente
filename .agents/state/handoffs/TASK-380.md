# Handoff - Task 380

## Task

- identificador: 380
- título: Mover ações de jogo e vídeo para o corpo da tela mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas semanais e evolução

## Decisões preservadas

- jogo e vídeo não exibem mais a barra superior com seta/check
- as ações `Concluir atividade` e `Voltar` foram movidas para dentro da página nesses dois fluxos
- o fluxo de áudio mantém a barra superior anterior

## Contexto utilizado

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`

## Arquivos alterados

- tela, estilos, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npm run typecheck` — sem diagnósticos

## Pendências ou bloqueios

- nenhuma

## Próximo contexto recomendado

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
