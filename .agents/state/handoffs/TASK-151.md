# Handoff - Task 151

## Identificador

- Task 151 - Hardening de exportacoes e consultas admin no backend
- `tasks/change-requests/151-hardening-exportacoes-admin-backend.md`

## Slice vertical

- Slice 025 - Hardening de exportacoes e consultas admin no backend
- `tasks/slices/025-hardening-exportacoes-admin-backend.md`

## Status final

done

## Decisoes preservadas

- `UsersService.list` passou a depender de paginação real no repositório, sem carregar sempre todos os usuários para depois fatiar em memória
- a árvore de profissionais e a exportação de vínculos iteram profissionais em lotes internos de 100, preservando compatibilidade da rota atual
- crianças vinculadas passaram a ser resolvidas em lote por `findChildrenByIds`, eliminando o N+1 anterior no módulo admin
- `linkedAt` na exportação de profissionais agora tolera `Date`, string, `null` ou `undefined`, retornando ISO válido ou string vazia
- a exportação de logs administrativos usa stream HTTP incremental com paginação por cursor no repositório, evitando montar um CSV completo em memória
- o utilitário CSV trata `Date` explicitamente antes de cair em `JSON.stringify`
- o e2e de `/api/users` foi atualizado para criar um master, autenticar, exercer o fluxo real protegido por JWT e evitar conflitos usando e-mails únicos por execução

## Contexto efetivamente usado

- `ajustes_backend.md`
- Task 151 e Slice 025
- handoffs `TASK-021` e `TASK-085`
- `contracts/openapi.yaml`
- `backend/AGENTS.md`
- `backend/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `QA.md`
- `backend/src/modules/admin/*`
- `backend/src/modules/users/*`
- `backend/src/modules/guardians/*`
- `backend/test/app.e2e-spec.ts`

## Arquivos alterados

- `backend/src/modules/admin/admin-audit.in-memory.repository.ts`
- `backend/src/modules/admin/admin-audit.repository.ts`
- `backend/src/modules/admin/admin-audit.typeorm.repository.ts`
- `backend/src/modules/admin/admin.service.ts`
- `backend/src/modules/admin/admin.service.spec.ts`
- `backend/src/modules/admin/admin.controller.ts`
- `backend/src/modules/admin/utils/admin-report-csv.ts`
- `backend/src/modules/admin/utils/admin-report-csv.spec.ts`
- `backend/src/modules/guardians/guardians.repository.ts`
- `backend/src/modules/guardians/guardians.in-memory.repository.ts`
- `backend/src/modules/guardians/guardians.typeorm.repository.ts`
- `backend/src/modules/users/users.repository.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.typeorm.repository.ts`
- `backend/test/app.e2e-spec.ts`

## Validacoes executadas

- `npm run lint` ok
- `npm run test` ok (16 suites, 59 testes)
- `npm run test:e2e` ok
- `npm run build` ok

## Pendencias

- decidir em task futura se `/admin/professionals-tree` deve ganhar paginação HTTP explícita para o front

## Proximo contexto recomendado

- `backend/src/modules/admin/admin.service.ts`
- `backend/src/modules/admin/admin-audit.repository.ts`
- `backend/src/modules/admin/admin.controller.ts`

## Contexto que nao deve ser carregado

- design-system, mobile e telas web, salvo se uma task futura realmente expandir o contrato HTTP da árvore admin
