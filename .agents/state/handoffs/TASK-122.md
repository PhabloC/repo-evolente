# Handoff - Task 122

## Identificador

- Task 122 - Melhorar design da home do responsavel no mobile
- `tasks/change-requests/122-melhorar-design-home-responsavel-mobile.md`

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Status final

done

## Decisoes preservadas

- Home do responsavel composta por `HomeHeader` (avatar com inicial, saudacao, sino com badge de nao lidos) e `HomeActionCard` (pastilha de icone com tint, titulo, badge, descricao, chevron quando pressable, slot para CTA)
- Tints suaves viraram tokens compartilhados: `orangeSoft`, `pinkSoft`, `blueSoft`, `yellowSoft`, `coralSoft`
- Papel das cores por DS: laranja = trilha/acao, azul = avisos/informacao, coral = acesso limitado/atencao, rosa = avatar/acolhimento
- "Sair" ghost no rodape via `marginTop: 'auto'`
- Correcao colateral: `ShellTabBar` deixou de acessar ref durante render (`react-hooks/refs`), lint pre-existente que bloqueava a validacao

## Contexto efetivamente usado

- Task 122, slice 010, `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/COMPONENT_REUSE.md`
- `ResponsavelHomeScreen.tsx`, `shell/screens/styles.ts`, `ResponsavelShellNavigator.tsx`, `tokens.ts`, shared components e hooks de perfil/notificacoes

## Arquivos alterados

- `mobile/src/shared/theme/tokens.ts`
- `mobile/src/features/shell/components/HomeHeader/{index.tsx,styles.ts}` (novos)
- `mobile/src/features/shell/components/HomeActionCard/{index.tsx,styles.ts}` (novos)
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/shared/components/ShellTabBar/index.tsx`

## Validacoes executadas

- `npm run lint` ok, `npm run typecheck` ok, `npm run test` ok (9 suites, 19 testes)

## Pendencias

- Validar visual em dispositivo fisico/Expo Go
- Possivel reuso do `HomeActionCard` na home do master (CR futuro)

## Proximo contexto recomendado

- `mobile/src/features/shell/components/` para novos refinos da home ou reuso de cards
