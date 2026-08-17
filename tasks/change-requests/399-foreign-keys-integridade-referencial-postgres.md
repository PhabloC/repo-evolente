# Task 399 - Foreign keys de integridade referencial no Postgres

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

- sem alteração de OpenAPI; mudança apenas de schema Postgres

## Modo de execução

single-stack

## Slice vertical

- Slice 033 - Integridade referencial Postgres
- `tasks/slices/033-integridade-referencial-postgres.md`

## Objetivo

Adicionar foreign keys no Postgres para as colunas de relação já usadas pela aplicação (`user_id`, `child_id`, `trail_id`, etc.), para reforçar integridade e permitir linhas no diagrama ER.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/033-integridade-referencial-postgres.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Colunas e tabelas | `backend/src/modules/**/entities/*.ts` | mapear FKs |
| Padrão de migration | `backend/src/database/migrations/` | criar migration |
| Validação | Postgres `evolente` | órfãos + `migration:run` + listar FKs |
| Padrões locais | `backend/docs/ai/` | orientar implementação e QA |

## Orçamento de contexto

- baixo
- uma migration + validação SQL; sem UI

## Critérios de conclusão

- [x] migration cria FKs para todas as relações lógicas mapeadas
- [x] `down` remove as FKs na ordem inversa
- [x] dados atuais passam na constraint (sem órfãos bloqueantes)
- [x] migration aplicada no banco remoto configurado
- [x] contagem de FKs > 0 em `information_schema`

## Politica de ON DELETE

- `RESTRICT` na maioria (política do produto: inativar, não excluir), inclusive `trail_items.trail_id` (evita conflito com `evolution_records`)
- `CASCADE` em `password_reset_tokens.user_id` (tokens efêmeros)
- `SET NULL` em colunas opcionais: `admin_audit_logs.actor_user_id`, `evolution_reports.shared_by_user_id`

## Resultado da execucao

- Criada migration `1830000000000-AddReferentialForeignKeys` com 23 FKs.
- Antes das constraints: reparo de `contents.created_by_user_id` órfão (UUID placeholder) reatribuído ao master mais antigo; remoção de 7 `evolution_records` cujo `trail_item_id` apontava para itens já recriados/removidos (bloqueavam unique/FK).
- Migration aplicada com sucesso no Postgres `evolente`.
- Validação: `FK_COUNT = 23`; diagrama ER passa a exibir linhas.

## Contexto utilizado

- contexto mínimo: raiz, task, Slice 033
- contexto sob demanda: entities, migrations existentes, consulta SQL no Postgres
- contexto evitado: requirements, design systems, front-end, mobile, OpenAPI

## Handoff

- `.agents/state/handoffs/TASK-399.md`

## Arquivos alterados

- `backend/src/database/migrations/1830000000000-AddReferentialForeignKeys.ts`
- `tasks/slices/033-integridade-referencial-postgres.md`
- `tasks/change-requests/399-foreign-keys-integridade-referencial-postgres.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-399.md`

## Validacoes executadas

- `npm run migration:run` — sucesso
- consulta `information_schema` — 23 foreign keys
- confirmação: 0 contents com UUID placeholder; evolution_records órfãos removidos

## Pendencias pos-task

- Atualizar o visualizador ER (refresh) para ver as linhas
- Follow-up opcional: `@ManyToOne` nas entities TypeORM (não necessário para o ERD)
- Follow-up opcional: limpar usuários E2E sem perfil

## Status final

done
