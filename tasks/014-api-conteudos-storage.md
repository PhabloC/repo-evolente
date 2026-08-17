# Task 014 - API de conteudos com storage de midia

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

- `contracts/openapi.yaml#/paths` contents

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

Master publica audio/video.

### O que

CRUD atividades + upload storage (nao no DB).

### Comportamento esperado

- Upload
- Metadados
- RBAC master write / profissional read

### Fora de escopo

- Jogos
- Gamificacao

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: master write; profissional read
- Casos de erro: tipo invalido; storage
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: arquivo grande

## Especificacao tecnica

### Deve

- Storage externo
- Categorias alinhadas pergunta 6

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Blob no DB

## Entradas

- `requirements/002-regras-de-negocio.md`
- `requirements/003-requisitos-nao-funcionais.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/`

## Dependencias

- Task 002

## Slice vertical

### Identificador do slice

Slice 006 - Catalogo

### Arquivo do slice

- `tasks/slices/006-catalogo-conteudos-master.md`

### Objetivo de negócio

Catalogo.

### Entrega verificável do slice

API+storage.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

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

- Midia em storage
- RBAC

## Instrucoes de implementacao

- Storage S3-compativel ou local em dev

## Validacao esperada

- npm run test
- npm run lint

## Entregaveis esperados

- API conteudos

## Riscos ou ambiguidades

- Provider prod TBD

## Resultado da execucao

### Resumo por stack

- **backend**: módulo `ContentsModule` com CRUD de metadados, upload Base64 para `MediaStorageAdapter` (local em dev), categorias = pergunta 6, RBAC via `RolesGuard` (master write / profissional read), inativação sem exclusão.

### Relação com o slice

- Slice 006 permanece aberto até Task 015 (UI catálogo).

### Decisões técnicas

- Storage adapter + `LocalMediaStorageAdapter`; `STORAGE_PROVIDER=s3` documentado mas cai no local até SDK autorizado.
- Sem blob no DB — só `mediaStorageKey` / `mediaUrl` / mime / size.
- Upload JSON Base64 (sem nova dep multer/@types); multipart futuro quando autorizado.
- Categorias = `ANAMNESE_AREA_OPTIONS`.
- `RolesGuard` + `@Roles` reutilizáveis.
- Nenhuma dependência de produção nova.

### Trade-offs

- Base64 em vez de multipart (evita deps tipadas).
- S3 real pendente de decisão/SDK.

### Contrato

- Paths `/contents` adicionados ao OpenAPI.

### Referência visual

- nao se aplica

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 006
- handoff `TASK-013.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002 | regras | metadados/RBAC/categorias |
| requirements 003 | NFR | storage fora do DB |
| openapi | API | paths contents |
| ARCHITECTURE/SECURITY | back | módulo + adapter |

### Evitado

- design-system / front / mobile

## Handoff

- Caminho: `.agents/state/handoffs/TASK-014.md`
- Decisões: local storage; Base64 upload; RolesGuard; categorias Q6
- Próximo contexto: Task 015 UI catálogo
- Pendências: S3 SDK; multipart; UI 015

## Arquivos alterados

### backend

- `backend/src/modules/contents/**`
- `backend/src/common/decorators/roles.decorator.ts`
- `backend/src/common/guards/roles.guard.ts`
- `backend/src/patterns/adapters/media-storage.adapter.ts`
- `backend/src/patterns/adapters/local-media-storage.adapter.ts`
- `backend/src/app.module.ts`
- `backend/src/database/migrations/1750000000000-CreateContentsTable.ts`
- `backend/src/database/typeorm.datasource.ts`
- `backend/.env.example`

### contrato / repo

- `contracts/openapi.yaml`
- `.gitignore` (`.data/`)

### governança

- `tasks/014-api-conteudos-storage.md`
- `tasks/000-index.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-014.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok (30 tests)
- `npm run typecheck` — ok

## Aderencia ao design system

- nao se aplica

## Pendencias pos-task

- Task 015 — UI catálogo master web
- Provider S3-compatível com SDK autorizado
- Multipart upload opcional

## Status final

done
