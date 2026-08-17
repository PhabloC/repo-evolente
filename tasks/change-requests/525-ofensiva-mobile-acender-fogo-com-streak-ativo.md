# Task 525 - Ofensiva mobile: acender fogo com streak ativo

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

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- este arquivo

## Contexto sob demanda

- `mobile/src/features/trail/utils/computeTrailStreak.ts` (+ testes)
- `mobile/src/features/trail/components/TrailStreakBadge.tsx`
- Task 293 (ofensiva original)

## Orçamento de contexto

- baixo

## Objetivo

O foguinho da ofensiva no header de Atividades mostra o número de dias, mas permanece em `fire-off` enquanto o dia atual não estiver 100% concluído. Ajustar para acender (`fire.png`) sempre que a ofensiva estiver ativa (`streakDays > 0`), no estilo Duolingo — o fogo só apaga quando a sequência zera.

## Criterios de aceite

- [x] `isOnTrack === true` quando `streakDays > 0`
- [x] `isOnTrack === false` quando `streakDays === 0`
- [x] Contagem de dias (regra de dias 100% concluídos) inalterada
- [x] Testes unitários atualizados e passando

## Resultado da execucao

- `isOnTrack` passou a ser `streakDays > 0` (fogo aceso com ofensiva ativa, mesmo com o dia de hoje ainda pendente)
- Contagem de dias inalterada (hoje só entra na conta após 100% concluído)
- `TrailStreakBadge` remonta a imagem com `key` ao trocar on/off

## Contexto utilizado

- mínimo: backlog + slice 008 + esta task
- sob demanda: `computeTrailStreak` + badge + regra Task 293

## Handoff

- `.agents/state/handoffs/TASK-525.md`

## Arquivos alterados

- `mobile/src/features/trail/utils/computeTrailStreak.ts`
- `mobile/src/features/trail/utils/computeTrailStreak.test.ts`
- `mobile/src/features/trail/components/TrailStreakBadge.tsx`
- `tasks/change-requests/525-ofensiva-mobile-acender-fogo-com-streak-ativo.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-525.md`

## Validacoes executadas

- `npx jest src/features/trail/utils/computeTrailStreak.test.ts --no-coverage` — ok

## Pendencias pos-task

- Smoke visual no app: ofensiva > 0 com dia atual ainda pendente deve mostrar `fire.png`

## Status final

done
