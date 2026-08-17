# Task 108 - Splash loading com selo e textos girando (mobile)

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Criar tela de loading com `logo-seal.webp` no centro e textos "Evolente / Desenvolver hoje / Evoluir sempre" girando ao redor. Na saida, a logo avanca em zoom + fade revelando a tela seguinte.

## Resultado da execucao

- `SplashLoadingScreen` + `RotatingBrandRing` com Animated API
- Integrado em `AppGate` (boot + tempo minimo ~2.2s)
- Saida: anel some, selo escala e some, overlay some e revela login/shell
- lint/typecheck ok

## Handoff

- `.agents/state/handoffs/TASK-108.md`

## Arquivos alterados

- `mobile/src/features/splash/components/SplashLoadingScreen.tsx`
- `mobile/src/features/splash/components/SplashLoadingScreen.styles.ts`
- `mobile/src/features/splash/components/RotatingBrandRing.tsx`
- `mobile/src/features/splash/components/RotatingBrandRing.styles.ts`
- `mobile/src/app/AppGate.tsx`
- `tasks/change-requests/108-splash-loading-selo-textos-girando-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-108.md`

## Status final

done
