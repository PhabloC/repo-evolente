# Handoff - Task 389

## Task

- identificador: 389
- título: Tratar período do relatório como data civil no mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao

## Decisões preservadas

- datas civis (`YYYY-MM-DD`) são montadas pelos componentes em horário local; timestamps completos continuam com `new Date` para respeitar o fuso do dispositivo
- a lógica virou utilitário compartilhado (`mobile/src/shared/utils/civilDate.ts`, renomeado na Task 390) para poder ser testada, já que o projeto não tem teste de componente
- o restante do app já tratava datas civis por string (`formatProfile.formatBirthDate`); a tela de relatórios era a exceção

## Contexto utilizado

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `contracts/openapi.yaml` (schema `EvolutionReport`)
- `backend/src/modules/reports/entities/evolution-report.entity.ts`
- `mobile/src/features/profile/utils/formatProfile.ts`

## Arquivos alterados

- tela de relatórios mobile, novo utilitário e seu teste, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npx eslint` nos arquivos alterados
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Pendências ou bloqueios

- nenhuma; a divergência do agrupamento mensal virou a Task 390

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-390.md`
