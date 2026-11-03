# Handoff TASK-805

## Decisões

- Causa: OTAs de produção de 29/10 publicados do commit `e95a16d`, que não tinha a Task 791. Correção: republicar a partir do `main` (`ec80da9`).
- Publicar por plataforma (`--platform ios` / `android`). Com `all`, o export web falha por causa de um ícone webp.
- Runtime 1.0.2 (só Android): `expo.version` em 1.0.2 apenas durante o `eas update`, depois revertido para 1.0.3.

## Arquivos alterados (mobile)

- `src/features/auth/screens/SignInScreen.tsx`
- `src/shared/utils/getAppVersion.ts` e o teste dele

## Validação

- eslint, tsc e jest passaram. Os updates `7fabb2d6` (iOS 1.0.3), `b434183c` (Android 1.0.3) e `168dc457` (Android 1.0.2) foram publicados.

## Pendências

- Revisar e fazer merge da PR #28.
- O stash "login getAppVersion (OTA hoje)" da branch `chore/versao-loja-1-0-3` foi mantido. Só descartar com aval do usuário.
- Publicar futuros OTAs sempre a partir do `main` atualizado.
