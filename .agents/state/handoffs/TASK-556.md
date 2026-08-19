# Handoff - Task 556

- task: `556`
- título: Contrato e requisitos: cadastro só do responsável + filhos autenticados
- slice: `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- status final: done

## Decisões preservadas

- `POST /guardians/register` só `guardian`; payload com `child`/`anamnese` → 400
- `POST /guardians/me/children` cria filho + anamnese + `patientCode` + categorias
- parentesco canônico em `Child.kinship`; `GuardianProfile.kinship` legado/nullable
- `POST /patients` atômico via `CreatePatientRequest`, independente do register
- assinatura por conta; sem teto de filhos

## Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 556, slices 049/050

## Contexto sob demanda carregado

- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml` (guardians/patients/schemas)

## Arquivos alterados

- `contracts/openapi.yaml`
- `requirements/001-escopo-produto.md`
- `requirements/002-regras-de-negocio.md`

## Validações executadas

- critérios de aceite da 556 conferidos no YAML e nos requirements

## Pendências

- Task 557 (API)

## Próxima ação sugerida

- executar Task 557

## Próximo contexto recomendado

- `tasks/change-requests/557-api-cadastro-responsavel-e-filhos.md`
- `backend/src/modules/guardians/**`
- contrato atualizado (`RegisterGuardianRequest`, `CreateGuardianChildRequest`, `CreatePatientRequest`)
- migration TypeORM para `children.kinship` e `guardian_profiles.kinship` nullable

## Contexto que não deve ser carregado

- front-end UI, mobile, jogos, trilhas além do `suggestedTrailCategories`
