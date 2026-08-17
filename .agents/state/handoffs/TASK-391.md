# Handoff - Task 391

## Task

- identificador: 391
- título: Filtrar relatórios indisponíveis no perfil do responsável mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao

## Decisões preservadas

- o filtro por `availableToGuardian` passou a viver em um único ponto: o `select` de `useGuardianReportsQuery`, consumido pelo perfil e pela tela de relatórios
- o seletor foi extraído para `mobile/src/features/reports/utils/selectAvailableReports.ts` com identidade estável em módulo, evitando recomputar a cada render e permitindo teste puro
- a tela de relatórios deixou de filtrar localmente, para não existirem duas regras concorrentes
- nada mudou no backend nem no contrato: `GET /reports` já filtra para o papel `responsavel`, então a correção é de consistência do cliente

## Contexto utilizado

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/reports/hooks/useGuardianReports.ts`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `backend/src/modules/reports/reports.service.ts`

## Arquivos alterados

- hook de relatórios, novo seletor e seu teste, tela de relatórios, task, slice, índice e handoff

## Validações executadas

- `cd mobile && npx eslint` nos arquivos alterados
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Pendências ou bloqueios

- warning preexistente `react-hooks/exhaustive-deps` sobre `reports` na tela de relatórios

## Próximo contexto recomendado

- `mobile/src/features/reports/hooks/useGuardianReports.ts`, caso alguma tela futura precise ver relatórios ainda não disponibilizados
