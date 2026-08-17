# Task 119 - Restaurar copy completa nas telas auth mobile

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

Restaurar a exibicao completa do subtitulo no login mobile e eliminar o corte inferior do texto na recuperacao de senha, preservando a animacao atual de recolhimento ao abrir o teclado.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/119-restaurar-copy-auth-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-118.md`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`

## Orcamento de contexto

- 8 fontes
- estrategia de reducao: limitar o ajuste aos limites de altura do hero nas telas de auth mobile, sem reabrir o layout da nuvem ou o formulario

## Resultado da execucao

- A altura expandida do topo no login mobile foi aumentada para voltar a exibir o subtitulo completo
- A altura expandida do topo na recuperacao de senha foi aumentada para impedir o corte inferior do texto
- A animacao de recolhimento ao abrir teclado foi preservada nas duas telas

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md`, `.agents/state/handoffs/TASK-118.md`, `mobile/src/features/auth/screens/SignInScreen.tsx`, `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx` e `mobile/src/features/auth/screens/styles.ts`
- Fontes evitadas por nao se aplicarem: `requirements/`, `contracts/openapi.yaml`, outras stacks e outros fluxos mobile fora de auth
- Reducao de escopo: ajuste concentrado nas interpolacoes de altura do hero para evitar regressao visual ampla

## Handoff

- `.agents/state/handoffs/TASK-119.md`
- Decisoes preservadas: o auth mobile continua sem scroll e com a mesma animacao de teclado, mas com area superior maior para acomodar a copy completa
- Proximo contexto recomendado: `mobile/src/features/auth/screens/SignInScreen.tsx` e `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx` se houver novo refino fino de altura ou timing

## Arquivos alterados

- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `tasks/change-requests/119-restaurar-copy-auth-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-119.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
