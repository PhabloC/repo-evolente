# Task 114 - Elevar login mobile ao abrir teclado

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

Ao focar os inputs de login mobile, fazer a nuvem e o formulario deslizarem para cima para abrir espaço ao teclado, permitindo que logo, titulo e subtitulo recolham temporariamente.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/114-elevar-login-com-teclado-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-113.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`

## Orcamento de contexto

- 8 fontes
- estrategia de reducao: alterar apenas a composicao visual do login mobile e o foco dos campos

## Resultado da execucao

- `SignInScreen` passou a reagir ao foco dos campos e aos eventos do teclado com uma animacao curta de recolhimento
- Logo, titulo e subtitulo podem recolher temporariamente enquanto a nuvem e o formulario deslizam para cima
- O ajuste foi restrito ao login mobile; recovery e demais telas ficaram intactos

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md`, `.agents/state/handoffs/TASK-113.md`, `mobile/src/features/auth/screens/SignInScreen.tsx`, `mobile/src/features/auth/screens/styles.ts` e `mobile/src/features/auth/components/SignInForm.tsx`
- Fontes evitadas por nao se aplicarem: `requirements/`, `contracts/openapi.yaml`, recovery mobile e outras stacks
- Reducao de escopo: alteracao localizada apenas na tela de login e no foco dos campos

## Handoff

- `.agents/state/handoffs/TASK-114.md`
- Decisoes preservadas: disparo por foco dos campos e reforco por listener de teclado para manter o comportamento consistente
- Proximo contexto recomendado: `mobile/src/features/auth/screens/SignInScreen.tsx` se houver novo ajuste de amplitude, timing ou comportamento no recovery

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/SignInForm.tsx`
- `tasks/change-requests/114-elevar-login-com-teclado-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-114.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
