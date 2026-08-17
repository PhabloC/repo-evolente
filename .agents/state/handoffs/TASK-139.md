# Handoff - Task 139

## Identificador

- Task 139 - Aplicar selo com icone nos heroes mobile
- `tasks/change-requests/139-aplicar-selo-com-icone-nos-heroes-mobile.md`

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Status final

done

## Decisoes preservadas

- O selo foi implementado como componente compartilhado para evitar variacoes entre telas
- O fundo do selo usa branco translúcido e borda suave para manter contraste no hero laranja
- As telas de atividades usam estrela; perfil usa usuarios; avisos usa sino; home usa sparkles

## Contexto efetivamente usado

- Task 139, slice 022, handoff `TASK-138`, componentes compartilhados e heroes do responsavel/trilha

## Arquivos alterados

- `mobile/src/shared/components/HeroEyebrowBadge/index.tsx`
- `mobile/src/shared/components/HeroEyebrowBadge/styles.ts`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok

## Pendencias

- Validar em dispositivo o peso visual do selo sobre cada ilustracao de fundo
