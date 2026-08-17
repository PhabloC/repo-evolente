# Handoff - Task 268

## Status

done

## Decisões

- o `bell.webp` foi aplicado no quadro "Avisos da trilha" da home
- o sino do header foi revertido para o ícone vetorial anterior
- não foi aberto escopo para corrigir débitos antigos de lint do `HomeHeader`

## Contexto utilizado

- `tasks/change-requests/268-usar-bell-na-home-com-asset-local-mobile.md`
- `.agents/state/handoffs/TASK-265.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/assets/bell.webp`

## Arquivos alterados

- `tasks/change-requests/268-usar-bell-na-home-com-asset-local-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-268.md`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeHeader/index.tsx`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/components/HomeHeader/index.tsx src/features/shell/components/HomeActionCard/index.tsx src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `cd mobile && npm run typecheck`

## Pendencias

- `HomeHeader` continua com débitos antigos de lint na regra `react-hooks/refs`

## Proximo contexto recomendado

- abrir task dedicada se quiser corrigir o lint estrutural de `HomeHeader`
