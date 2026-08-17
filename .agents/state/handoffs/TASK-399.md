# Handoff — Task 399

- Task: 399 — Foreign keys de integridade referencial no Postgres
- Slice: 033 — Integridade referencial Postgres
- Status final: done

## Decisões preservadas

- FKs no Postgres sem `@ManyToOne` nas entities
- `ON DELETE RESTRICT` como padrão; `CASCADE` só em `password_reset_tokens`; `SET NULL` em FKs opcionais
- Reparo de dados antes das constraints: contents seed com UUID fake → master; evolution_records órfãos de trail_item removidos (7)

## Contexto usado

- entities/migrations backend + Postgres `evolente`

## Arquivos alterados

- `backend/src/database/migrations/1830000000000-AddReferentialForeignKeys.ts`
- task/slice/index/handoff da Task 399

## Validações

- migration run OK; 23 FKs em `information_schema`

## Pendências

- refresh do diagrama ER no cliente
- opcional: relações ORM; limpeza E2E

## Próximo contexto recomendado

- nenhum obrigatório; se UI/ORM follow-up, abrir nova task

## Não carregar

- design-system, front-end, mobile, requirements
