# Task 719 - Corrigir persistência e restauração da sessão mobile

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

- `contracts/openapi.yaml#/paths/~1auth~1refresh` (consumo do refresh já existente)

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao
- `tasks/slices/002-autenticacao.md`

## Objetivo

Garantir que a sessão autenticada seja restaurada ao reabrir o app sem exigir e-mail e senha novamente, renovando o access token com o refresh token quando necessário e expondo falhas de persistência segura.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/719-corrigir-persistencia-sessao-mobile.md`
- `tasks/slices/002-autenticacao.md`

## Contexto sob demanda

- `contracts/openapi.yaml` (path de refresh)
- `mobile/docs/ai/AGENTS.md`
- `mobile/docs/ai/SECURITY.md`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/app/AppGate.tsx`
- `mobile/src/shared/network/apiClient.ts`
- `mobile/src/features/auth/types/session.ts`

## Orcamento de contexto

- 11 fontes
- estrategia de reducao: limitar a análise ao boot, storage seguro e refresh; não reabrir telas ou endpoints não relacionados.

## Criterios de aceite

- Sessão salva em login é restaurada no próximo boot do app.
- Access token expirado pode ser renovado usando refresh token antes da validação protegida.
- Falha no salvamento seguro não é silenciosa.
- Logout continua removendo a sessão local.
- Senha nunca é persistida.
- Testes do storage e typecheck/lint passam.

## Dependencias

- Task 127 (refresh automático de sessão mobile)
- Task 024 (hardening de auth e storage mobile)

## Fora de escopo

- Salvar senha em texto
- Alterar contrato ou backend
- Alterar layout das telas de autenticação

## Status final

done

## Resultado da execucao

- A restauração da sessão agora tenta renovar o access token quando a validação protegida falha.
- A renovação usa o refresh token persistido e salva o novo par de tokens no SecureStore.
- O papel retornado pelo refresh é validado antes da persistência e do retorno; perfis sem shell mobile são limpos e rejeitados.
- Falhas de gravação da sessão no SecureStore deixaram de ser silenciosamente ignoradas.
- No alvo web, onde o expo-secure-store não possui implementação, a sessão fica somente em memória para não bloquear o login nem persistir tokens em armazenamento inseguro.
- A senha não é persistida e o logout continua limpando a sessão local.

## Contexto utilizado

- Contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, Task 719 e Slice 002.
- Contexto sob demanda: contrato do `/auth/refresh`, segurança mobile, `authService`, `secureStorage`, `AppGate`, `apiClient`, tipos e testes de autenticação/storage.
- Não foram alteradas telas ou contrato/backend.

## Handoff

- `.agents/state/handoffs/TASK-719.md`
- Decisão: manter tokens no SecureStore e fazer refresh explícito durante a restauração quando a validação protegida rejeitar a sessão.
- Próximo contexto recomendado: validar reabertura do app com access token expirado em dispositivo real.

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `mobile/src/shared/storage/secureStorage.ts`
- `mobile/src/shared/storage/secureStorage.test.ts`
- `tasks/change-requests/719-corrigir-persistencia-sessao-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-719.md`

## Validacoes executadas

- `npx jest src/shared/storage/secureStorage.test.ts --runInBand --forceExit`: passou (7 testes).
- `npx jest src/features/auth/services/authService.test.ts --runInBand --forceExit`: passou (7 testes).
- `npx eslint src/shared/storage/secureStorage.ts src/shared/storage/secureStorage.test.ts`: passou.
- `npx eslint src/features/auth/services/authService.ts src/features/auth/services/authService.test.ts`: passou.
- `git -C mobile diff --check`: concluído sem erros.
- `npm run typecheck`: bloqueado por erros preexistentes em outros módulos; após a correção do tipo do teste novo, não restaram erros em `secureStorage.ts` ou `secureStorage.test.ts`.
- Revisão do diff: concluída.

## Pendencias pos-task

- Validar em dispositivo/emulador o cenário: login, fechar app, reabrir após expiração do access token e confirmar entrada sem redigitar senha.
- Validar manualmente o login web sabendo que a sessão em memória será perdida ao recarregar a página; persistência web segura permanece fora do escopo desta correção.
