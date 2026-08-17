# Handoff - Task 223

## Task

- 223 — done
- Capa do jogo no ícone da trilha mobile

## Decisão

- `IconPill` aceita `imageUri` opcional com fallback para o ícone Lucide
- Capa resolvida via `resolveTrailActivityCoverUrl` → `gameConfig.coverUrl`

## Arquivos

- `mobile/src/shared/components/IconPill/index.tsx`
- `mobile/src/shared/components/IconPill/styles.ts`
- `mobile/src/features/trail/utils/resolveTrailActivityCoverUrl.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
