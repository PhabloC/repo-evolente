# Task 807 - Corrigir avisos Play Console (DEX + edge-to-edge)

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

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 073 — `tasks/slices/073-play-console-qualidade-android.md`

## Referencia de design system

- nao se aplica (config nativa / system bars; sem redesign de telas)

## Origem da solicitacao

Pedido humano: corrigir avisos da Play Console na versão 1.0.2 — ofuscação DEX em 1% e APIs descontinuadas de edge-to-edge.

## Objetivo

1. Habilitar R8 (minify + shrink + optimize) nos builds Android de release via `expo-build-properties` e preset `proguard-android-optimize.txt`, com keep rules mínimas para Expo Modules.
2. Alinhar edge-to-edge: manter plugin `expo-navigation-bar` moderno e tornar modais Android translucent nas system bars.

## Fora de escopo

- `eas build` / submit nesta task
- Bump de `expo.version` (obrigatório só imediatamente antes do build de loja)
- Garantir remoção total do aviso edge-to-edge se a origem for `react-native`/`expo-image-picker` internos

## Dependências

- nenhuma

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 073

## Contexto sob demanda

- `mobile/app.json`, `mobile/package.json`
- `mobile/android/app/build.gradle` (local/prebuild, gitignored)
- componentes com `<Modal>`

## Orçamento de contexto

- Fontes obrigatórias: 8
- Estratégia de redução: não carregar front-end/backend/requirements

## Criterios de aceite

- [x] `expo-build-properties` instalado e plugin com `enableMinifyInReleaseBuilds` + `enableShrinkResourcesInReleaseBuilds`
- [x] Prebuild/EAS usa `proguard-android-optimize.txt`
- [x] Keep rules mínimas de Expo Modules em `extraProguardRules`
- [x] Modais Android com `statusBarTranslucent` e `navigationBarTranslucent`
- [x] Task, índice e handoff atualizados

## Resultado da execucao

- R8 ativado no release via `expo-build-properties`
- Plugin `./plugins/withAndroidR8Optimize.js` troca o preset ProGuard para `proguard-android-optimize.txt`
- Keep rules mínimas para `expo.modules.**`
- Todos os `<Modal>` do app com `statusBarTranslucent` + `navigationBarTranslucent`
- Edge-to-edge já é mandatório no SDK 57; não foi adicionado `edgeToEdgeEnabled` (gera warning no prebuild)

## Contexto utilizado

- Task 807, Slice 073, `mobile/app.json`, docs Play/Expo R8, Modais mobile

## Handoff

- `.agents/state/handoffs/TASK-807.md`

## Arquivos alterados

- `mobile/app.json`
- `mobile/package.json` (+ lockfile)
- `mobile/plugins/withAndroidR8Optimize.js`
- `mobile/src/shared/components/AppConfirmModal/index.tsx`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/professionals/components/ProfessionalContactModal.tsx`
- `mobile/src/features/admin/screens/AdminUserDetailScreen.tsx`
- `mobile/src/features/games/components/WordSearchGameRenderer/index.tsx`
- `tasks/change-requests/807-corrigir-avisos-play-console-dex-edge-to-edge.md`
- `tasks/slices/073-play-console-qualidade-android.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-807.md`

## Validacoes executadas

- `npx expo install expo-build-properties` → `~57.0.22`
- Patch local gitignored confirmado: minify/shrink + optimize preset + keep rules

## Pendencias pos-task

- Bump `expo.version` antes do próximo build de loja se `1.0.3` já foi enviada
- `eas build` Android production + validar % DEX no App bundle explorer
- Smoke test do AAB release (R8)
- Aviso edge-to-edge pode permanecer por código interno do React Native

## Status final

done
