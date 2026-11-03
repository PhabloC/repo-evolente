# Task 805 - Restaurar diretório de profissionais no app via OTA de produção

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite) (não envolvida)
- mobile: sim

## Contrato

Não aplicável (sem mudança de API).

## Modo de execucao

single-stack

## Slice vertical

`tasks/slices/` do diretório de profissionais (Task 791). Esta task só corrige a publicação, sem escopo novo.

## Contexto mínimo

- `mobile/app.json` (`runtimeVersion` com policy `appVersion`)
- `mobile/eas.json` (canal `production`)
- `mobile/src/features/auth/screens/SignInScreen.tsx`

## Contexto sob demanda

- `tasks/change-requests/791-card-encontrar-profissionais-perfil-mobile.md`, para confirmar a feature perdida

## Orçamento de contexto

Baixo.

## Problema

O card "Encontrar profissionais" (Task 791, PR #26) sumiu do perfil de paciente em produção. Os OTAs publicados em 29/10 vieram do commit `e95a16d`, de uma branch local sem a feature, e substituíram o bundle das lojas (iOS 1.0.3, Android 1.0.3 e 1.0.2).

## Entrega

- Branch `fix/ota-restaura-diretorio-profissionais` criada a partir do `main`, com a versão do login lida via `expo-constants` (`getAppVersion`).
- PR: https://github.com/fasters-projects/evolente-app/pull/28
- OTAs de produção publicados do commit `ec80da9`:
  - iOS runtime 1.0.3: `7fabb2d6-fb20-4351-8466-f92ac12f5d25`
  - Android runtime 1.0.3: `b434183c-b827-4a7f-bfac-003beccdb434`
  - Android runtime 1.0.2: `168dc457-08c5-4ab5-a5a4-6d309a56766b` (com `expo.version` em 1.0.2 só durante a publicação, depois revertido)

## Validação

- eslint, `tsc --noEmit` e jest (auth, professionals, getAppVersion): 11 suítes e 39 testes passaram.

## Fora de escopo

- Build de loja (não houve bump de `expo.version`).
- OTA com `--platform all`: falha no export web (`image/webp` não suportado pelo jimp). Publicar por plataforma.
