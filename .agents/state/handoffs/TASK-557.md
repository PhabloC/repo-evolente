# Handoff - Task 557

## Task

- identificador: `557`
- título: API: cadastro só do responsável e criação autenticada de filhos
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 049
- objetivo de negócio: cadastro público só do responsável
- entrega verificável: `POST /guardians/register` sem filho; `POST /guardians/me/children` autenticado

## Decisões preservadas

- Register público: só `guardian`; `kinship` do perfil fica `null`; sem tokens
- Filho autenticado exige `accessGranted`; `registerFamily` pula o gate para `POST /patients`
- Evento `guardian.child.created` dispara o equivalente ao filho no register antigo
- Parentesco canônico em `Child.kinship`; migration 187 faz backfill + nullable no perfil

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/557-api-cadastro-responsavel-e-filhos.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `.agents/state/handoffs/TASK-556.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | contrato 556 | DTOs/respostas |
| `backend/src/modules/guardians/**` | implementação | register/filho |
| `backend/src/modules/patients/**` | atomicidade | `registerFamily` |
| `backend/docs/ai/ARCHITECTURE.md` | padrão de camadas | fluxo |
| `backend/docs/ai/SECURITY.md` | guards/DTO | authz |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end / mobile | fora da task |
| design-system | sem UI |

## Resultado por stack

- front-end ou next-js: não alterado
- backend: register sem filho + POST children + patients atômico
- mobile: não alterado

## Arquivos alterados

- `backend/src/modules/guardians/**` (DTO, entidades, repos, service, controller, specs, eventos)
- `backend/src/modules/patients/**`
- `backend/src/modules/admin/admin.service.ts` (`kinship` em `toPublicChild`)
- `backend/src/database/migrations/1870000000000-AddKinshipToChildrenAndNullableGuardianKinship.ts`

## Validações executadas

- jest guardians + patients: passou
- eslint dos arquivos do módulo: passou (exceto CRLF pré-existente em `anamnese.types.ts`)

## Pendências ou bloqueios

- aplicar migration 187 no Postgres local
- Slice 049 continua `todo` até a Task 558

## Próxima ação sugerida

- executar Task 558 (wizard web)

## Próximo contexto recomendado

- `tasks/change-requests/558-wizard-cadastro-so-responsavel-web.md`
- `front-end/src/pages/Auth/RegisterGuardian/**`
- `front-end/src/services/guardians/guardianService.ts`
- `front-end/src/types/guardian.ts`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `design-system/front/Design_System_Evolente_Desktop.md` (auth/wizard)

## Contexto que não deve ser carregado na próxima etapa

- mobile
- dashboard do responsável (Task 559)
- cadastro autenticado de filho (Task 560)
- backend além do contrato já fechado
