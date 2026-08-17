# Task 125 - Resiliencia da API nas telas do responsavel mobile

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

- `contracts/openapi.yaml#/paths/~1guardians~1me`
- `contracts/openapi.yaml#/paths/~1guardians~1me~1children`
- `contracts/openapi.yaml#/paths/~1notifications`
- `contracts/openapi.yaml#/paths/~1patients~1{patientId}~1trails`
- `contracts/openapi.yaml#/paths/~1patients~1{patientId}~1progress`

## Modo de execucao

single-stack

## Slice vertical

- Slice 023 - Resiliencia da API no app do responsavel
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

continuidade da linguagem existente

### Fonte primaria visual

- `design-system/mobile/prints/home-responsavel-referencia.png`

## Objetivo

Corrigir o erro recorrente nas telas de atividades, perfil e avisos do app do responsavel quando a API fica indisponivel no ambiente mobile, degradando a leitura para fallback local em vez de bloquear a UX com erro fatal de conexao.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/125-resiliencia-api-telas-responsavel-mobile.md`
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`

## Contexto sob demanda

- `contracts/openapi.yaml`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-120.md`
- `.agents/state/handoffs/TASK-124.md`
- `mobile/src/config/env.ts`
- `mobile/src/shared/network/`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/notifications/services/notificationsService.ts`
- `mobile/src/features/trail/services/trailService.ts`

## Orcamento de contexto

- 11 fontes
- estrategia de reducao: mudar apenas services e utilitario de rede compartilhado; sem tocar auth, navegacao, design system ou backend

## Criterios de aceite

- Perfil, avisos e atividades deixam de exibir erro fatal de conexao quando a falha for `network` ou `timeout`
- Fallback local reutiliza os dados demo existentes nessas features
- Erros funcionais da API continuam propagados para a UI
- Mutacoes seguem exigindo API real
- Cobertura de regressao adicionada para o criterio de fallback

## Fora de escopo

- Persistencia offline
- Cache entre sessoes
- Mudancas de contrato/backend
- Ajustes visuais

## Dependencias

- Task 120
- Task 124

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Criado utilitario compartilhado para decidir fallback local apenas em falha de rede/timeout
- `profileService`, `notificationsService.list` e `trailService.getTodayTrail` passaram a degradar para dados demo nessas falhas
- Mutacoes de `notifications` e `trail` continuam sem fallback para nao mascarar erro real de escrita
- Cobertura de regressao adicionada para o helper de fallback

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`
- Contexto sob demanda carregado: contrato dos endpoints do responsavel, docs mobile `ARCHITECTURE.md`/`CODE_STYLE.md`/`QA.md`, handoffs `TASK-120` e `TASK-124`, `env.ts`, camada `shared/network` e services de profile/notifications/trail
- Fontes evitadas: backend, web, auth visual, tab bar, design system documental completo

## Handoff

- `.agents/state/handoffs/TASK-125.md`

## Arquivos alterados

- `mobile/src/shared/network/shouldFallbackToDemoData.ts`
- `mobile/src/shared/network/shouldFallbackToDemoData.test.ts`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/notifications/services/notificationsService.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `tasks/change-requests/125-resiliencia-api-telas-responsavel-mobile.md`
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-125.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- Validar em dispositivo fisico se o fallback atende a expectativa operacional quando a API local estiver fora do ar
- Se a meta for sempre usar dados reais, investigar em etapa separada a causa raiz da indisponibilidade da API no ambiente do usuario

## Status final

done
