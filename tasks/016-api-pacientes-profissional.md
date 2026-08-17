# Task 016 - API de pacientes, vinculo e inativacao

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

- `contracts/openapi.yaml#/paths` patients

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

Profissional gerencia so sua arvore.

### O que

CRUD/vinculo/inativar; anamnese; isolamento.

### Comportamento esperado

- Vinculo por codigo
- Inativar
- 403 cross-tenant

### Fora de escopo

- Trilhas
- Delete

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: profissional+assinatura
- Casos de erro: codigo invalido; 403
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: ja vinculado — bloquear

## Especificacao tecnica

### Deve

- Sem delete
- Anamnese no perfil

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Listar globais

## Entradas

- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/SECURITY.md`

## Dependencias

- Tasks 008, 010 e 012

## Slice vertical

### Identificador do slice

Slice 007 - Pacientes

### Arquivo do slice

- `tasks/slices/007-gestao-pacientes-profissional.md`

### Objetivo de negócio

Gestao pacientes.

### Entrega verificável do slice

API isolada.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |
| NFR | `requirements/003-requisitos-nao-funcionais.md` | LGPD/storage | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- Isolamento testado
- Inativar
- Sem delete

## Instrucoes de implementacao

- Criar login responsavel reutilizando regras

## Validacao esperada

- npm run test
- npm run lint

## Entregaveis esperados

- API pacientes

## Riscos ou ambiguidades

- Mono-vinculo premissa

## Resultado da execucao

API de pacientes do profissional entregue em `backend/src/modules/patients/`:

- `GET /patients` — lista isolada por profissional (filtro opcional `status`)
- `POST /patients` — cria responsável+criança+anamnese via `GuardiansService.register` e vincula
- `POST /patients/link` — vínculo por `patientCode` (404 inválido; 409 se já vinculado)
- `GET /patients/:id` — perfil + anamnese (403 cross-tenant)
- `PATCH /patients/:id` — edita dados da criança (sem CPF/código)
- `PATCH /patients/:id/status` — inativa/reativa o vínculo (sem delete)

Guards: JWT + role `profissional` + `AccessGrantedGuard`. Contrato OpenAPI atualizado. Migration `professional_patient_links` com `child_id` UNIQUE (mono-vínculo).

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/007-gestao-pacientes-profissional.md`

### Sob demanda

- `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md`
- `requirements/003-requisitos-nao-funcionais.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/SECURITY.md` + padrões de `contents`/`guardians`/`subscriptions`

## Handoff

- `.agents/state/handoffs/TASK-016.md`

## Arquivos alterados

- `backend/src/modules/patients/**` (módulo completo + spec)
- `backend/src/modules/guardians/guardians.repository.ts`
- `backend/src/modules/guardians/guardians.in-memory.repository.ts`
- `backend/src/modules/guardians/guardians.typeorm.repository.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/database/migrations/1760000000000-CreateProfessionalPatientLinksTable.ts`
- `backend/src/app.module.ts`
- `contracts/openapi.yaml`
- `tasks/016-api-pacientes-profissional.md`
- `tasks/000-index.md`
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-016.md`

## Validacoes executadas

- `cd backend && npm run lint` — ok
- `cd backend && npm run test` — 10 suites / 36 tests ok (isolamento 403, mono-vínculo 409, inativação sem delete)

## Aderencia ao design system

nao se aplica (sem UI)

## Pendencias pos-task

- Task 017 — UI dashboard pacientes web
- Confirmação humana de multi-vínculo (hoje mono via UNIQUE `child_id`)

## Status final

done
