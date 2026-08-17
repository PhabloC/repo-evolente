# Handoff - Task 008

## Task

- identificador: 008
- título: API de cadastro de profissional
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 003 - Onboarding profissional
- objetivo de negócio: Cadastro profissional
- entrega verificável: API cadastro (UI 009 pendente)
- status do slice: in_progress

## Decisões preservadas

- decisão: `POST /professionals/register` público; role `profissional`; `accessGranted: false`
- motivo: cadastro antes do pagamento sem liberar acesso completo
- impacto: gate de assinatura futuro usa `accessGranted`

- decisão: clínica mínima = legalName + CNPJ (14 dígitos) + phone
- motivo: premissa da task (campos TBD)
- impacto: `practiceType=clinica` exige `clinic`

- decisão: specialties como array livre (multi)
- motivo: não restringir a fono
- impacto: validação ArrayMinSize(1)

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/008-api-cadastro-profissional.md`
- `tasks/slices/003-onboarding-profissional.md`
- `.agents/state/handoffs/TASK-007.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002 | regras | campos |
| openapi | API | schemas/path |
| ARCHITECTURE/SECURITY | back | módulo Nest |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system / front / mobile | sem UI |

## Resultado por stack

- backend + contrato: done
- front/mobile: n/a

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/professionals/**`
- migration professional_profiles
- task/index/slice/handoff

## Validações executadas

- lint/test/typecheck: ok (15 tests)

## Pendências ou bloqueios

- Task 009 UI web; liberação accessGranted no pagamento

## Próxima ação sugerida

- Executar Task 009 (`tasks/009-fluxo-cadastro-profissional-web.md`) se existir no backlog

## Próximo contexto recomendado

- task 009 + DS Desktop (registro) + openapi professionals/register + front-end docs

## Contexto que não deve ser carregado na próxima etapa

- fonte: mobile docs / DS mobile
- motivo: Task 009 é web
