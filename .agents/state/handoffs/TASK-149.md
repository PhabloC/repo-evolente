# Handoff - Task 149

## Identificador

- Task 149 - Eliminar faixa branca da nav bar Android abaixo da tabbar mobile
- `tasks/change-requests/149-eliminar-faixa-branca-nav-bar-android-abaixo-da-tabbar-mobile.md`

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Status final

done

## Decisoes preservadas

- A faixa branca vinha do scrim nativo Android (`style="dark"` + `enforceContrast`), nao do design da `ShellTabBar`
- `ShellTabBar` permanece intocada visualmente
- O inset inferior Android e preenchido no shell com `colors.primary`
- Fundos raiz usam `colors.background` para evitar branco do window

## Contexto minimo lido

- AGENTS.md, GUIDE.md, context-map, 000-index, task 149, slice 022, handoff 148

## Contexto sob demanda carregado

- app.json, AppProviders, AppGate, RootNavigator, shell navigators/styles, tokens
- ShellTabBar (leitura)

## Arquivos alterados

- `mobile/app.json`
- `mobile/src/app/providers/AppProviders.tsx`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/shell/navigators/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/shell/navigators/MasterShellNavigator.tsx`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok

## Pendencias

- Confirmar no device apos reload; plugin `enforceContrast: false` exige native build para efeito total no tema

## Proxima acao sugerida

- Recarregar o app no Android e validar a base da tela com tab bar

## Proximo contexto recomendado

- handoff TASK-149 + shell navigators se ainda houver faixa residual

## Contexto que nao deve ser carregado

- requirements, contracts, design-system completo, stacks web/backend
