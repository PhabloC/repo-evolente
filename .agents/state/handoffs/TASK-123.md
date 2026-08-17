# Handoff - Task 123

## Identificador

- Task 123 - Aproximar a home do responsavel do print de referencia
- `tasks/change-requests/123-home-responsavel-fiel-ao-print-referencia.md`

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Status final

done

## Decisoes preservadas

- Print `design-system/mobile/prints/home-responsavel-referencia.png` governa a composicao da home do responsavel (header saudacao+avatar-tile, banner hero laranja com CTA pilula, atalhos pastel, secao de cards com "Ver todos")
- Cores continuam vindo dos tokens Evolente, nao do amarelo/pessego exatos do print (DS documental governa paleta)
- Sem mascote/ilustracoes do print (marca de terceiros); apenas circulos decorativos no banner
- Sino removido do `HomeHeader`; avisos acessiveis via tile pastel com badge e card da secao
- `ResponsavelShellNavigator` ganhou repasse `onOpenProfile`; `ShellTabBar` intocado (restricao explicita do usuario)

## Contexto efetivamente usado

- Task 123, slice 010, handoff TASK-122, print de referencia, tokens do tema, componentes da home (Task 122), navigator do responsavel

## Arquivos alterados

- `mobile/src/features/shell/components/HomeHeroBanner/{index.tsx,styles.ts}` (novos)
- `mobile/src/features/shell/components/HomeShortcutTile/{index.tsx,styles.ts}` (novos)
- `mobile/src/features/shell/components/HomeHeader/{index.tsx,styles.ts}` (restilizados)
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `design-system/mobile/prints/home-responsavel-referencia.png` (novo)

## Validacoes executadas

- `npm run lint` ok, `npm run typecheck` ok, `npm run test` ok (9 suites, 19 testes)

## Pendencias

- Validar visual em dispositivo fisico/Expo Go
- Fonte Nunito segue sem pacote autorizado (tipografia bold do print aproximada com peso extrabold do sistema)

## Proximo contexto recomendado

- `mobile/src/features/shell/components/` e o print de referencia, se houver novo refino da home
