# Task 118 - Restaurar subtitulo da recuperacao de senha mobile

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

Restaurar a exibição do subtitulo completo na tela de recuperacao de senha mobile, sem remover a animacao de recolhimento ao abrir teclado.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/118-restaurar-subtitulo-recuperacao-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-117.md`
- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`

## Orcamento de contexto

- 7 fontes
- estrategia de reducao: ajustar apenas a altura do bloco superior da tela de recuperacao

## Resultado da execucao

- A altura base do bloco superior da tela de recuperacao foi aumentada para voltar a comportar o subtitulo completo
- A animacao de recolhimento ao abrir teclado foi preservada
- O ajuste ficou restrito a `PasswordRecoveryScreen`

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/docs/ai/AGENTS.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md`, `.agents/state/handoffs/TASK-117.md` e `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- Fontes evitadas por nao se aplicarem: `requirements/`, `contracts/openapi.yaml`, login mobile, estilos sem necessidade de ajuste e outras stacks
- Reducao de escopo: ajuste apenas da altura interpolada do topo da recuperacao

## Handoff

- `.agents/state/handoffs/TASK-118.md`
- Decisoes preservadas: recuperar senha manteve a animacao e ganhou mais espaço no topo para o subtitulo
- Proximo contexto recomendado: `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx` se houver novo refino de altura ou timing

## Arquivos alterados

- `mobile/src/features/auth/screens/PasswordRecoveryScreen.tsx`
- `tasks/change-requests/118-restaurar-subtitulo-recuperacao-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-118.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
