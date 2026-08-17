# Handoff — Task 293

## Decisões

- Ofensiva no `rightAction` do `ShellScreenTopBar` da tela de Atividades.
- Em dia (`fire.png`): hoje sem pendência e nenhum dia anterior da semana incompleto.
- Fora do dia (`fire-off.png`): há atividade pendente hoje ou dia anterior incompleto.
- Contagem = dias consecutivos concluídos na semana atual; dias sem atividade são ignorados.
- Sem API nova: usa `day.activities` já carregados.

## Contexto usado

- Task 293
- TrailTodayScreen + ShellScreenTopBar
- assets `fire.png` / `fire-off.png`

## Arquivos alterados

- `mobile/src/features/trail/utils/computeTrailStreak.ts` (+ test)
- `mobile/src/features/trail/components/TrailStreakBadge/`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`

## Validações

- `npx jest src/features/trail/utils/computeTrailStreak.test.ts` — ok

## Pendências

- Contagem limitada à semana atual (sem histórico entre semanas).
- Assets têm fundo preto; se o visual incomodar, exportar PNG com transparência.

## Próximo contexto recomendado

- Se precisar streak entre semanas: API de evoluções históricas ou storage local.
