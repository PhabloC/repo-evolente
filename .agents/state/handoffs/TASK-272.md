# Handoff - Task 272

## Status

done

## Decisões

- CTA da home agora usa label + seta à direita
- CTA do hero da trilha foi alinhado ao mesmo visual da home
- o comportamento de navegação foi preservado

## Contexto utilizado

- `tasks/change-requests/272-alinhar-ctas-dos-heroes-home-e-trilha-mobile.md`
- `.agents/state/handoffs/TASK-271.md`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`

## Arquivos alterados

- `tasks/change-requests/272-alinhar-ctas-dos-heroes-home-e-trilha-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`
- `.agents/state/handoffs/TASK-272.md`
- `mobile/src/features/shell/components/HomeHeroBanner/index.tsx`
- `mobile/src/features/shell/components/HomeHeroBanner/styles.ts`
- `mobile/src/features/trail/screens/TrailTodayScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`

## Validacoes executadas

- `cd mobile && npx eslint src/features/shell/components/HomeHeroBanner/index.tsx src/features/shell/components/HomeHeroBanner/styles.ts src/features/trail/screens/TrailTodayScreen.tsx src/features/trail/screens/styles.ts` - sem retorno final da sessão
- `cd mobile && npm run typecheck` - sem retorno final da sessão

## Pendencias

- reexecutar validações do escopo em nova sessão
- `npm run lint` global do mobile continua com débitos antigos fora deste escopo

## Proximo contexto recomendado

- reutilizar esta task se outros heroes mobile precisarem padronizar CTA e ícone de ação
