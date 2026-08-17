# Handoff - Task 370

## Task

- identificador: 370
- título: Exibir tab bar do responsável nas edições de perfil e relatórios mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010

## Decisões preservadas

- decisão: extrair um frame compartilhado do responsável para telas fora do shell principal
- motivo: evitar duplicar a lógica da `ShellTabBar` e do preenchimento inferior do Android
- impacto: as telas de edição e relatórios passaram a usar a mesma base visual e de navegação do shell

- decisão: sincronizar a tab ativa por `initialTab` na rota `ResponsavelShell`
- motivo: permitir que a tab bar dessas telas externas leve o usuário de volta para a aba correta
- impacto: a navegação entre `Home`, `Trilha`, `Perfil` e `Avisos` funciona também fora do shell principal

## Contexto utilizado

- handoff `TASK-369`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/shared/components/ShellTabBar/**`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/screens/EditChildProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/routes/params.ts`

## Arquivos alterados

- `mobile/src/features/shell/constants/responsavelTabs.ts`
- `mobile/src/features/shell/components/ResponsavelStackScreenFrame.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/screens/EditChildProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/routes/params.ts`
- `tasks/change-requests/370-exibir-tab-bar-do-responsavel-nas-edicoes-de-perfil-e-relatorios-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-370.md`

## Validações executadas

- `cd mobile && npm run lint` — falhou por erros preexistentes fora do escopo
- `cd mobile && npm run typecheck` — falhou por erros preexistentes fora do escopo
- `cd mobile && npm run test` — passou (`27` suítes, `95` testes)

## Pendências ou bloqueios

- erros preexistentes de lint e typecheck no mobile continuam abertos

## Próxima ação sugerida

- se o usuário quiser, consolidar o comportamento de navegação externa do shell também em outras telas do responsável fora da raiz do tab bar

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-370.md`
- `mobile/src/features/shell/components/ResponsavelStackScreenFrame.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
