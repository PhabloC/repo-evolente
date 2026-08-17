# Handoff - Task 021

## Task

- identificador: 021
- título: API de administração master
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 009 - Admin master
- objetivo de negócio: Métricas, usuários, planos, logs e árvore pacientes
- entrega verificável: API admin (UI nas tasks 022/023)
- status do slice: in_progress

## Decisões preservadas

- decisão: paths `/admin/*` novos no OpenAPI (não existiam)
- motivo: contrato citava admin sem paths
- impacto: UI 022/023 deve consumir esses endpoints

- decisão: `/users` e `/roles` restritos a master + paginação/filtros
- motivo: alinhar OpenAPI e segurança
- impacto: clientes não-master recebem 403

- decisão: bloquear auto-inativação do master
- motivo: caso de borda da task
- impacto: 403 `CANNOT_INACTIVATE_SELF`

- decisão: planos = gestão de `subscriptions` (sem entidade Plan)
- motivo: valores/gateway TBD
- impacto: PATCH status sincroniza `accessGranted`

- decisão: auditoria em `admin_audit_logs` + listener de eventos de usuário
- motivo: NFR de logs acessíveis ao master
- impacto: migration 178…

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/021-api-admin-master.md`
- `tasks/slices/009-administracao-master.md`
- handoff TASK-020

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/003 | regras/NFR | escopo admin + auditoria |
| openapi | API | criação paths Admin |
| backend docs/ai | back | arquitetura/segurança |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front/mobile/DS | sem UI |

## Resultado por stack

- backend: done

## Arquivos alterados

- `backend/src/modules/admin/**`
- users/patients/subscriptions/trails/guardians/professionals (extensões)
- `contracts/openapi.yaml`
- migration audit logs
- task/index/slice/handoff

## Validações executadas

- lint + test backend: ok

## Pendências ou bloqueios

- Task 022 (web) e 023 (mobile) para UI
- Planos com valores definitivos TBD

## Próxima ação sugerida

- Executar Task 022 (`tasks/022-dashboard-master-web.md`)

## Próximo contexto recomendado

- task 022 + DS desktop dashboard master + openapi Admin + front-end docs/ai

## Contexto que não deve ser carregado na próxima etapa

- fonte: implementação interna de repositórios admin além do contrato
- motivo: UI só precisa dos paths/schemas OpenAPI
