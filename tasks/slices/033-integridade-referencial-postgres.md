# Slice 033 - Integridade referencial Postgres

## Status

done

## Objetivo de negocio

Declarar foreign keys no Postgres para as relações já usadas pela aplicação, garantindo integridade no banco e linhas no diagrama ER.

## Entrega verificavel

- Migration TypeORM que cria FKs para todas as colunas `*_id` de domínio
- Migration aplicada no banco `evolente`
- `information_schema` lista as FKs esperadas
- Diagrama ER passa a exibir linhas entre tabelas relacionadas

## Fora de escopo

- Introduzir `@ManyToOne` / relações ORM nas entities (pode ser follow-up)
- Hard delete de usuários ou mudança da política de inativação
- Limpeza de usuários E2E órfãos sem perfil

## Tasks relacionadas

- Task 399
- Task 400

## Dependencias do slice

- Slices 001–011 (schema já existente)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta slice
- entities e migrations em `backend/src/`

## Contexto sob demanda

- Dados atuais do Postgres (validar órfãos antes do `ADD CONSTRAINT`)
- `backend/docs/ai/` para padrões de migration

## Risco de contexto

baixo — alteração localizada em schema, sem UI nem contrato OpenAPI

## Resultado consolidado

- 23 foreign keys aplicadas no Postgres `evolente`
- migration `AddReferentialForeignKeys1830000000000`
- reparo de dados órfãos bloqueantes antes das constraints
- Task 400: `replaceItems` preserva IDs com evolução (compatível com FK RESTRICT)
