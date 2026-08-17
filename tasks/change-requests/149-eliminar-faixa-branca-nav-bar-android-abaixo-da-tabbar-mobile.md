# Task 149 - Eliminar faixa branca da nav bar Android abaixo da tabbar mobile

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

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Objetivo

Eliminar a faixa branca nativa do Android abaixo da tab bar custom, sem alterar o design visual da `ShellTabBar` (SVG, icones, indicador).

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/149-eliminar-faixa-branca-nav-bar-android-abaixo-da-tabbar-mobile.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-148.md`

## Contexto sob demanda

- `mobile/app.json` (plugin `expo-navigation-bar` / contraste)
- `mobile/src/app/providers/AppProviders.tsx`
- `mobile/src/features/shell/navigators/*`
- `mobile/src/shared/theme/tokens.ts`
- `mobile/src/shared/components/ShellTabBar/*` (somente leitura; nao alterar design)

## Orçamento de contexto

- baixo: ajuste de system UI + preenchimento inferior do shell
- bloquear se exigir redesign da tab bar ou mudanca cross-stack

## Dependencias

- Task 147
- Task 148

## Validacao esperada

- `npm run lint`
- `npm run typecheck`

## Observacao

- Tasks 147/148 tentaram ocultar a nav bar e zerar o padding; a faixa branca permanece por contraste nativo (`enforceContrast`) / estilo claro da barra
- Estrategia: desativar contraste branco, alinhar fundo raiz ao bege do app e preencher o inset inferior do Android com a cor primaria no shell (fora do design da tab bar)

## Resultado da execucao

- Removido `style="dark"` da `NavigationBar` (era o que forçava scrim branco)
- Plugin `expo-navigation-bar` com `enforceContrast: false` e `hidden: true`
- Fundos raiz/navegacao alinhados a `colors.background`
- Shells master/responsavel preenchem o inset inferior Android com `colors.primary` sem alterar `ShellTabBar`

## Contexto utilizado

- handoff TASK-148
- AppProviders, shell navigators, app.json, tokens
- ShellTabBar apenas leitura

## Arquivos alterados

- `mobile/app.json`
- `mobile/src/app/providers/AppProviders.tsx`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/shell/navigators/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/shell/navigators/MasterShellNavigator.tsx`

## Validacoes executadas

- `npm run lint` — ok
- `npm run typecheck` — ok

## Pendencias pos-task

- No Expo Go, `enforceContrast: false` do plugin so vale plenamente apos development build / prebuild; no Go a ocultacao + fill do inset devem cobrir o caso
- Validar visualmente no aparelho apos reload do Metro

## Handoff

- `.agents/state/handoffs/TASK-149.md`

## Status final

done
