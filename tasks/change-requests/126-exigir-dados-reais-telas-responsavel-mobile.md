# Task 126 - Exigir dados reais nas telas do responsavel mobile

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

Garantir que atividades, perfil e avisos do app do responsavel usem apenas dados reais quando o modo demo estiver desligado, removendo fallback automatico para mocks em falhas de rede ou configuracao.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/126-exigir-dados-reais-telas-responsavel-mobile.md`
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`

## Contexto sob demanda

- `contracts/openapi.yaml`
- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `mobile/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-120.md`
- `.agents/state/handoffs/TASK-125.md`
- `mobile/src/config/env.ts`
- `mobile/src/shared/network/`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/notifications/services/notificationsService.ts`
- `mobile/src/features/trail/services/trailService.ts`

## Orcamento de contexto

- 11 fontes
- estrategia de reducao: restringir a env, rede compartilhada e services de leitura do responsavel; sem tocar backend, UI ou navegacao

## Criterios de aceite

- Perfil, avisos e atividades usam dados demo somente quando `EXPO_PUBLIC_USE_DEMO_DATA=true`
- Falha de rede/timeout deixa de cair para mock automaticamente
- Ausencia de `EXPO_PUBLIC_API_URL` com demo desligado deixa erro explicito em vez de mock
- Cobertura de regressao adicionada para a regra de uso de dados reais

## Fora de escopo

- Alteracoes de backend
- Mudancas visuais
- Offline/cache persistente

## Dependencias

- Task 120
- Task 125

## Validacao esperada

- `npm run lint`
- `npm run typecheck`
- `npm run test`

## Resultado da execucao

- Removido o fallback automatico para mocks por erro de rede nas leituras de perfil, avisos e atividades
- Criado helper compartilhado para exigir configuracao explicita da API quando o modo demo estiver desligado
- Dados demo permaneceram apenas para modo demo intencional (`EXPO_PUBLIC_USE_DEMO_DATA=true`)
- Cobertura de regressao adicionada para a nova regra de configuracao real

## Contexto utilizado

- Contexto minimo lido: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task e `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`
- Contexto sob demanda carregado: contrato dos endpoints do responsavel, docs mobile `ARCHITECTURE.md`/`CODE_STYLE.md`/`QA.md`, handoffs `TASK-120` e `TASK-125`, `env.ts`, camada `shared/network` e services de `profile`/`notifications`/`trail`
- Fontes evitadas: backend, auth, design system completo e navegacao

## Handoff

- `.agents/state/handoffs/TASK-126.md`

## Arquivos alterados

- `mobile/src/shared/network/requireRealApi.ts`
- `mobile/src/shared/network/requireRealApi.test.ts`
- `mobile/src/shared/network/shouldFallbackToDemoData.ts` (removido)
- `mobile/src/shared/network/shouldFallbackToDemoData.test.ts` (removido)
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/notifications/services/notificationsService.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `tasks/change-requests/126-exigir-dados-reais-telas-responsavel-mobile.md`
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-126.md`

## Validacoes executadas

- `npm run lint` - ok
- `npm run typecheck` - ok
- `npm run test` - ok

## Pendencias pos-task

- Validar no dispositivo fisico se a API local em `http://192.168.2.143:3000/api` esta acessivel na mesma rede
- Se continuar falhando, investigar backend/infra em task separada

## Status final

done
