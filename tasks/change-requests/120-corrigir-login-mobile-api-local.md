# Task 120 - Corrigir acesso da API no login mobile em ambiente local

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

- `contracts/openapi.yaml#/paths/~1auth~1login`

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Corrigir o login mobile para que o app consiga alcançar a API de autenticação quando executado localmente em Expo, em emulador ou dispositivo físico.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/120-corrigir-login-mobile-api-local.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `contracts/openapi.yaml`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-007.md`
- `mobile/.env`
- `backend/.env`
- `mobile/.env.example`
- `mobile/src/config/env.ts`
- `mobile/src/shared/network/apiClient.ts`
- `mobile/src/shared/network/createAppError.ts`
- `mobile/src/features/auth/services/authService.ts`

## Orcamento de contexto

- 12 fontes
- estrategia de reducao: restringir a investigacao ao caminho de auth, configuracao de ambiente e cliente HTTP do mobile

## Resultado da execucao

- O mobile passou a reescrever `EXPO_PUBLIC_API_URL` quando ela usa `localhost`, trocando pelo host real do Metro em dispositivo físico e por `10.0.2.2` no Android Emulator
- O login mobile deixa de falhar por erro de rede em ambiente local quando o backend está ativo na máquina de desenvolvimento
- O tratamento de erro de rede ficou mais explícito para diferenciar indisponibilidade de servidor de erros funcionais da API
- Foi adicionada cobertura de regressão para a resolução da URL base no runtime do Expo

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/002-autenticacao.md`
- Contexto sob demanda carregado: `contracts/openapi.yaml`, `mobile/docs/ai/ARCHITECTURE.md`, `mobile/docs/ai/CODE_STYLE.md`, `mobile/docs/ai/QA.md`, `.agents/state/handoffs/TASK-007.md`, `mobile/.env`, `backend/.env`, `mobile/.env.example`, `mobile/src/config/env.ts`, `mobile/src/shared/network/apiClient.ts`, `mobile/src/shared/network/createAppError.ts` e `mobile/src/features/auth/services/authService.ts`
- Fontes evitadas: design system mobile e telas visuais, porque o problema estava restrito a ambiente local, config e rede

## Handoff

- `.agents/state/handoffs/TASK-120.md`
- Decisoes preservadas: `localhost` continua aceito no `.env`, mas no app nativo passa por resolução de runtime; web permanece intacto; Android Emulator usa `10.0.2.2`
- Proximo contexto recomendado: `mobile/src/config/env.ts` e `mobile/src/config/resolveApiUrl.ts` se houver nova necessidade de ambientes/staging

## Arquivos alterados

- `mobile/src/config/env.ts`
- `mobile/src/config/resolveApiUrl.ts`
- `mobile/src/config/resolveApiUrl.test.ts`
- `mobile/src/shared/network/createAppError.ts`
- `mobile/.env.example`
- `tasks/change-requests/120-corrigir-login-mobile-api-local.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-120.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test -- --runInBand` - ok

## Pendencias pos-task

- Confirmar no dispositivo/emulador em uso que o backend local está rodando na porta `3000`
- Se a API estiver fora da máquina local, apontar `EXPO_PUBLIC_API_URL` para o host real em vez de `localhost`
- `backend/.env` segue com `APP_PUBLIC_URL=http://localhost:5173`, sem impacto direto neste bug do login mobile

## Status final

done
