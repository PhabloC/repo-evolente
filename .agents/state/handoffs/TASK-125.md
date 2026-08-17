# Handoff - Task 125

## Identificador

- Task 125 - Resiliencia da API nas telas do responsavel mobile
- `tasks/change-requests/125-resiliencia-api-telas-responsavel-mobile.md`

## Slice vertical

- Slice 023 - Resiliencia da API no app do responsavel
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`

## Status final

done

## Decisoes preservadas

- Falha `network` ou `timeout` nas leituras do responsavel deve degradar para dados demo em vez de bloquear a tela
- Fallback vale apenas para leitura em `profile`, `notifications.list` e `trail.getTodayTrail`
- Mutacoes continuam exigindo API real para nao mascarar erro de escrita

## Contexto efetivamente usado

- Task 125, Slice 023, handoffs `TASK-120` e `TASK-124`, `contracts/openapi.yaml`, docs mobile `ARCHITECTURE.md`/`CODE_STYLE.md`/`QA.md`, `shared/network` e services de `profile`/`notifications`/`trail`

## Arquivos alterados

- `mobile/src/shared/network/shouldFallbackToDemoData.ts`
- `mobile/src/shared/network/shouldFallbackToDemoData.test.ts`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/notifications/services/notificationsService.ts`
- `mobile/src/features/trail/services/trailService.ts`
- `tasks/slices/023-resiliencia-api-app-responsavel-mobile.md`
- `tasks/change-requests/125-resiliencia-api-telas-responsavel-mobile.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
- `npm run test` ok (10 suites, 22 testes)

## Pendencias

- Validar em dispositivo fisico se o fallback atende ao fluxo esperado quando a API local estiver indisponivel
- Se a operacao exigir sempre dado real, abrir investigacao separada para causa raiz da indisponibilidade da API

## Proximo contexto recomendado

- `mobile/src/shared/network/shouldFallbackToDemoData.ts` e as services do responsavel se houver novo hardening de conectividade
