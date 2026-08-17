# Handoff - Task 010

## Task

- identificador: 010
- título: API cadastro responsavel, crianca, anamnese e codigo unico
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 004 - Onboarding responsavel
- objetivo de negócio: Cadastro multi-etapa responsável/criança/anamnese
- entrega verificável: API completa (UI 011 pendente)
- status do slice: in_progress

## Decisões preservadas

- decisão: `POST /guardians/register` atômico com guardian + child + anamnese
- motivo: API completa sem login da criança entre etapas
- impacto: wizard 011 envia payload único

- decisão: `patientCode` único `EVO-XXXXXX`; criança sem User
- motivo: requisitos + sem login da criança
- impacto: vínculo profissional futuro por código

- decisão: pergunta 6 → `suggestedTrailCategories`; trilha de conteúdo pendente
- motivo: catálogo pode estar vazio
- impacto: personalização preparada sem montar trilha

- decisão: CPF único + validação de dígitos; maioridade >= 18
- motivo: requisitos + risco de unicidade
- impacto: 400/409 conforme caso

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/010-api-cadastro-responsavel-anamnese.md`
- `tasks/slices/004-onboarding-responsavel-anamnese.md`
- `.agents/state/handoffs/TASK-009.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 002 §3 | regras | campos Q1–8 |
| openapi | API | schemas/path |
| ARCHITECTURE/SECURITY | back | módulo |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system / front / mobile | sem UI |

## Resultado por stack

- backend + contrato: done

## Arquivos alterados

- `backend/src/modules/guardians/**`
- migration guardian/children/anamneses
- `contracts/openapi.yaml`
- task/index/slice/handoff

## Validações executadas

- lint/test/typecheck: ok (23 tests)

## Pendências ou bloqueios

- Task 011 wizard web; montagem trilha; pagamento

## Próxima ação sugerida

- Executar Task 011 (`tasks/011-fluxo-cadastro-responsavel-web.md`)

## Próximo contexto recomendado

- task 011 + DS Desktop + openapi guardians/register + front-end docs

## Contexto que não deve ser carregado na próxima etapa

- fonte: mobile docs / DS mobile
- motivo: Task 011 é web
