# Handoff - Task 382

## Task

- identificador: 382
- título: Propagar description do conteúdo para o vídeo mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas semanais e evolução

## Decisões preservadas

- o card de vídeo agora usa `content.description` quando disponível
- `therapeuticObjective` continua exclusivo para o objetivo
- `description` ficou opcional no tipo mobile para preservar compatibilidade dos fixtures locais, mas o adapter normaliza ausência para `null`
- o demo `Bico de Peixe` foi atualizado com a descrição correta e o objetivo esperado

## Contexto utilizado

- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/trail/adapters/adaptDayTrail.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Arquivos alterados

- tipos, adapter, service demo, tela, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npm run typecheck` — sem diagnósticos

## Pendências ou bloqueios

- nenhuma

## Próximo contexto recomendado

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
