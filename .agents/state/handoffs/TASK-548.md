# Handoff - Task 548

## Task

- identificador: TASK-548
- título: Demo mobile: persistir add/remove na trilha
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 047
- objetivo de negócio: responsável montar a trilha no mobile
- entrega verificável: add/remove em demo sobrevivem ao refetch

## Decisões preservadas

- decisão: estado mutável `demoTrailState` em memória
- motivo: `replaceWeekItems` demo ignorava `items` e `getTodayTrail` clonava o snapshot original
- impacto: só `EXPO_PUBLIC_USE_DEMO_DATA=true`; API real inalterada

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 548, slice 047

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `trailService.ts` | demo ignora items | persistir mutações |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| contrato OpenAPI | ramo demo local |

## Arquivos alterados

- `mobile/src/features/trail/services/trailService.ts`

## Validações executadas

- validação: fluxo add/remove → invalidate → snapshot mutável

## Pendências ou bloqueios

- smoke manual em modo demo

## Próxima ação sugerida

- Task 549/550 já executadas neste review

## Próximo contexto recomendado

- `trailService.ts` ramo `env.useDemoData`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `contracts/openapi.yaml`
- motivo: correção só do mock demo
