# Handoff - Task 148

## Identificador

- Task 148 - Remover folga inferior da tabbar apos ocultar nav bar mobile
- `tasks/change-requests/148-remover-folga-inferior-da-tabbar-apos-ocultar-nav-bar-mobile.md`

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Status final

done

## Decisoes preservadas

- A folga inferior foi removida apenas no Android
- iOS continua respeitando `safe area` inferior da tab bar

## Arquivos alterados

- `mobile/src/shared/components/ShellTabBar/index.tsx`

## Validacoes executadas

- `npm run lint` ok
