# Handoff - Task 018

## Task

- identificador: 018
- título: API de trilhas semanais e evolução
- tipo: back
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 008 - Trilhas
- objetivo de negócio: Trilhas semanais + evolução
- entrega verificável: API trilhas/progresso (UI nas tasks 019/020)
- status do slice: in_progress

## Decisões preservadas

- decisão: uma trilha por `(childId, weekStartDate)`; weekStart normalizado para segunda ISO
- motivo: plano semanal do requisito; formato pouco detalhado na task
- impacto: 409 se criar duplicata da mesma semana

- decisão: itens só com `contentId` active do catálogo master
- motivo: profissional não cria atividade custom
- impacto: `requireActiveById` em create/replace/suggest

- decisão: `POST .../trails/suggest` usa `suggestedTrailCategories` da anamnese
- motivo: personalização automática (pergunta 6) como ponto de partida
- impacto: distribui em weekdays 1–5; semana vazia se catálogo vazio

- decisão: conclusão só por `responsavel` dono da criança → `evolution_records`
- motivo: permissões da task; evolução a cada conclusão
- impacto: `POST /progress/completions`; 409 se já concluído

- decisão: isolamento via vínculo profissional ou guardianUserId
- motivo: 403 cross-tenant
- impacto: leitura profissional/responsável; escrita de plano só profissional

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/018-api-trilhas-evolucao.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-017.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| requirements 001/002 | regras | trilha/catálogo/evolução |
| openapi.yaml | API | paths trails/progress (criados) |
| backend ARCHITECTURE/SECURITY | back | módulo + guards |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| design-system / front / mobile | sem UI nesta task |

## Resultado por stack

- backend: done

## Arquivos alterados

- `backend/src/modules/trails/**`
- migration `1770000000000-CreateTrailsAndEvolutionTables.ts`
- extensão ContentsService/PatientsService
- `contracts/openapi.yaml`
- task/index/slice/handoff

## Validações executadas

- lint/test: ok (40 tests; isolamento, suggest, evolução, conteúdo inválido)

## Pendências ou bloqueios

- UI web Task 019; mobile Task 020
- Formato de plano pode evoluir (dias/itens) conforme feedback humano

## Próxima ação sugerida

- Executar Task 019 (`tasks/019-ui-montagem-trilha-web.md`)

## Próximo contexto recomendado

- task 019 + DS Desktop planejamentos + openapi trails + front-end docs/ai

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend migrations / mobile docs
- motivo: Task 019 é front; consumir contrato trails já publicado
