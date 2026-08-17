# Task 021 - API de administracao master

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

- `contracts/openapi.yaml#/paths` admin (+ users master)

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- `nao se aplica`

### Regra de aderencia visual

- Sem UI.

## Contexto de negocio

### Por que

Master opera a plataforma.

### O que

Metricas, usuarios inativar/permissoes, planos, logs, pacientes por profissional.

### Comportamento esperado

- Metricas
- Inativar
- Logs
- Arvore por profissional

### Fora de escopo

- Hard delete
- Catalogo

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master
- Casos de erro: 403
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: inativar a si mesmo

## Especificacao tecnica

### Deve

- Auditoria admin
- Sem delete

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada


## Entradas

- `requirements/001-escopo-produto.md`
- `requirements/003-requisitos-nao-funcionais.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/`

## Dependencias

- Tasks 005 e 012

## Slice vertical

### Identificador do slice

Slice 009 - Admin master

### Arquivo do slice

- `tasks/slices/009-administracao-master.md`

### Objetivo de negócio

Admin API.

### Entrega verificável do slice

API admin.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/009-administracao-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |
| NFR | `requirements/003-requisitos-nao-funcionais.md` | LGPD/storage | sim |

## Orçamento de contexto

- Risco alto — fatiar paths se preciso

## Criterios de conclusao

- Metricas
- Inativar
- Logs

## Instrucoes de implementacao

- Monitorar orcamento de contexto

## Validacao esperada

- npm run test
- npm run lint

## Entregaveis esperados

- API admin

## Riscos ou ambiguidades

- Volume de endpoints

## Resultado da execucao

API admin master entregue:

- `GET /admin/metrics` — profissionais ativos, pacientes, vínculos, atividades concluídas, pagamentos
- `GET /admin/audit-logs` — logs de auditoria (eventos de usuário + ações admin)
- `GET /admin/professionals-tree` — árvore profissional → pacientes
- `GET /admin/subscriptions` + `PATCH /admin/subscriptions/:id/status` — gestão de planos/assinaturas (sem hard delete; sincroniza `accessGranted`)
- `/users` e `/roles` endurecidos com `JwtAuthGuard` + `RolesGuard` master; listagem paginada/filtrada; bloqueio de auto-inativação (`CANNOT_INACTIVATE_SELF`)
- Contrato OpenAPI tag `Admin` + schemas; migration `admin_audit_logs`

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-020.md` (próxima sugerida)

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002/003 | regras/NFR | capacidades master + auditoria |
| openapi | API | paths ausentes → criados |
| backend ARCHITECTURE/SECURITY | back | módulo + guards |

### Contexto não carregado

- front-end / mobile / design-system (sem UI nesta task)

## Handoff

- `.agents/state/handoffs/TASK-021.md`

## Arquivos alterados

### Backend

- `backend/src/modules/admin/**` (módulo novo)
- `backend/src/modules/users/**` (guards master, listagem, self-inactivate)
- `backend/src/modules/patients|subscriptions|trails|guardians|professionals/**` (métodos/exports para agregação admin)
- `backend/src/app.module.ts`
- `backend/src/database/migrations/1780000000000-CreateAdminAuditLogsTable.ts`

### Contrato

- `contracts/openapi.yaml` (tag Admin + paths/schemas)

### Governança

- esta task, `tasks/000-index.md`, `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-021.md`

## Validacoes executadas

- `npm run lint` ok
- `npm run test` ok (suite completa)

## Aderencia ao design system

- nao se aplica (API only)

## Pendencias pos-task

- UI web Task 022 e mobile Task 023 consomem esta API
- Valores definitivos de planos/gateway permanecem TBD (status operável)

## Status final

done
