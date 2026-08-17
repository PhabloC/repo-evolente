# Task 396 - Filtrar atividades planejadas por data no relatório

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem alteração; preserva `POST /reports`

## Modo de execução

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Objetivo

Calcular as atividades previstas do relatório pela data planejada de cada item, respeitando períodos que começam ou terminam no meio da semana.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-395.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Regra de período | `backend/src/modules/reports/reports.service.ts` | calcular a data planejada por item |
| Convenção semanal | `backend/src/modules/trails/utils/week.util.ts` | confirmar weekday ISO |
| Regressão | `backend/src/modules/reports/reports.service.spec.ts` | cobrir recorte parcial da semana |
| Padrões locais | `backend/docs/ai/` | orientar implementação e QA |

## Orçamento de contexto

- baixo
- alteração localizada no serviço e testes de relatórios

## Critérios de conclusão

- [x] item planejado é filtrado por `weekStartDate + weekday - 1`
- [x] período parcial inclui apenas os dias dentro do recorte
- [x] totais e taxa de adesão usam o denominador corrigido
- [x] regressão coberta por teste

## Resultado da execucao

- `scopedTrailItems` passou a filtrar cada item da trilha, em vez de incluir ou excluir a semana inteira.
- A data planejada é calculada com `addDays(parseISO(weekStartDate), weekday - 1)` e normalizada para `YYYY-MM-DD`.
- A comparação é feita entre datas civis, sem deslocamento de fuso.
- Weekdays inválidos são excluídos defensivamente.
- O teste cobre uma semana com itens na segunda, quarta e sexta e um período de terça a quinta; somente a quarta entra no total previsto.

## Contexto utilizado

- contexto mínimo: raiz, esta task, Slice 011 e handoff da Task 395
- contexto sob demanda: `reports.service.ts`, `reports.service.spec.ts`, `trails/utils/week.util.ts` e guias locais de backend
- contexto evitado: requirements, design systems, front-end e mobile, pois não houve mudança de contrato nem UI

## Handoff

- `.agents/state/handoffs/TASK-396.md`

## Arquivos alterados

- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- teste focado: 2 testes passaram
- testes unitários completos: 19 suítes e 87 testes passaram
- e2e: 1 suíte e 1 teste passaram
- build: passou
- lint dos arquivos alterados: passou
- lint global: bloqueado por 197 erros preexistentes de Prettier/line endings e `no-implied-eval` em outros arquivos

## Pendencias pos-task

- corrigir o passivo global de lint em task própria, sem misturá-lo a esta regra de relatório

## Status final

done
