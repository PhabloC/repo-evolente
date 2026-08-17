# Task 150 - Hardening de auth, storage e acessibilidade mobile

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

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 024 - Hardening de auth, storage e acessibilidade mobile
- `tasks/slices/024-hardening-auth-acessibilidade-mobile.md`

## Objetivo

Aplicar os ajustes levantados no code review de `ajustes_mobile.md` para endurecer auth/storage mobile, corrigir configuracao Expo e melhorar acessibilidade sem redesenhar a interface.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/150-hardening-auth-acessibilidade-mobile.md`
- `tasks/slices/024-hardening-auth-acessibilidade-mobile.md`
- `.agents/state/handoffs/TASK-127.md`
- `.agents/state/handoffs/TASK-149.md`

## Contexto sob demanda

- `ajustes_mobile.md`
- `mobile/app.json`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/QA.md`
- `mobile/src/shared/components/TextField/*`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/features/shell/components/HomeActionCard/*`
- `mobile/src/features/shell/components/HomeShortcutTile/*`
- arquivos consumidores de `TextField` no auth, somente se a tipagem exigir ajuste

## Orçamento de contexto

- baixo: change request localizada em componentes compartilhados, auth/storage e configuracao Expo
- bloquear se a correcao exigir redesenhar telas, alterar contrato/API ou reabrir multiplos slices visuais

## Dependencias

- Task 121
- Task 123
- Task 127
- Task 149

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Observacao

- Origem: code review consolidado em `ajustes_mobile.md`
- Escopo validado: 7 pontos objetivos, sem duplicidade com tasks existentes

## Resultado da execucao

- `TextField` compartilhado agora encaminha `ref` ao `TextInput`, e os fluxos de login/reset passaram a usar foco programatico entre campos
- `biometricPreferenceStorage` passou a tratar falhas de `AsyncStorage` com fallback defensivo para a preferencia padrao
- `sessionStorage` passou a migrar a sessao legada de `mobile:auth:session` para `mobile.auth.session`, alem de tolerar falhas de `SecureStore`
- `HomeActionCard` e `HomeShortcutTile` passaram a compor labels acessiveis com badge/descricao quando nao houver label explicita
- `expo-status-bar` foi removido da lista de plugins do `app.json`, mantendo apenas o uso do componente JavaScript

## Contexto utilizado

- `ajustes_mobile.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/COMPONENT_REUSE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-127.md`
- `.agents/state/handoffs/TASK-149.md`
- `mobile/app.json`
- `mobile/src/shared/components/TextField/*`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/screens/PasswordResetScreen.tsx`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/features/shell/components/HomeActionCard/*`
- `mobile/src/features/shell/components/HomeShortcutTile/*`

## Arquivos alterados

- `mobile/app.json`
- `mobile/src/shared/components/TextField/index.tsx`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/screens/PasswordResetScreen.tsx`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.ts`
- `mobile/src/features/auth/storage/biometricPreferenceStorage.test.ts`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeShortcutTile/index.tsx`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/shared/storage/secureStorage.test.ts`

## Validacoes executadas

- `npm run lint` — ok
- `npm run typecheck` — ok
- `npm run test` — ok (12 suites, 30 testes)

## Pendencias pos-task

- Validar em dispositivo/emulador que o foco entre campos de auth segue natural com o teclado nativo
- Se existirem mais componentes clicaveis com badge na home mobile, aplicar o mesmo padrao de label acessivel em task futura

## Handoff

- `.agents/state/handoffs/TASK-150.md`
- `mobile/docs/ai/ACCESSIBILITY.md` nao existe; foram aplicadas apenas as praticas locais ja consolidadas de acessibilidade na stack

## Status final

done
