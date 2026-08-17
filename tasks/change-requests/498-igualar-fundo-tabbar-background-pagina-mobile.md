# Task 498 - Igualar fundo da tab bar mobile ao background da página

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Slice vertical

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Objetivo

A faixa atrás da tab bar laranja (área do “sidebar”/menu inferior) está branca; deve usar a mesma cor bege/marrom claro do background da página.

## Criterios de aceite

- [x] shell + tabBarSlot + ShellTabBar wrapper usam `colors.background`
- [x] sem faixa branca entre o conteúdo e a barra laranja
- [x] indice/handoff atualizados

## Resultado da execucao

- `navigators/styles.ts`: shell e tabBarSlot com `colors.background`
- `ShellTabBar/styles.ts`: wrapper com `colors.background` (preenche o entalhe/padding da barra)

## Arquivos alterados

- `mobile/src/features/shell/navigators/styles.ts`
- `mobile/src/shared/components/ShellTabBar/styles.ts`
- `tasks/change-requests/498-igualar-fundo-tabbar-background-pagina-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-498.md`

## Status final

done
