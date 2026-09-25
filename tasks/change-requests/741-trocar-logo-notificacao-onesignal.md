## Status

done

# Task 741 - Trocar logo usada na configuração do app

## Objetivo

Usar `mobile/assets/logo-seal-original.webp` em todos os pontos da configuração Expo que atualmente referenciam `logo-seal.png`, incluindo o ícone pequeno do OneSignal, e remover a configuração obsoleta `NOTIFICATION_IMAGE_URL`.

## Tipo

mobile

## Stacks envolvidos

mobile (Expo/EAS)

## Perfil do projeto

stack web `front-end` (React/Vite); mobile `sim` (Expo)

## Contrato

Não aplicável.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/060-one-signal-push-mobile.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/060-one-signal-push-mobile.md`
- `mobile/app.json`
- `mobile/assets/logo-seal-original.webp`

## Contexto sob demanda

- `mobile/docs/ai/QA.md`: validar a configuração Expo final.

## Orçamento de contexto

Até 6 fontes; limitar às referências de asset, configuração Expo/OneSignal e validação mobile.

## Resultado da execucao

Todas as referências antigas de `logo-seal.png`/`logo-seal.webp` na configuração e nos componentes de splash/auth foram substituídas por `logo-seal-original.webp`. A variável local `NOTIFICATION_IMAGE_URL` também foi removida, pois o payload não envia mais mídia.

## Contexto utilizado

Contexto mínimo da raiz, slice 060, `mobile/app.json`, asset solicitado e QA mobile.

## Handoff

O próximo build nativo deve confirmar a renderização do `.webp` como ícone Android, ícone OneSignal, adaptive icon e splash.

## Arquivos alterados

- `mobile/app.json`
- `mobile/src/features/splash/components/SplashLoadingScreen.tsx`
- `mobile/src/features/auth/components/AuthHero.tsx`
- `backend/.env` (configuração local não versionada)
- `tasks/change-requests/741-trocar-logo-notificacao-onesignal.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-741.md`

## Validacoes executadas

- `node -e "require('./app.config.js')"` — passou com as referências `.webp`.
- `git diff --check` — passou.

## Pendencias pos-task

- Validar visualmente em novo build nativo Android/iOS.

## Status final

done
