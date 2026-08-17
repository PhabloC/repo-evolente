# Handoff - Task 221

## Task

- identificador: 221
- título: Trilha: dias da semana em accordion
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010
- objetivo de negócio: trilha semanal do responsável navegável por dia
- entrega verificável: accordion Seg–Dom com atividades ao expandir

## Decisões preservadas

- decisão: um dia expandido por vez; hoje aberto por padrão
- motivo: foco no dia atual sem esconder a semana
- impacto: `expandedWeekday` inicia com `getIsoWeekday()`

- decisão: `adaptDayTrail` sem `weekday` retorna a semana inteira
- motivo: UI precisa agrupar por dia
- impacto: serviço deixa de filtrar só o dia atual

## Contexto utilizado

### Contexto mínimo lido

- Task 221
- `TrailTodayScreen.tsx`, `adaptDayTrail.ts`, `trailService.ts`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `trail/screens/styles.ts` | estilos accordion | headers/conteúdo |
| `trail/utils/week.ts` | labels ISO | Seg–Dom |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| OpenAPI / backend | fora de escopo |
| front-end / next-js | task mobile |

## Resultado por stack

- mobile: accordion semanal na trilha
- front-end / next-js / backend: n/a

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/trail/adapters/adaptDayTrail.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `tasks/change-requests/221-trilha-dias-semana-accordion-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-221.md`

## Validações executadas

- `npm run typecheck` (mobile): ok
- `npm test -- --testPathPattern=adaptDayTrail`: ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente no app (aba Atividades)

## Próximo contexto recomendado

- `TrailTodayScreen.tsx` se houver ajuste de UX do accordion

## Contexto que não deve ser carregado na próxima etapa

- requirements/contracts completos — mudança só de UI/dados da trilha mobile
