# Handoff - Task 015

## Task

- identificador: 015
- título: UI do catalogo de conteudos do master
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catalogo
- objetivo de negócio: UI catálogo / biblioteca web
- entrega verificável: Biblioteca web
- status do slice: done

## Decisões preservadas

- decisão: `/biblioteca` — master cria/edita/upload Base64/inativa; profissional read-only
- motivo: RBAC API 014 + critérios da task
- impacto: botões de mutação só para master

- decisão: inativar/reativar via `status` (sem hard delete)
- motivo: regra do produto
- impacto: filtro de status só no master

- decisão: upload Base64 via `fileToBase64` + `POST /contents/:id/media`
- motivo: handoff 014
- impacto: UI seleciona File e converte antes do envio

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/015-ui-catalogo-master-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-014.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| DS Desktop | UI | tabela/filtros/card |
| openapi contents | API | payloads |
| ARCHITECTURE/ACCESSIBILITY | front | estrutura + a11y |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| mobile / backend docs | single-stack front |

## Resultado por stack

- front-end: done

## Arquivos alterados

- `front-end/src/pages/Main/Library/**`
- types/constants/service/utils content
- routes library
- task/index/slice/handoff

## Validações executadas

- lint/test/build: ok (16 tests)

## Pendências ou bloqueios

- Multipart/S3 futuros; próximo slice pacientes

## Próxima ação sugerida

- Executar Task 016 (`tasks/016-api-pacientes-profissional.md`)

## Próximo contexto recomendado

- task 016 + openapi patients + backend docs

## Contexto que não deve ser carregado na próxima etapa

- fonte: design-system front / front-end docs
- motivo: Task 016 é back
