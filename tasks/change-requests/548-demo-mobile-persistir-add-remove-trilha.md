# Task 548 - Demo mobile: persistir add/remove na trilha

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Contrato

- nao se aplica (ramo `EXPO_PUBLIC_USE_DEMO_DATA`)

## Modo de execucao

single-stack

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- comportamento do modo demo; sem alteração visual

## Origem da solicitacao

Code review em `ajustes_mobile.md` item 1: com demo data, `replaceWeekItems` ignora `items` e devolve `demoDayTrail`.

## Objetivo

No modo demo, adicionar/remover atividades e esvaziar/sugerir a semana devem sobreviver à invalidação do React Query.

## Escopo

- Estado demo mutável em `trailService.ts`
- `getTodayTrail`, `replaceWeekItems`, `createEmptyWeek`, `suggestFromAnamnese` e `completeActivity` reutilizam esse estado

## Fora de escopo

- API real
- UI da trilha
- Persistência em disco

## Slice vertical

### Identificador do slice

Slice 047 - Trilha self-serve do responsável no mobile

### Arquivo do slice

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

### Objetivo de negocio

Permitir que o responsável monte e personalize a trilha no mobile.

### Entrega verificavel do slice

Em demo, add/remove não revertem após o refetch.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Implementação | `mobile/src/features/trail/services/trailService.ts` | ao corrigir o ramo demo | sim |
| Hooks | `mobile/src/features/trail/hooks/useTrailToday.ts` | se a invalidação precisar mudar | nao |
| Contrato | `contracts/openapi.yaml` | não — ramo demo local | nao |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 1
- Risco de contexto excessivo: baixo
- Estratégia: só o service demo da trilha

## Dependencias

- Task 502 (done)

## Criterios de conclusao

- Add/remove em demo persiste após `invalidateQueries` de `['trail','today']`
- `createEmptyWeek` demo permanece vazia no refetch
- Sem mudança no caminho da API real

## Instrucoes de implementacao

- Manter um clone mutável da trilha demo
- `replaceWeekItems` reconstrói `activities` a partir de `items` e do catálogo demo
- `getTodayTrail` demo devolve o estado atual, não o snapshot original

## Validacao esperada

- Leitura do fluxo add → invalidate → getTodayTrail
- Lint do arquivo alterado

## Entregaveis esperados

- Service demo mutável
- Task, índice, slice e handoff

## Resultado da execucao

- mobile: `trailService` passa a manter `demoTrailState` mutável
- `replaceWeekItems` demo reconstrói atividades a partir de `items`
- `getTodayTrail` demo devolve o estado atual; empty/suggest/complete também persistem
- Slice 047 permanece done
- Sem contrato (ramo `EXPO_PUBLIC_USE_DEMO_DATA`)

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 047

### Contexto sob demanda carregado

- `trailService.ts` e `useTrailToday.ts` — invalidação restaura via `getTodayTrail`

### Contexto não carregado

- `contracts/openapi.yaml`, `design-system/mobile/` — não se aplicam

## Handoff

- `.agents/state/handoffs/TASK-548.md`
- Próximo contexto: smoke com `EXPO_PUBLIC_USE_DEMO_DATA=true`

## Arquivos alterados

- `mobile/src/features/trail/services/trailService.ts`
- `tasks/change-requests/548-demo-mobile-persistir-add-remove-trilha.md`
- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`
- `tasks/000-index.md`

## Validacoes executadas

- Leitura: add/remove → invalidate → snapshot do estado mutável
- eslint `trailService.ts`: só warnings preexistentes (imports duplicados, `Array<T>`)

## Pendencias pos-task

- Smoke manual no app em modo demo: adicionar/remover atividade e confirmar que a lista não reverte

## Status final

done
