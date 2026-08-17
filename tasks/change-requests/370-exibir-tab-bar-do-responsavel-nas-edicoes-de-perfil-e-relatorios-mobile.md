# Task 370 - Exibir tab bar do responsável nas edições de perfil e relatórios mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- não se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

refino incremental da navegação do responsável

### Fonte primaria visual

- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/shared/components/ShellTabBar`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/screens/EditChildProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`

## Objetivo

Fazer a tab bar do responsável aparecer também nas telas de edição de perfil do responsável, edição da criança e página de relatórios.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-369.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Navegação do responsável | `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`, `mobile/src/routes/params.ts` | reaproveitar a tab bar e sincronizar a tab ativa | sim |
| Tab bar compartilhada | `mobile/src/shared/components/ShellTabBar/index.tsx` e `styles.ts` | renderizar a mesma barra fora do shell principal | sim |
| Telas alvo | `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`, `EditChildProfileScreen.tsx`, `mobile/src/features/shell/screens/GuardianReportsScreen.tsx` | encaixar a tab bar nas telas pedidas | sim |
| Arquitetura mobile | `mobile/docs/ai/ARCHITECTURE.md` e `mobile/docs/ai/CODE_STYLE.md` | manter navegação e layout em camadas coerentes | sim |

## Orçamento de contexto

- baixo
- estratégia: extrair um frame compartilhado do responsável e reutilizá-lo nas telas fora do shell principal, evitando duplicar a lógica da tab bar

## Criterios de conclusao

- [x] edição do responsável exibe a tab bar do responsável
- [x] edição da criança exibe a tab bar do responsável
- [x] página de relatórios exibe a tab bar do responsável
- [x] tocar em uma tab fora do shell volta para a área correspondente do responsável
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 369 - done

## Resultado da execucao

- foi criado um frame compartilhado do responsável com a mesma `ShellTabBar` do shell principal
- as telas de editar responsável, editar criança e relatórios passaram a usar esse frame
- a navegação do shell passou a aceitar `initialTab`, permitindo abrir a aba correta quando a navegação vem dessas telas externas

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-369.md`
- `mobile/docs/ai/ARCHITECTURE.md`, `mobile/docs/ai/CODE_STYLE.md`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/shared/components/ShellTabBar/index.tsx`
- `mobile/src/shared/components/ShellTabBar/styles.ts`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/screens/EditChildProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/routes/params.ts`

## Handoff

- `.agents/state/handoffs/TASK-370.md`

## Arquivos alterados

- `tasks/change-requests/370-exibir-tab-bar-do-responsavel-nas-edicoes-de-perfil-e-relatorios-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-370.md`
- `mobile/src/features/shell/constants/responsavelTabs.ts`
- `mobile/src/features/shell/components/ResponsavelStackScreenFrame.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/screens/EditChildProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/routes/params.ts`

## Validacoes executadas

- `cd mobile && npm run lint` — falhou por erros preexistentes em `WordSearchGameRenderer`, `EditChildProfileScreen`, `EditGuardianProfileScreen`, `HomeHeader`, `AppBackgroundBubbles` e `Screen`
- `cd mobile && npm run typecheck` — falhou por erros preexistentes em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` — passou (`27` suítes, `95` testes)

## Pendencias pos-task

- erros preexistentes de lint e typecheck no app mobile seguem fora do escopo desta task

## Status final

done
