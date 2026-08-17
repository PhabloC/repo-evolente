# Handoff - Task 126

## Identificador

- Task 126 - Exigir dados reais nas telas do responsavel mobile
- `tasks/change-requests/126-exigir-dados-reais-telas-responsavel-mobile.md`

## Slice vertical

- Slice 023 - Resiliencia da API no app do responsavel
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`

## Status final

done

## Decisoes preservadas

- Perfil, avisos e atividades do responsavel nao podem cair para mock automaticamente quando `EXPO_PUBLIC_USE_DEMO_DATA=false`
- Dados demo permanecem apenas por opt-in explicito de ambiente
- Ausencia de `EXPO_PUBLIC_API_URL` com demo desligado vira erro explicito de configuracao

## Contexto efetivamente usado

- Task 126, Slice 023, handoffs `TASK-120` e `TASK-125`, `contracts/openapi.yaml`, docs mobile `ARCHITECTURE.md`/`CODE_STYLE.md`/`QA.md`, `env.ts`, `shared/network` e services de `profile`/`notifications`/`trail`

## Arquivos alterados

- `mobile/src/shared/network/requireRealApi.ts`
- `mobile/src/shared/network/requireRealApi.test.ts`
- `mobile/src/shared/network/shouldFallbackToDemoData.ts` (removido)
- `mobile/src/shared/network/shouldFallbackToDemoData.test.ts` (removido)
- `mobile/src/config/env.ts`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/notifications/services/notificationsService.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `tasks/change-requests/126-exigir-dados-reais-telas-responsavel-mobile.md`
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok (10 suites, 21 testes)

## Pendencias

- Validar no dispositivo fisico se a API em `http://192.168.2.143:3000/api` responde na mesma rede
- Se as telas continuarem falhando, investigar backend/infra em task separada

## Proximo contexto recomendado

- `mobile/src/config/env.ts` e `mobile/src/shared/network/requireRealApi.ts` se houver nova necessidade de endurecer ambientes
