# Handoff - Task 011

## Task

- identificador: 011
- título: Fluxo multi-etapa de cadastro responsavel na web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 004 - Onboarding responsavel
- objetivo de negócio: UI onboarding responsável/criança/anamnese
- entrega verificável: Wizard web completo
- status do slice: done

## Decisões preservadas

- decisão: wizard 3 etapas + `POST /guardians/register` atômico; sem `setSession`
- motivo: API 010 não retorna tokens; evita liberar dashboard
- impacto: redirect `/assinatura` com state (`email`, `patientCode`, `audience: 'responsavel'`)

- decisão: pergunta 6 multi-select no front; `patientCode` exibido no gate
- motivo: requisitos + instrução da task
- impacto: personalização no backend; responsável vê código da criança

- decisão: sem prints — seguir DS documental + padrão do cadastro profissional
- motivo: lacuna visual declarada
- impacto: AuthLayout/Input/Button/tokens; desvio documentado

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/011-fluxo-cadastro-responsavel-web.md`
- `tasks/slices/004-onboarding-responsavel-anamnese.md`
- `.agents/state/handoffs/TASK-010.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | wizard/estados |
| openapi guardians/register | API | payload |
| ARCHITECTURE/ACCESSIBILITY | front | estrutura + a11y |
| requirements 002 | regras | Q1–8 |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile / backend docs | single-stack front |

## Resultado por stack

- front-end: done

## Arquivos alterados

- `front-end/src/pages/Auth/RegisterGuardian/**`
- `front-end/src/types/guardian.ts`, services/adapters, utils cpf/age
- `front-end/src/pages/Auth/SubscriptionGate/**` (patientCode + audience)
- `front-end/src/routes/index.tsx`
- task/index/slice/handoff

## Validações executadas

- lint/test/build: ok (11 tests)

## Pendências ou bloqueios

- Tasks 012/013 assinatura real; gate no login; montagem de trilha

## Próxima ação sugerida

- Executar Task 012 (`tasks/012-api-assinatura-gate.md`)

## Próximo contexto recomendado

- task 012 + openapi subscription/access + backend docs

## Contexto que não deve ser carregado na próxima etapa

- fonte: design-system mobile / mobile docs
- motivo: Task 012 é back (salvo se a task declarar UI)
