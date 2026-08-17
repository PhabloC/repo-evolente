# Task 115 - Reduzir subida do login mobile ao abrir teclado

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

Reduzir um pouco a altura da subida do bloco nuvem+form no login mobile quando o teclado abrir.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/115-reduzir-subida-login-teclado-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-114.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`

## Orcamento de contexto

- 7 fontes
- estrategia de reducao: refino numerico localizado apenas na amplitude da animacao ja existente

## Resultado da execucao

- A amplitude da animacao do bloco nuvem+form no login mobile foi reduzida
- O deslocamento ao abrir o teclado passou de `-128` para `-96`, mantendo o comportamento mas com subida mais contida
- Nenhum outro aspecto do login foi alterado

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md`, `.agents/state/handoffs/TASK-114.md` e `mobile/src/features/auth/screens/SignInScreen.tsx`
- Fontes evitadas por nao se aplicarem: `requirements/`, `contracts/openapi.yaml`, recovery mobile, estilos sem necessidade de alteracao e demais stacks
- Reducao de escopo: ajuste numerico localizado apenas na amplitude da interpolacao

## Handoff

- `.agents/state/handoffs/TASK-115.md`
- Decisoes preservadas: manter o padrão de recolhimento, apenas com menor elevação do bloco inferior
- Proximo contexto recomendado: `mobile/src/features/auth/screens/SignInScreen.tsx` se houver novo ajuste fino de amplitude

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `tasks/change-requests/115-reduzir-subida-login-teclado-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-115.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
