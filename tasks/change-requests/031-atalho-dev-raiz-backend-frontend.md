# Change Request 031 - Atalho dev na raiz para backend + frontend

## Status

done

## Tipo

shared

## Stacks envolvidos

- raiz
- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

cross-stack

## Slice vertical

### Identificador do slice

Slice 001 - Fundacao e contrato base

### Arquivo do slice

- `tasks/slices/001-fundacao-contrato-base.md`

## Contexto de negocio

### Por que

Facilitar a subida local do ambiente web + API com um unico comando.

### O que

Adicionar um script na raiz para iniciar backend e frontend em paralelo.

### Comportamento esperado

- `npm run dev` na raiz sobe `backend` e `front-end` juntos

### Fora de escopo

- mobile
- orquestracao de banco
- alteracoes em scripts internos das stacks

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `tasks/000-index.md`
- este arquivo

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| scripts existentes | `package.json`, `backend/package.json`, `front-end/package.json` | definir atalho raiz | sim |

## Orçamento de contexto

- Risco baixo

## Resultado da execucao

Script `dev` adicionado na raiz usando `concurrently` para executar `npm --prefix backend run start:dev` e `npm --prefix front-end run dev`.

## Arquivos alterados

- `package.json`
- `package-lock.json`
- `tasks/000-index.md`
- `tasks/change-requests/031-atalho-dev-raiz-backend-frontend.md`
- `.agents/state/handoffs/TASK-031.md`

## Validacoes executadas

- `npm install` na raiz — ok
- tentativa controlada de `npm run dev` — script inicia, mas o encerramento forçado por timeout gerou `EPIPE` no `concurrently`

## Status final

done
