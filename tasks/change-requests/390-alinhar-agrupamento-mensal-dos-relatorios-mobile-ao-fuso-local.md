# Task 390 - Alinhar agrupamento mensal dos relatórios mobile ao fuso local

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/components/schemas/EvolutionReport` (`sharedAt` e `createdAt` com `format: date-time`)

## Modo de execução

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referência visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

correção funcional de agrupamento, sem mudança de layout

### Fonte primaria visual

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`

## Objetivo

Fazer a chave e o rótulo do agrupamento mensal da tela de relatórios saírem da mesma data local, evitando divergência na virada do mês.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-389.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Agrupamento por mês | `mobile/src/features/shell/screens/GuardianReportsScreen.tsx` | alinhar chave e rótulo do grupo | sim |
| Parse de datas | `mobile/src/shared/utils/civilDate.ts` | reaproveitar o parse criado na Task 389 | sim |

## Orçamento de contexto

- baixo
- estratégia: reaproveitar o utilitário de data da Task 389 e ajustar apenas a derivação da chave do mês

## Critérios de conclusão

- [x] chave do mês deixa de ser fatiada da string UTC
- [x] chave e rótulo do grupo saem da mesma data local
- [x] datas inválidas continuam agrupadas em "Outros relatórios" e vão para o fim da lista
- [x] `npm run lint` executado nos arquivos alterados
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Origem

- observação registrada na Task 389 durante a correção do período do relatório

## Resultado da execucao

- o utilitário da Task 389 foi renomeado para `mobile/src/shared/utils/civilDate.ts` e passou a expor `parseCivilDate` e `parseDisplayDate`, que aceita tanto data civil quanto timestamp e sempre devolve data no fuso do dispositivo
- `formatDateLabel`, `formatMonthLabel` e a nova `resolveMonthKey` passaram a usar `parseDisplayDate`, então a data exibida e a data que define o grupo são a mesma
- a chave do mês passou a ser derivada de `getFullYear`/`getMonth` em vez de `sortDate.slice(0, 7)`
- datas não parseáveis usam a chave `0000-00`, que mantém o grupo "Outros relatórios" no fim da ordenação decrescente
- testes do utilitário atualizados para cobrir data civil, timestamp e valor inválido

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 011, handoff `TASK-389`
- contexto sob demanda: `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`, `mobile/src/shared/utils/civilDate.ts`
- contexto evitado: backend, front-end web e design system, porque a correção é de apresentação no cliente mobile

## Handoff

- `.agents/state/handoffs/TASK-390.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/shared/utils/civilDate.ts`
- `mobile/src/shared/utils/civilDate.test.ts`
- `tasks/change-requests/389-tratar-periodo-do-relatorio-como-data-civil-no-mobile.md` e `.agents/state/handoffs/TASK-389.md` (atualizados pelo rename do utilitário)
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/screens/GuardianReportsScreen.tsx src/shared/utils/civilDate.ts src/shared/utils/civilDate.test.ts`
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Pendencias pos-task

- o warning `react-hooks/exhaustive-deps` sobre `reports` na mesma tela é preexistente e segue fora do escopo

## Status final

done
