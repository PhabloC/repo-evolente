# Task 018 - API de trilhas semanais e evolucao

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

- `contracts/openapi.yaml#/paths` trails/progress

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

Nucleo terapeutico.

### O que

Plano semanal do catalogo; progresso; evolucao.

### Comportamento esperado

- CRUD plano
- Progresso
- Historico

### Fora de escopo

- Gamificacao
- Push

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: profissional escreve; responsavel conclui
- Casos de erro: 403; atividade inexistente
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: semana vazia

## Especificacao tecnica

### Deve

- So catalogo master
- Registrar evolucao

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Criar atividade nova

## Entradas

- `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/`

## Dependencias

- Tasks 014 e 016

## Slice vertical

### Identificador do slice

Slice 008 - Trilhas

### Arquivo do slice

- `tasks/slices/008-trilhas-semanais-evolucao.md`

### Objetivo de negócio

Trilhas.

### Entrega verificável do slice

API trilhas/progresso.

### Fora do slice

- UI

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- Conclusao registra
- Isolamento

## Instrucoes de implementacao

- Trilha sugerida da anamnese como ponto de partida

## Validacao esperada

- npm run test
- npm run lint

## Entregaveis esperados

- API trilhas

## Riscos ou ambiguidades

- Formato plano pouco detalhado

## Resultado da execucao

API de trilhas/progresso entregue em `backend/src/modules/trails/`:

- `GET/POST /patients/:patientId/trails` — listar/criar plano semanal (vazio permitido)
- `POST /patients/:patientId/trails/suggest` — ponto de partida via anamnese (categorias pergunta 6)
- `GET/PATCH /trails/:trailId` — detalhe / inativar
- `PUT /trails/:trailId/items` — substituir itens (só catálogo active)
- `GET /patients/:patientId/progress` — histórico de evolução
- `POST /progress/completions` — responsável conclui item e registra evolução

Guards: JWT + roles + `AccessGrantedGuard`. OpenAPI atualizado. Migration `weekly_trails`, `trail_items`, `evolution_records`.

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-017.md`

### Sob demanda

- `requirements/001-escopo-produto.md`, `requirements/002-regras-de-negocio.md`
- `contracts/openapi.yaml`
- `backend/docs/ai/ARCHITECTURE.md`, `SECURITY.md`

## Handoff

- `.agents/state/handoffs/TASK-018.md`

## Arquivos alterados

- `backend/src/modules/trails/**`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/database/migrations/1770000000000-CreateTrailsAndEvolutionTables.ts`
- `backend/src/app.module.ts`
- `contracts/openapi.yaml`
- `tasks/018-api-trilhas-evolucao.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-018.md`

## Validacoes executadas

- `cd backend && npm run lint` — ok
- `cd backend && npm run test` — 11 suites / 40 tests ok

## Aderencia ao design system

nao se aplica (sem UI)

## Pendencias pos-task

- Task 019 — UI montagem trilha web
- Task 020 — execução mobile
- Formato do plano pode ser refinado com feedback humano

## Status final

done
