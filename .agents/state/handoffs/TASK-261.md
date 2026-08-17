# Handoff - Task 261

## Status

done

## Decisões

- a limpeza de avisos deixou de ser estado local efêmero e passou a persistir em storage do app
- a tela usa query local para carregar ids dispensados e manter o comportamento após remontagem
- o escopo ficou restrito ao mobile, sem contrato novo e sem backend

## Contexto utilizado

- `tasks/change-requests/261-persistir-limpeza-de-avisos-mobile.md`
- `tasks/change-requests/260-limpar-avisos-na-tela-mobile.md`
- `.agents/state/handoffs/TASK-260.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/shared/storage/appStorage.ts`
- `mobile/src/features/notifications/storage/dismissedNotificationsStorage.ts`
- `mobile/src/features/notifications/storage/dismissedNotificationsStorage.test.ts`

## Arquivos alterados

- `tasks/change-requests/261-persistir-limpeza-de-avisos-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-261.md`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/notifications/storage/dismissedNotificationsStorage.ts`
- `mobile/src/features/notifications/storage/dismissedNotificationsStorage.test.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/screens/ResponsavelNotificationsScreen.tsx src/features/notifications/storage/dismissedNotificationsStorage.ts src/features/notifications/storage/dismissedNotificationsStorage.test.ts`
- `cd mobile && npm run typecheck`
- `cd mobile && npx jest src/features/notifications/storage/dismissedNotificationsStorage.test.ts --runInBand`

## Pendencias

- `npm run lint` global do mobile continua com débitos antigos fora deste escopo

## Proximo contexto recomendado

- reutilizar esta task se a central de avisos passar a precisar sincronizar a limpeza com backend ou perfil de usuário
