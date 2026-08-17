# Task 002 - Fundacao backend de identidade e papeis

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

- `contracts/openapi.yaml#/paths` auth/users/roles

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

Base de usuarios/papeis antes dos fluxos.

### O que

Modelos e modulo de identidade com roles e status ativo/inativo.

### Comportamento esperado

- Usuario com role
- Conta inativa distinguivel

### Fora de escopo

- Login completo
- Cadastros
- Pagamento

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: roles master/profissional/responsavel
- Casos de erro: role invalida
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: usuario sem role

## Especificacao tecnica

### Deve

- Seguir ARCHITECTURE/SECURITY do backend
- Persistir role e status

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Exclusao fisica

## Entradas

- `tasks/001-contrato-openapi-base.md`
- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/SECURITY.md`
- `contracts/openapi.yaml`

## Dependencias

- Task 001

## Slice vertical

### Identificador do slice

Slice 001 - Fundacao e contrato base

### Arquivo do slice

- `tasks/slices/001-fundacao-contrato-base.md`

### Objetivo de negócio

Fundar identidade.

### Entrega verificável do slice

Modelos no backend.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/001-fundacao-contrato-base.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| API | `contracts/openapi.yaml` | API | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |
| NFR | `requirements/003-requisitos-nao-funcionais.md` | LGPD/storage | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Modelo User com role/status
- Seed master documentado

## Instrucoes de implementacao

- Apenas fundacao
- Hooks para auditoria futura

## Validacao esperada

- npm run lint
- npm run test
- npm run build

## Entregaveis esperados

- Modulo identidade

## Riscos ou ambiguidades

- Auth propria por requisito

## Resultado da execucao

Fundacao de identidade no backend alinhada ao OpenAPI: roles Evolente, status active/inactive, inativacao sem exclusao fisica, seed master documentado e hooks de auditoria via eventos.

### Por stack

- backend: `UserEntity` com `UserRole` (master/profissional/responsavel) e `UserStatus` (active/inactive); migration atualizada; `PATCH /users/:id/status`; `GET /roles`; remocao de DELETE fisico; evento `user.status_changed`; seed `npm run seed:master`

### Slice

- Slice 001 permanece `in_progress`: Task 002 done; Tasks 003/004 ainda planned
- Entrega parcial: modelos de identidade no backend

### Decisoes tecnicas

- Roles alinhadas ao contrato (substituem admin/member do scaffold)
- Status default `active`; inativacao via update + evento de auditoria
- Conta inativa rejeitada em `validateCredentials` (Forbidden)
- Seed master idempotente via env (`MASTER_SEED_*`)
- Sem novas dependencias npm

### Trade-offs

- Login completo e cadastros permanecem fora (auth scaffold existente so ajustado para status)
- Auditoria completa (historico persistido) fica para tasks futuras; hook de evento ja emite

### Contrato

- Alinhado a schemas Role/UserStatus/User e paths users/roles

### Referencia visual

- nao se aplica

## Contexto utilizado

### Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, `tasks/slices/001-fundacao-contrato-base.md`, handoff Task 001

### Contexto sob demanda carregado

- `contracts/openapi.yaml` — Role/UserStatus/User
- `backend/docs/ai/ARCHITECTURE.md` — camadas e seeds
- `backend/docs/ai/SECURITY.md` — hash, DTO, migrations
- `requirements/003-requisitos-nao-funcionais.md` — LGPD/auditoria/perfis

### Contexto nao carregado

- design-system (sem UI)
- front-end/mobile docs
- requirements 001/002 (cobertos pelo handoff 001 + contrato)

## Handoff

- `.agents/state/handoffs/TASK-002.md`
- Proximo contexto: Task 003 (shell web) ou Task 005 (auth completa no slice 002), conforme ordem do backlog

## Arquivos alterados

- `backend/src/modules/users/entities/user.entity.ts`
- `backend/src/modules/users/dto/create-user.dto.ts`
- `backend/src/modules/users/dto/update-user.dto.ts`
- `backend/src/modules/users/dto/update-user-status.dto.ts`
- `backend/src/modules/users/users.repository.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/modules/users/users.typeorm.repository.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `backend/src/modules/users/users.controller.ts`
- `backend/src/modules/users/roles.controller.ts`
- `backend/src/modules/users/users.module.ts`
- `backend/src/modules/users/events/user.events.ts`
- `backend/src/modules/users/events/users-events.listener.ts`
- `backend/src/patterns/adapters/analyticsAdapter.ts`
- `backend/src/database/migrations/1700000000000-CreateUsersTable.ts`
- `backend/src/database/seeds/master-user.seed.ts`
- `backend/src/database/seeds/README.md`
- `backend/.env.example`
- `backend/package.json`
- `backend/docs/ai/BACKEND_PATTERNS.md`
- `tasks/002-fundacao-backend-identidade.md`
- `tasks/000-index.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `.agents/state/handoffs/TASK-002.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — 4 passed
- `npm run build` — ok

## Aderencia ao design system

- nao se aplica (sem UI)

## Pendencias pos-task

- Login completo / recuperacao de senha (Slice 002 / Task 005+)
- Persistencia de historico de auditoria (hoje so evento/log)
- Shells web/mobile (Tasks 003/004)
- Rodar migration + `npm run seed:master` em ambiente com Postgres

## Status final

done
