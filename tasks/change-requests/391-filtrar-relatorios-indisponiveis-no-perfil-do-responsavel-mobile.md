# Task 391 - Filtrar relatórios indisponíveis no perfil do responsável mobile

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

- `contracts/openapi.yaml#/components/schemas/EvolutionReport` (`availableToGuardian`)

## Modo de execução

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referência visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

correção funcional de dados exibidos, sem mudança de layout

### Fonte primaria visual

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Objetivo

Garantir que o resumo de relatórios do perfil do responsável considere apenas relatórios disponibilizados, igual à tela de lista.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-390.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Resumo do perfil | `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx` | identificar contagem, último envio e metadados sem filtro | sim |
| Origem dos dados | `mobile/src/features/reports/hooks/useGuardianReports.ts` | centralizar o filtro no ponto compartilhado | sim |
| Tela de lista | `mobile/src/features/shell/screens/GuardianReportsScreen.tsx` | remover o filtro duplicado | sim |
| Regra do servidor | `backend/src/modules/reports/reports.service.ts` | confirmar o comportamento atual da API para o responsável | sim |

## Orçamento de contexto

- baixo
- estratégia: um seletor único no hook de relatórios, sem tocar em backend nem contrato

## Critérios de conclusão

- [x] perfil e lista de relatórios passam a usar o mesmo conjunto de dados
- [x] o filtro deixa de ser duplicado em tela
- [x] regra coberta por teste automatizado
- [x] `npm run lint` executado nos arquivos alterados
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Origem

- comentário de code review (`P2 MÉDIO`) apontando que o array sem filtro alimentava badge, último envio e detalhes do perfil, divergindo da tela de relatórios

## Achado da investigacao

- hoje `GET /reports` já filtra por `availableToGuardian` quando o usuário é `responsavel` (`reports.service.ts` usa `listAvailableByPatientIds`), então não há divergência em produção no momento
- ainda assim o cliente estava inconsistente: a tela de lista filtrava e o perfil não, ou seja, as duas telas discordariam se a API passasse a devolver relatórios não disponibilizados
- por isso a correção foi tratada como consistência de cliente, e não como bug reproduzível hoje

## Resultado da execucao

- criado `mobile/src/features/reports/utils/selectAvailableReports.ts`, que mantém apenas relatórios com `availableToGuardian`
- `useGuardianReportsQuery` passou a aplicar esse seletor via `select`, então perfil e lista consomem exatamente o mesmo conjunto
- o filtro local duplicado da tela de relatórios foi removido
- o seletor ficou em módulo próprio, com identidade estável fora do componente, para não recalcular a cada render
- cobertura adicionada em `mobile/src/features/reports/utils/selectAvailableReports.test.ts`

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 011, handoff `TASK-390`
- contexto sob demanda: perfil do responsável, hook de relatórios, tela de relatórios e `backend/src/modules/reports/reports.service.ts`
- contexto evitado: contrato e front-end web, porque a regra do servidor já estava correta e nada mudou na API

## Handoff

- `.agents/state/handoffs/TASK-391.md`

## Arquivos alterados

- `mobile/src/features/reports/hooks/useGuardianReports.ts`
- `mobile/src/features/reports/utils/selectAvailableReports.ts`
- `mobile/src/features/reports/utils/selectAvailableReports.test.ts`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npx eslint` nos arquivos alterados
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Pendencias pos-task

- o warning `react-hooks/exhaustive-deps` sobre `reports` na tela de relatórios é preexistente e segue fora do escopo

## Status final

done
