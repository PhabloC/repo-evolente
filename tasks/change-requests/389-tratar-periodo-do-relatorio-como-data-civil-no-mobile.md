# Task 389 - Tratar período do relatório como data civil no mobile

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

- `contracts/openapi.yaml#/components/schemas/EvolutionReport` (`periodFrom` e `periodTo` com `format: date`)

## Modo de execução

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referência visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

correção funcional de exibição, sem mudança de layout

### Fonte primaria visual

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`

## Objetivo

Exibir o período do relatório com o dia informado pelo profissional, sem deslocamento de fuso na tela mobile do responsável.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Formatação do período | `mobile/src/features/shell/screens/GuardianReportsScreen.tsx` | corrigir o parse das datas civis | sim |
| Tipo do dado no contrato | `contracts/openapi.yaml#/components/schemas/EvolutionReport` | confirmar `format: date` em `periodFrom`/`periodTo` | sim |
| Serialização no backend | `backend/src/modules/reports/entities/evolution-report.entity.ts` | confirmar que a coluna `date` chega como `YYYY-MM-DD` | sim |
| Padrão existente no app | `mobile/src/features/profile/utils/formatProfile.ts` | conferir como o app já formata datas civis | não |

## Orçamento de contexto

- baixo
- estratégia: um utilitário compartilhado de data civil e o ajuste pontual na tela de relatórios

## Critérios de conclusão

- [x] `periodFrom` e `periodTo` deixam de ser interpretados como UTC
- [x] datas com hora (`sharedAt`/`createdAt`) continuam convertidas para o horário local
- [x] regressão coberta por teste automatizado
- [x] `npm run lint` executado nos arquivos alterados
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Origem

- comentário de code review (`P2 MÉDIO`) apontando que `new Date('YYYY-MM-DD')` é lido como UTC e exibe o dia anterior nos fusos brasileiros

## Resultado da execucao

- criado utilitário compartilhado de data civil, montando a data a partir dos componentes `YYYY-MM-DD` em horário local
- `formatDateLabel` da tela de relatórios passou a usar o utilitário quando o valor é data civil e manteve `new Date` apenas para timestamps completos
- período do relatório passou a exibir o mesmo dia informado no filtro do profissional em fusos negativos
- cobertura adicionada para o utilitário
- na Task 390 o utilitário foi renomeado para `mobile/src/shared/utils/civilDate.ts`, expondo `parseCivilDate` e `parseDisplayDate`

## Observacao levantada

- o agrupamento mensal da mesma tela derivava a chave do mês fatiando a string UTC (`sortDate.slice(0, 7)`) enquanto o rótulo usava `toLocaleDateString` em horário local; em relatórios compartilhados na virada do mês isso podia gerar rótulo e chave divergentes
- por alterar comportamento de agrupamento visível ao usuário, virou task própria: Task 390

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 011
- contexto sob demanda: tela de relatórios mobile, `contracts/openapi.yaml` (schema `EvolutionReport`), entidade de relatório no backend, `mobile/src/features/profile/utils/formatProfile.ts`
- contexto evitado: front-end web e design system, porque a correção é de parsing no cliente mobile

## Handoff

- `.agents/state/handoffs/TASK-389.md`

## Arquivos alterados

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/shared/utils/civilDate.ts` (criado como `formatCivilDate.ts` e renomeado na Task 390)
- `mobile/src/shared/utils/civilDate.test.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npx eslint` nos arquivos alterados
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Pendencias pos-task

- nenhuma; o agrupamento mensal foi tratado na Task 390

## Status final

done
