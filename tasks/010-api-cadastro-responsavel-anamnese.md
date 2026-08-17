# Task 010 - API cadastro responsavel, crianca, anamnese e codigo unico

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

- `contracts/openapi.yaml#/paths` register guardian/child/anamnese

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

Fluxo central do responsavel e personalizacao.

### O que

Multi-etapa: responsavel, crianca, anamnese; codigo unico; sugestao pela pergunta 6.

### Comportamento esperado

- Bloqueia menor
- Codigo unico
- Anamnese
- Categorias trilha

### Fora de escopo

- Pagamento
- Mobile

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: publico no registro
- Casos de erro: menoridade; CPF; anamnese
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: catalogo vazio

## Especificacao tecnica

### Deve

- Perguntas 1-8
- Sem login da crianca

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada


## Entradas

- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/`

## Dependencias

- Task 005

## Slice vertical

### Identificador do slice

Slice 004 - Onboarding responsavel

### Arquivo do slice

- `tasks/slices/004-onboarding-responsavel-anamnese.md`

### Objetivo de negócio

Onboarding responsavel.

### Entrega verificável do slice

API completa.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/004-onboarding-responsavel-anamnese.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- Codigo unico
- Maioridade
- Pergunta 6 persistida

## Instrucoes de implementacao

- Trilha sugerida pode ficar pendente

## Validacao esperada

- npm run test
- npm run lint

## Entregaveis esperados

- API + contrato

## Riscos ou ambiguidades

- Unicidade CPF

## Resultado da execucao

### Resumo por stack

- **backend**: `POST /api/guardians/register` atômico (responsável + criança + anamnese 1–8); maioridade; CPF único; `patientCode` único; `suggestedTrailCategories` da pergunta 6; `accessGranted: false`.
- **contrato**: path/schemas Guardians adicionados.

### Relação com o slice

- Entrega API do Slice 004 concluída. Slice permanece `in_progress` até Task 011 (wizard web).

### Decisões técnicas

- Registro atômico (wizard UI pode coletar etapas e enviar uma vez).
- Criança sem user/login; só entidade `children` + código `EVO-XXXXXX`.
- CPF: normalização + dígitos verificadores; unicidade em guardian e child.
- Trilha: apenas categorias sugeridas persistidas; montagem de conteúdo pendente (catálogo).
- Nenhuma dependência nova.

### Trade-offs

- Sem endpoints step-by-step separados nesta fase.
- CPF guardian ≠ child obrigatório.

### Contrato

- `POST /guardians/register` → 201 `GuardianRegistrationResponse`.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/004-onboarding-responsavel-anamnese.md`
- handoff `TASK-009.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 002 §3 | regras | campos + Q1–8 |
| openapi | API | path novo |
| ARCHITECTURE/SECURITY | back | módulo Nest |

### Evitado

- design-system / front / mobile
- requirements além da seção de cadastro/anamnese

## Handoff

- Caminho: `.agents/state/handoffs/TASK-010.md`
- Decisões: registro atômico; patientCode; Q6 → suggestedTrailCategories
- Próximo: Task 011 wizard web
- Pendências: UI; montagem trilha; pagamento

## Arquivos alterados

### contrato

- `contracts/openapi.yaml`

### backend

- `backend/src/modules/guardians/**`
- `backend/src/database/migrations/1730000000000-CreateGuardianOnboardingTables.ts`
- `backend/src/database/typeorm.datasource.ts`
- `backend/src/app.module.ts`

### governança

- `tasks/010-api-cadastro-responsavel-anamnese.md`
- `tasks/000-index.md`
- `tasks/slices/004-onboarding-responsavel-anamnese.md`
- `.agents/state/handoffs/TASK-010.md`

## Validacoes executadas

- `npm run lint` — ok
- `npm run test` — ok (23 tests)
- `npm run typecheck` — ok

## Aderencia ao design system

- nao se aplica

## Pendencias pos-task

- Task 011 — wizard web
- Montagem automática de trilha a partir do catálogo
- Gate de assinatura (slice 005)

## Status final

done
