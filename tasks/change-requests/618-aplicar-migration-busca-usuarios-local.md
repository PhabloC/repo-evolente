# Task 618 - Aplicar migration da busca de usuários local

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

- `GET /users?search={termo}` já documentado na Task 615.

## Modo de execução

single-stack

## Slice vertical

- Slice 017 — `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Aplicar no banco local a migration que instala `unaccent`, dependência da consulta de usuários por nome/e-mail.

## Dependências

- Task 615 — done

## Contexto mínimo

- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-615.md`
- `backend/src/database/migrations/1900000000000-EnableUnaccentForUserSearch.ts`
- `backend/package.json`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Busca retorna vazia para nome existente | banco local | executar a migration pendente que fornece `unaccent`. |

## Orçamento de contexto

- baixo
- estratégia: aplicar apenas as migrations pendentes pelo script oficial do backend, sem alterar registros de usuários.

## Critérios de aceite

- [x] Migration `EnableUnaccentForUserSearch` aplicada no banco local.
- [x] Busca do endpoint não falha pela ausência da extensão PostgreSQL.

## Resultado da execução

- A migration pendente foi executada e criou a extensão PostgreSQL `unaccent` no banco local.

## Contexto utilizado

- Task 618, Slice 017, handoff Task 615, migration `EnableUnaccentForUserSearch` e script `migration:run`.

## Arquivos alterados

- Nenhum arquivo de aplicação previsto; alteração controlada no schema local.

## Validações executadas

- `npm run migration:run` executou `EnableUnaccentForUserSearch1900000000000` com sucesso e confirmou `COMMIT`.

## Pendências pós-task

- Reiniciar o backend somente se ele não estiver em modo watch; fazer smoke da pesquisa com um nome existente.

## Handoff

- Criado em `.agents/state/handoffs/TASK-618.md`.

## Status final

done
