# Task 799 - Versão do login segue a versão publicada

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

- Slice 002 — `tasks/slices/002-autenticacao.md`

## Referencia de design system

- Stack: mobile
- Fonte: `design-system/mobile/prints/login-mobile.png`
- Preservar rodapé `Versão X.Y.Z` (Task 789)

## Origem da solicitacao

Pedido humano: a versão na página de login precisa mudar quando a versão do app muda.

## Objetivo

O rodapé do login deve ler a versão do config Expo publicado (`expo.version` / OTA), não um import estático que pode ficar atrás do binário da loja.

## Fora de escopo

- Build de loja
- Mudar o layout do login

## Dependências

- Task 789

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 002

## Contexto sob demanda

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `expo-constants`

## Orçamento de contexto

- Fontes obrigatórias: 6

## Criterios de aceite

- [x] Login mostra `Constants.expoConfig.version` (cai no nativo se vazio)
- [ ] Ao publicar OTA com `expo.version` novo, o número do login muda após aplicar o update

## Resultado da execucao

- `getAppVersion()` lê `Constants.expoConfig.version` e cai em `nativeAppVersion`
- `SignInScreen` deixou de importar `app.json` direto
- Testes do util passam

## Contexto utilizado

- SignInScreen, expo-constants, Slice 002

## Handoff

- `.agents/state/handoffs/TASK-799.md`

## Arquivos alterados

- `mobile/src/shared/utils/getAppVersion.ts`
- `mobile/src/shared/utils/getAppVersion.test.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `tasks/change-requests/799-versao-login-segue-expo-config.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-799.md`

## Validacoes executadas

- `npx jest src/shared/utils/getAppVersion.test.ts` — 2 passed

## Pendencias pos-task

- Publicar OTA com este JS para o número `1.0.3` aparecer no login das lojas 1.0.2/1.0.3

## Status final

done
