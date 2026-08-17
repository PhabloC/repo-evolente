# Task 117 - Elevar recuperacao de senha mobile ao abrir teclado

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

Aplicar na tela de recuperacao de senha mobile a mesma animacao de recolhimento do topo e subida do bloco nuvem+form ao abrir teclado.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/117-elevar-recuperacao-com-teclado-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-116.md`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `mobile/src/features/auth/components/PasswordRecoveryForm.tsx`

## Orcamento de contexto

- 8 fontes
- estrategia de reducao: reaproveitar a mesma estrutura da tela de login e limitar a mudanca ao fluxo recovery

## Resultado da execucao

- `PasswordRecoveryScreen` passou a reagir ao foco do campo e aos eventos do teclado com a mesma animacao de recolhimento usada no login
- Logo, titulo e textos da recuperacao podem recolher temporariamente enquanto nuvem e formulario sobem para abrir espaço ao teclado
- A `PasswordRecoveryForm` passou a expor o foco do campo para disparo imediato da animacao

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md`, `.agents/state/handoffs/TASK-116.md`, `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`, `mobile/src/features/auth/screens/styles.ts` e `mobile/src/features/auth/components/PasswordRecoveryForm.tsx`
- Fontes evitadas por nao se aplicarem: `requirements/`, `contracts/openapi.yaml`, backend e demais telas mobile fora do auth
- Reducao de escopo: reuso da mesma estrutura de animacao ja consolidada no login

## Handoff

- `.agents/state/handoffs/TASK-117.md`
- Decisoes preservadas: recuperação usa a mesma lógica de recolhimento/subida do login, com disparo por foco e listeners de teclado
- Proximo contexto recomendado: `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx` se houver novo ajuste fino na amplitude

## Arquivos alterados

- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `mobile/src/features/auth/components/PasswordRecoveryForm.tsx`
- `tasks/change-requests/117-elevar-recuperacao-com-teclado-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-117.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
