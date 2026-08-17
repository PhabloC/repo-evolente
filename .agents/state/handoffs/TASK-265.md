# Handoff - Task 265

## Status

done

## Decisões

- os assets locais da tela de avisos precisavam subir 4 níveis até `mobile/assets`
- o fix ficou restrito aos `require(...)` da tela de avisos

## Contexto utilizado

- `tasks/change-requests/265-corrigir-path-dos-assets-de-avisos-mobile.md`
- `.agents/state/handoffs/TASK-262.md`
- `.agents/state/handoffs/TASK-264.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Arquivos alterados

- `tasks/change-requests/265-corrigir-path-dos-assets-de-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-265.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/trail/screens/TrailTodayScreen.tsx`
- `cd mobile && npm run typecheck`

## Pendencias

- `npm run lint` global do mobile continua com débitos antigos fora deste escopo

## Proximo contexto recomendado

- reutilizar esta task se outros assets locais forem adicionados em telas sob `src/features/.../screens`
