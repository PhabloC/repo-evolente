# Task 113 - Exibir erro de login em modal central no mobile

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

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Substituir a mensagem inline de erro no login mobile por um mini modal central com a informacao e acao `OK`.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/113-modal-erro-login-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-112.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/components/styles.ts`
- `mobile/src/features/auth/hooks/useSignInForm.ts`

## Orcamento de contexto

- 10 fontes
- estrategia de reducao: limitar mudanca ao fluxo de erro do login mobile, sem tocar recovery nem backend

## Resultado da execucao

- O erro de autenticação deixou de aparecer abaixo do botão `Entrar`
- `SignInScreen` agora exibe um mini modal central com título, mensagem de erro e botão `OK`
- `SignInForm` ficou responsável apenas pelos campos e submit, sem renderização inline de erro de credencial

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md`, `.agents/state/handoffs/TASK-112.md`, `mobile/src/features/auth/screens/SignInScreen.tsx`, `mobile/src/features/auth/screens/styles.ts`, `mobile/src/features/auth/components/SignInForm.tsx`, `mobile/src/features/auth/components/styles.ts` e `mobile/src/features/auth/hooks/useSignInForm.ts`
- Fontes evitadas por nao se aplicarem: `requirements/`, `contracts/openapi.yaml`, recovery mobile e outras stacks
- Reducao de escopo: alteracao restrita ao fluxo de erro do login

## Handoff

- `.agents/state/handoffs/TASK-113.md`
- Decisoes preservadas: erro de login centralizado na tela e fechamento explícito por `OK`
- Proximo contexto recomendado: `mobile/src/features/auth/screens/SignInScreen.tsx` se houver novo refino de copy ou comportamento do modal

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `mobile/src/features/auth/hooks/useSignInForm.ts`
- `tasks/change-requests/113-modal-erro-login-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-113.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
