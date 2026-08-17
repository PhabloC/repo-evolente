# Handoff - Task 367

## Task

- identificador: 367
- título: Voltar check.webp para cover na trilha e avisos mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 008

## Decisões preservadas

- decisão: restaurar `cover` apenas nos dois usos do `check.webp`
- motivo: pedido explícito do usuário
- impacto: inset e borda arredondada foram preservados

## Contexto utilizado

- `TrailTodayScreen.tsx`
- `ResponsavelNotificationsScreen.tsx`
- handoff `TASK-366`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- task/index/slice/handoff 367

## Validações executadas

- `cd mobile && npm run lint`
- `cd mobile && npm run typecheck`
- `cd mobile && npm run test`

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-367.md`
