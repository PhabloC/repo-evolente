# Handoff - Task 124

## Identificador

- Task 124 - Aplicar linguagem visual do print nas demais telas mobile
- `tasks/change-requests/124-linguagem-visual-print-demais-telas-mobile.md`

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Status final

done

## Decisoes preservadas

- `shared/components/ScreenHeader` (eyebrow + titulo extrabold + descricao) e `shared/components/IconPill` (pastilha com tints orange/blue/pink/green/yellow/coral) sao os blocos padrao da linguagem interna do app
- Print `design-system/mobile/prints/home-responsavel-referencia.png` governa composicao; tokens Evolente governam cores
- Pills de status arredondadas (999) com `blueSoft`/`greenSoft`; token novo `greenSoft`
- Telas restilizadas sem mudanca de comportamento: Avisos, Perfil, TrailToday, TrailActivity, MasterHome, MasterPlaceholder, AdminHome, AdminUsers
- Atencao: `MasterShellNavigator` usa `AdminHomeScreen`/`AdminUsersScreen` (feature `admin`), nao `MasterHomeScreen`; correcao aplicada na propria task
- `ShellTabBar` e navigators intocados (restricao do usuario)

## Contexto efetivamente usado

- Task 124, slice 022, handoff TASK-123, print de referencia, tokens, CODE_STYLE/COMPONENT_REUSE, telas alvo shell/trail

## Arquivos alterados

- `mobile/src/shared/components/ScreenHeader/**` e `IconPill/**` (novos)
- `mobile/src/shared/theme/tokens.ts`
- `mobile/src/features/shell/screens/{ResponsavelNotificationsScreen,ResponsavelProfileScreen,MasterHomeScreen,MasterPlaceholderScreen,styles}.tsx/.ts`
- `mobile/src/features/trail/screens/{TrailTodayScreen,TrailActivityScreen,styles}.tsx/.ts`
- `mobile/src/features/admin/screens/{AdminHomeScreen,AdminUsersScreen,styles}.tsx/.ts`

## Validacoes executadas

- `npm run lint` ok, `npm run typecheck` ok, `npm run test` ok (9 suites, 19 testes)

## Pendencias

- Validar visual em dispositivo fisico/Expo Go
- Fonte Nunito segue sem pacote autorizado

## Proximo contexto recomendado

- `mobile/src/shared/components/ScreenHeader` e `IconPill` ao criar/refinar qualquer tela mobile
