# Task 008 - API de cadastro de profissional

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

- `contracts/openapi.yaml#/paths` register professional

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

Profissional cria conta antes do pagamento.

### O que

Cadastro individual/clinica; sem assinatura ativa.

### Comportamento esperado

- Cria role profissional
- Clinica condicional
- Nao libera acesso

### Fora de escopo

- Checkout

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: publico
- Casos de erro: e-mail duplicado; clinica
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: registro opcional

## Especificacao tecnica

### Deve

- Campos do requirements/002
- Multi-especialidade

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Exigir so fono

## Entradas

- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/`

## Dependencias

- Task 005

## Slice vertical

### Identificador do slice

Slice 003 - Onboarding profissional

### Arquivo do slice

- `tasks/slices/003-onboarding-profissional.md`

### Objetivo de negócio

Cadastro profissional.

### Entrega verificável do slice

API cadastro.

### Fora do slice

- UI
- Pagamento

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/003-onboarding-profissional.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- Individual e clinica testados

## Instrucoes de implementacao

- Campos clinica minimos (razao social, CNPJ, telefone) como premissa

## Validacao esperada

- npm run test
- npm run lint

## Entregaveis esperados

- API + contrato

## Riscos ou ambiguidades

- Campos clinica TBD

## Resultado da execucao

### Resumo por stack

- **backend**: `POST /api/professionals/register` cria user `profissional` + perfil com multi-especialidade, clínica condicional e `accessGranted: false`.
- **contrato**: path/schemas de registro profissional adicionados em `contracts/openapi.yaml`.

### Relação com o slice

- Entrega API do Slice 003 concluída. Slice permanece `in_progress` até Task 009 (fluxo web).

### Decisões técnicas

- Premissa clínica: `legalName` (razão social), `cnpj` (14 dígitos normalizados), `phone`.
- Especialidades como array livre (não restrito a fono).
- Conta `active` para permitir login/pagamento futuro; acesso completo controlado por `accessGranted: false`.
- CNPJ: validação de formato (14 dígitos), sem lib externa.
- Nenhuma dependência nova.

### Trade-offs

- Campos clínicos além do mínimo ficam para evolução futura (risco TBD da task).
- Gate de assinatura (slice 005) consumirá `accessGranted`.

### Contrato

- `POST /professionals/register` → 201 `ProfessionalRegistrationResponse`; 400/409.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/003-onboarding-profissional.md`
- handoff `TASK-007.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002 | regras | campos cadastro |
| openapi | API | path novo |
| ARCHITECTURE/SECURITY | back | módulo + DTO + hash |

### Evitado

- design-system / front / mobile (sem UI)

## Handoff

- Caminho: `.agents/state/handoffs/TASK-008.md`
- Decisões: accessGranted false; clínica mínima; multi-especialidade
- Próximo contexto: Task 009 (fluxo web cadastro profissional)
- Pendências: UI web; pagamento/gate

## Arquivos alterados

### contrato

- `contracts/openapi.yaml`

### backend

- `backend/src/modules/professionals/**`
- `backend/src/database/migrations/1720000000000-CreateProfessionalProfilesTable.ts`
- `backend/src/database/typeorm.datasource.ts`
- `backend/src/app.module.ts`

### governança

- `tasks/008-api-cadastro-profissional.md`
- `tasks/000-index.md`
- `tasks/slices/003-onboarding-profissional.md`
- `.agents/state/handoffs/TASK-008.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok (15 tests)
- `npm run typecheck` — ok

## Aderencia ao design system

- nao se aplica (sem UI)

## Pendencias pos-task

- Task 009 — fluxo cadastro profissional web
- Liberação de `accessGranted` no slice de assinatura
- Campos clínicos adicionais se validados humanamente

## Status final

done
