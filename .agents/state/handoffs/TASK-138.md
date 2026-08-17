# Handoff - Task 138

## Identificador

- Task 138 - Cachear SVGs dos heroes mobile
- `tasks/change-requests/138-cachear-svgs-dos-heroes-mobile.md`

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Status final

done

## Decisoes preservadas

- O cache foi implementado no bootstrap do app, nao por tela
- Os heroes usam `SvgXml` com XML ja em memoria e mantem `SvgUri` como fallback resiliente
- O escopo ficou restrito aos backgrounds SVG estaveis dos cards hero

## Contexto efetivamente usado

- Task 138, slice 022, handoff `TASK-137`, `AppGate`, cache compartilhado de SVG e componentes/telas dos heroes

## Arquivos alterados

- `mobile/src/app/AppGate.tsx`
- `mobile/src/shared/assets/heroBackgroundSvgCache.ts`
- `mobile/src/shared/components/CachedHeroBackgroundSvg.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok (11 suites, 22 testes)

## Pendencias

- Validar em dispositivo fisico/Expo Go a reducao do atraso perceptivel na troca de telas

## Proximo contexto recomendado

- `mobile/src/shared/assets/` e os heroes do responsavel
