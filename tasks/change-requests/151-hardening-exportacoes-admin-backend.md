# Task 151 - Hardening de exportacoes e consultas admin no backend

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1admin~1professionals-tree`
- `contracts/openapi.yaml#/paths/~1admin~1reports~1professionals~1export`
- `contracts/openapi.yaml#/paths/~1admin~1reports~1audit-logs~1export`

## Modo de execucao

single-stack

## Slice vertical

- Slice 025 - Hardening de exportacoes e consultas admin no backend
- `tasks/slices/025-hardening-exportacoes-admin-backend.md`

## Objetivo

Aplicar os ajustes do code review em `ajustes_backend.md` para endurecer as exportacoes CSV administrativas e reduzir risco de degradação na montagem da arvore profissional.

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/151-hardening-exportacoes-admin-backend.md`
- `tasks/slices/025-hardening-exportacoes-admin-backend.md`
- `.agents/state/handoffs/TASK-021.md`
- `.agents/state/handoffs/TASK-085.md`

## Contexto sob demanda

- `ajustes_backend.md`
- `contracts/openapi.yaml`
- `backend/AGENTS.md`
- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `backend/docs/ai/QA.md`
- `backend/src/modules/admin/*`
- `backend/src/modules/users/*`
- `backend/src/modules/guardians/*`
- `backend/src/modules/patients/*` somente se a estrutura dos vinculos exigir leitura adicional

## Orçamento de contexto

- medio: concentrado em admin/users/guardians e contrato admin
- bloquear se a correcao exigir redesenhar a rota consumida pelo front, refatorar persistencia geral ou alterar UI

## Dependencias

- Task 021
- Task 085
- Task 089

## Validacao esperada

- `npm run lint`
- `npm run test`
- `npm run test:e2e`
- `npm run build`

## Observacao

- Origem: code review consolidado em `ajustes_backend.md`
- Escopo validado: 4 pontos concentrados no modulo admin/backend

## Resultado da execucao

- `UsersService.list` passou a usar paginação real no repositório, reduzindo carga para leituras administrativas em lote
- a composição da árvore de profissionais e da exportação CSV passou a iterar profissionais em páginas internas de 100, sem reaproveitar uma carga total monolítica
- o módulo admin passou a resolver crianças vinculadas em lote via `findChildrenByIds`, removendo o N+1 anterior
- `linkedAt` agora é convertido defensivamente para ISO na exportação de profissionais, sem `TypeError` quando vier ausente ou stringificado
- a exportação de logs administrativos passou a escrever o CSV em stream HTTP incremental, lendo o repositório em páginas com cursor em vez de montar um `Buffer` único em memória
- o utilitário CSV passou a tratar instâncias de `Date` explicitamente, evitando aspas triplas em serialização futura
- o teste e2e de `/api/users` foi alinhado ao fluxo autenticado atual da API e endurecido com e-mails únicos por execução para evitar conflito com dados persistidos

## Contexto utilizado

- `ajustes_backend.md`
- `contracts/openapi.yaml`
- `backend/AGENTS.md`
- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/CODE_STYLE.md`
- `backend/docs/ai/QA.md`
- `.agents/state/handoffs/TASK-021.md`
- `.agents/state/handoffs/TASK-085.md`
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

- `npm run lint` — ok
- `npm run test` — ok (16 suites, 59 testes)
- `npm run test:e2e` — ok (1 suite, 1 teste)
- `npm run build` — ok

## Pendencias pos-task

- avaliar em task futura se `/admin/professionals-tree` deve expor paginação HTTP explícita para o front, já que nesta task o hardening ficou restrito à paginação interna compatível

## Handoff

- `.agents/state/handoffs/TASK-151.md`
- reexecução concluída em `2026-07-23` para fechar o hardening da exportação de audit logs com streaming incremental

## Status final

done
