# Handoff - Task 264

## Status

done

## Decisões

- o asset `bell-off.webp` foi aplicado apenas no estado de avisos limpos da tela
- o estado “Nenhum aviso ainda” manteve o ícone anterior
- a mudança ficou restrita à tela de avisos

## Contexto utilizado

- `tasks/change-requests/264-usar-bell-off-no-estado-de-avisos-limpos-mobile.md`
- `.agents/state/handoffs/TASK-262.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/assets/bell-off.webp`

## Arquivos alterados

- `tasks/change-requests/264-usar-bell-off-no-estado-de-avisos-limpos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-264.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `cd mobile && npm run typecheck`

## Pendencias

- `npm run lint` global do mobile continua com débitos antigos fora deste escopo

## Proximo contexto recomendado

- reutilizar esta task se outros estados vazios de avisos também passarem a usar assets dedicados
