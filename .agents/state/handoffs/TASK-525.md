# Handoff — Task 525

## Identificador

TASK-525

## Título

Ofensiva mobile: acender fogo com streak ativo

## Slice vertical

`tasks/slices/008-trilhas-semanais-evolucao.md`

## Status final

done

## Decisões preservadas

- Fogo aceso (`fire.png`) quando `streakDays > 0`
- Fogo apagado (`fire-off.png`) quando `streakDays === 0`
- Contagem continua exigindo dia 100% concluído; hoje incompleto não entra na conta, mas não apaga o fogo da ofensiva já acumulada

## Contexto mínimo lido

- backlog + slice 008 + esta task

## Contexto sob demanda carregado

- `computeTrailStreak` + testes + `TrailStreakBadge`

## Arquivos alterados

- `mobile/src/features/trail/utils/computeTrailStreak.ts`
- `mobile/src/features/trail/utils/computeTrailStreak.test.ts`
- `mobile/src/features/trail/components/TrailStreakBadge.tsx`

## Validações executadas

- jest `computeTrailStreak.test.ts` — ok

## Pendências

- smoke visual no Expo

## Próxima ação sugerida

- Abrir Atividades com ofensiva > 0 e confirmar foguinho colorido

## Próximo contexto recomendado

- apenas `TrailStreakBadge` / `computeTrailStreak` se precisar ajustar visual dos assets

## Contexto que não deve ser carregado

- API de progress, design-system web, jogos
