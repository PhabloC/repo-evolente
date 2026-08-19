# Task 557 - API: cadastro só do responsável e criação autenticada de filhos

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

- `contracts/openapi.yaml#/paths/~1guardians~1register`
- `contracts/openapi.yaml#/paths/~1guardians~1me~1children`

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

nao se aplica

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- `nao se aplica`

## Contexto de negocio

### Por que

A API hoje cria responsável, criança e anamnese no mesmo POST público.

### O que

Separar: register cria só o responsável; um POST autenticado cria cada filho com anamnese, código único e categorias de trilha.

### Comportamento esperado

- `POST /guardians/register` valida maioridade, CPF e senha forte; cria `User(role=responsavel)` + `GuardianProfile(accessGranted=false)` **sem** child
- Não retorna tokens
- `POST /guardians/me/children` exige JWT `responsavel` + `AccessGrantedGuard`
- Cria `Child` com `patientCode` único (`EVO-…`), anamnese 1–8, `suggestedTrailCategories` da pergunta 6
- CPF da criança ≠ CPF do responsável e único na base
- Evento de domínio ao criar filho (para trilha sugerida), equivalente ao `guardian.registered` no que diz respeito ao filho
- Listagem `GET /guardians/me/children` retorna todos os filhos
- `POST /patients` permanece atômico

### Fora de escopo

- UI
- Auto-montar a trilha semanal no POST do filho (manter suggest/categorias; montagem continua no fluxo já existente)
- Cadastro de filho sem anamnese

## Slice vertical

### Identificador do slice

Slice 049 - Cadastro público só do responsável

### Arquivo do slice

- `tasks/slices/049-cadastro-responsavel-sem-filho.md`

Também habilita o Slice 050.

## Permissoes

- Register público
- POST/GET children: responsável com assinatura

## Casos de erro mapeados

- 400 menoridade, CPF inválido, anamnese incompleta, pergunta 6 vazia, parentesco curto
- 401/403 sem sessão ou sem `accessGranted`
- 409 CPF/e-mail duplicado; falha ao alocar `patientCode`
- Register com payload antigo (`child`/`anamnese`) → 400

## Decisoes humanas confirmadas

- Cadastro público só do responsável
- Cada filho tem código único, perfil e trilha individualizada

## Premissas adotadas pela IA

- `kinship` obrigatório no POST do filho; no perfil do responsável fica opcional (valor legado preservado)
- Sem teto de filhos
- Não quebrar contas antigas que já têm um `Child`

## Criterios de aceite

- [x] Register sem filho cobre o contrato da Task 556
- [x] POST children cria N filhos para o mesmo `guardianUserId`
- [x] Cada filho tem `patientCode` único e anamnese persistida
- [x] Testes unitários do service cobrem: register sem child; dois filhos; CPF duplicado; acesso sem pagamento
- [x] `POST /patients` inalterado no comportamento atômico

## Casos de borda

- Responsável pago sem filhos
- Dois filhos com CPFs distintos
- Tentativa de criar filho antes do pagamento

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 049, Task 556
- handoff da Task 556 quando existir

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Contrato | `contracts/openapi.yaml` paths/schemas da Task 556 | aderência | sim |
| Modulo | `backend/src/modules/guardians/**` | implementação | sim |
| Pacientes | `backend/src/modules/patients/**` se `POST /patients` reusar register | não quebrar | sim se compartilhado |
| Docs back | `backend/docs/ai/` ARCHITECTURE/SECURITY | padrões | sim |

## Orçamento de contexto

- medio
- estrategia de reducao: só modulo guardians (+ patients se o createPatient chamar register)

## Dependencias

- Task 556

## Resultado da execucao

### Resumo por stack

- **backend**: `POST /guardians/register` cria só usuário + `GuardianProfile` (`kinship` null, `accessGranted` false), sem tokens e sem filho. `POST /guardians/me/children` cria filho + anamnese + `patientCode` com JWT `responsavel` + `AccessGrantedGuard`. `POST /patients` permanece atômico via `registerFamily` (register + filho sem exigir pagamento). Migration `1870000000000` adiciona `children.kinship` e torna `guardian_profiles.kinship` nullable.

### Relação com o slice

- Slice 049: API do cadastro público pronta. Slice permanece `todo` (wizard web Task 558 pendente). Também habilita o Slice 050 no backend.

### Decisões técnicas

- Evento `guardian.registered` sem child; novo `guardian.child.created` ao criar filho.
- `createMyChild(..., { requireAccessGranted: false })` só para o fluxo profissional.
- Parentesco canônico em `Child.kinship`; listagem de pacientes espelha `child.kinship || guardian.kinship`.
- Mapper admin `toPublicChild` passou a incluir `kinship`.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 049, handoff Task 556

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` paths `/guardians/register` e `/guardians/me/children` | aderência | DTOs e respostas |
| `backend/src/modules/guardians/**` | implementação | register/filho |
| `backend/src/modules/patients/**` | `POST /patients` reusa register | `registerFamily` |
| `backend/docs/ai/ARCHITECTURE.md` | padrão controller/service/repo | fluxo |
| `backend/docs/ai/SECURITY.md` | DTO + guards | JWT/roles/accessGranted |

### Evitado

- front-end UI, mobile, design-system, montagem de trilha semanal

## Handoff

- Caminho: `.agents/state/handoffs/TASK-557.md`
- Próximo contexto: Task 558 (`front-end/src/pages/Auth/RegisterGuardian/**` + `guardianService.ts`)
- Pendência: rodar a migration `187` no Postgres local se ainda não aplicada

## Arquivos alterados

- `backend/src/modules/guardians/dto/register-guardian.dto.ts`
- `backend/src/modules/guardians/dto/update-my-child.dto.ts`
- `backend/src/modules/guardians/entities/child.entity.ts`
- `backend/src/modules/guardians/entities/guardian-profile.entity.ts`
- `backend/src/modules/guardians/guardians.repository.ts`
- `backend/src/modules/guardians/guardians.in-memory.repository.ts`
- `backend/src/modules/guardians/guardians.typeorm.repository.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.controller.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `backend/src/modules/guardians/events/guardian.events.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/patients/patients.controller.ts`
- `backend/src/modules/patients/patients.service.spec.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `backend/src/modules/trails/trails.service.spec.ts`
- `backend/src/modules/admin/admin.service.ts`
- `backend/src/modules/admin/admin.service.spec.ts`
- `backend/src/database/migrations/1870000000000-AddKinshipToChildrenAndNullableGuardianKinship.ts`
- `tasks/change-requests/557-api-cadastro-responsavel-e-filhos.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-557.md`

## Validacoes executadas

- `npx jest --runInBand --no-coverage src/modules/guardians/guardians.service.spec.ts src/modules/patients/patients.service.spec.ts` — passou (19 testes)
- Specs de reports, trails e admin atualizados para `kinship` / `registerFamily` (execução anterior da sessão: 38 testes no conjunto afetado)
- `npx eslint` nos arquivos alterados do módulo — passou, exceto `anamnese.types.ts` (CRLF pré-existente, fora do escopo)
- `npx tsc --noEmit` — `toPublicChild` do admin corrigido; demais erros de tsc aparentam pré-existentes (bootstrap/csv/e2e)

## Qualidade estrutural

- DTOs novos no módulo `guardians/dto`; evento de filho em `events/`
- Sem utils soltos; persistência continua no repository

## Aderencia ao design system

- Não se aplica (task back)

## Pendencias pos-task

- Rodar `npm run migration:run` no backend contra o Postgres local
- Task 558: wizard web só do responsável

## Status final

done
