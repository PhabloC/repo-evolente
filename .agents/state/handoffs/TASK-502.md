# Handoff - Task 502

## Task

- identificador: 502
- título: Mobile: UI trilha self-serve
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 047-trilha-self-serve-responsavel-mobile
- objetivo de negócio: empty + biblioteca + suggest + editor no modo dono
- entrega verificável: TrailTodayScreen modos + TrailLibraryScreen

## Decisões preservadas

- decisão: empty state só quando `canManage && !trailId` (semana sem trilha)
- decisão: dias futuros bloqueados só no modo execução (`lockFutureDays: !canManage`)
- decisão: biblioteca é stack screen, não nova aba

## Contexto utilizado

### Contexto mínimo lido

- Task 502 + slice 047
- `TrailTodayScreen`, `trailService`, hooks

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| canManage API | modo UI | dono vs execução |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| web front-end | fora do escopo |

## Resultado por stack

- mobile: TrailTodayScreen + TrailLibraryScreen + rotas + service mutations

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailLibraryScreen.tsx`
- `mobile/src/features/trail/hooks/useTrailToday.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `mobile/src/routes/params.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`

## Validações executadas

- typecheck mobile: erros pré-existentes; sem erros novos nas telas da trilha
- backend trails.spec: 8 passed (dependência)

## Pendências ou bloqueios

- migration 186 no DB local se create guardian falhar
- demo mode: createEmpty inválida e refetch pode repor demo cheia

## Próxima ação sugerida

- validar fluxo real sem vínculo (gerar / biblioteca / zerar) e com vínculo (só execução)

## Próximo contexto recomendado

- handoffs 500–502; não recarregar slice inteiro

## Contexto que não deve ser carregado na próxima etapa

- jogos / admin / Asaas
