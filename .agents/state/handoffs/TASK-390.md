# Handoff - Task 390

## Task

- identificador: 390
- título: Alinhar agrupamento mensal dos relatórios mobile ao fuso local
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao

## Decisões preservadas

- o utilitário de data virou `mobile/src/shared/utils/civilDate.ts`, com `parseCivilDate` (só `YYYY-MM-DD`) e `parseDisplayDate` (data civil ou timestamp, sempre no fuso do dispositivo)
- a tela de relatórios formata e agrupa a partir da mesma função de parse, então rótulo e chave do mês não podem mais divergir
- chave do mês passou a vir de `getFullYear`/`getMonth`; datas inválidas usam `0000-00` para o grupo "Outros relatórios" cair no fim da ordenação decrescente
- a ordenação continua por `key.localeCompare` decrescente, sem mudança de contrato ou de API

## Contexto utilizado

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/shared/utils/civilDate.ts`
- `.agents/state/handoffs/TASK-389.md`

## Arquivos alterados

- tela de relatórios mobile, utilitário de data e seu teste, docs da Task 389, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npx eslint` nos arquivos alterados
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Pendências ou bloqueios

- warning preexistente `react-hooks/exhaustive-deps` sobre `reports` na mesma tela

## Próximo contexto recomendado

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`, caso o warning de `useMemo` vire task de limpeza
