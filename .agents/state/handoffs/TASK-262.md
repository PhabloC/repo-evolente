# Handoff - Task 262

## Status

done

## Decisões

- a lista de avisos usa assets locais `bell.webp` e `check.webp` apenas nos cards de notificação
- `IconPill` passou a aceitar `imageSource` local com fallback para ícone vetorial
- hero e estado vazio de avisos permaneceram com a linguagem anterior

## Contexto utilizado

- `tasks/change-requests/262-usar-assets-bell-e-check-nos-avisos-mobile.md`
- `.agents/state/handoffs/TASK-261.md`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/assets/bell.webp`
- `mobile/assets/check.webp`

## Arquivos alterados

- `tasks/change-requests/262-usar-assets-bell-e-check-nos-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-262.md`
- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/shared/components/IconPill/index.tsx src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/trail/screens/TrailTodayScreen.tsx`
- `cd mobile && npm run typecheck`

## Pendencias

- `npm run lint` global do mobile continua com débitos antigos fora deste escopo

## Proximo contexto recomendado

- reutilizar esta task se outros cards de avisos passarem a usar assets locais dedicados
