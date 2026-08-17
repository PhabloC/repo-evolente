# Handoff - Task 016

## Task

- identificador: 016
- título: API de pacientes, vínculo e inativação
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 007 - Pacientes
- objetivo de negócio: Gestão pacientes
- entrega verificável: API isolada (UI na Task 017)
- status do slice: in_progress (API done; UI pendente)

## Decisões preservadas

- decisão: tabela `professional_patient_links` com `child_id` UNIQUE (mono-vínculo)
- motivo: premissa da task/slice até confirmação humana de multi-vínculo
- impacto: segundo vínculo → 409; inativar não libera o child para outro profissional

- decisão: `:id` nos paths = `child.id` (não o id do link)
- motivo: alinhamento com domínio “paciente = criança”
- impacto: OpenAPI `PatientId` documenta child.id

- decisão: POST `/patients` reutiliza `GuardiansService.register` + cria link
- motivo: mesma regra de cadastro responsável/anamnese
- impacto: cria login do responsável; accessGranted do responsável permanece false até assinatura

- decisão: guards `JwtAuthGuard` + `RolesGuard(profissional)` + `AccessGrantedGuard`
- motivo: profissional com assinatura
- impacto: master/responsável não usam esta API nesta task

- decisão: inativar = status do link; sem DELETE
- motivo: regra de produto
- impacto: PATCH `/patients/:id/status`

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/016-api-pacientes-profissional.md`
- `tasks/slices/007-gestao-pacientes-profissional.md`
- handoff Task 015 (próxima ação)

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002 | regras | isolamento/vínculo/inativar |
| openapi.yaml | API | paths/schemas patients |
| backend SECURITY + padrões contents/guardians | back | módulo + guards |
| NFR 003 | LGPD/storage | sem blob; inativar |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system / front-end | sem UI nesta task |
| mobile | não envolvido |

## Resultado por stack

- backend: done

## Arquivos alterados

- `backend/src/modules/patients/**`
- `backend/src/modules/guardians/*` (lookups/update child)
- `backend/src/database/migrations/1760000000000-CreateProfessionalPatientLinksTable.ts`
- `backend/src/app.module.ts`
- `contracts/openapi.yaml`
- task/index/slice/handoff

## Validações executadas

- `npm run lint` ok
- `npm run test` ok (36 tests, incl. isolamento/mono-vínculo/inativação)

## Pendências ou bloqueios

- UI web Task 017
- dúvida humana: multi-vínculo (hoje mono)

## Próxima ação sugerida

- Executar Task 017 (`tasks/017-dashboard-profissional-pacientes-web.md`)

## Próximo contexto recomendado

- task 017 + DS Desktop pacientes + openapi patients + front-end docs/ai

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend docs profundos / migrations
- motivo: Task 017 é front; consumir contrato patients já publicado
