# Task 049 - Gitignore local nas stacks backend, front-end e mobile

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica

## Modo de execucao

cross-stack

## Slice vertical

- Slice 001 - Fundacao e contrato base
- `tasks/slices/001-fundacao-contrato-base.md`

## Contexto de negocio

### Por que

Permitir que cada stack tenha regras locais de ignorar artefatos gerados e arquivos sensiveis, mesmo quando usada isoladamente.

### O que

Criar o `.gitignore` faltante no `backend/` e garantir que `front-end/` e `mobile/` tenham regras locais adequadas, incluindo arquivos de ambiente quando aplicavel.

### Comportamento esperado

- `backend/.gitignore` passa a ignorar `node_modules`, `dist`, `coverage`, `.data` e variaveis de ambiente locais
- `front-end/.gitignore` ignora variaveis de ambiente locais e preserva `.env.example`
- `mobile/.gitignore` ignora variaveis de ambiente locais e preserva `.env.example`

### Fora de escopo

- alteracoes em codigo de produto
- mudancas de build, lint ou scripts

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/001-fundacao-contrato-base.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| padrao existente de ignore | `.gitignore`, `front-end/.gitignore`, `mobile/.gitignore` | definir regras locais coerentes | sim |
| stack backend | `backend/package.json` | confirmar artefatos gerados pelo backend | sim |
| continuidade de slice | `.agents/state/handoffs/TASK-031.md` | reaproveitar contexto de fundacao compartilhada similar | nao |

## Orçamento de contexto

- baixo; restrito aos arquivos de configuracao e rastreabilidade do scaffold

## Criterios de conclusao

- [x] `backend/.gitignore` criado
- [x] `front-end/.gitignore` confirmado
- [x] `mobile/.gitignore` confirmado
- [x] task, indice, slice e handoff reconciliados

## Resultado da execucao

- criado `backend/.gitignore` com ignores para dependencias, build, cobertura, pasta `.data` e arquivos de ambiente
- confirmado que o pedido de `frontend` corresponde ao diretório real `front-end/`
- ajustado `front-end/.gitignore` para ignorar `.env` e `.env.*`, preservando `.env.example`
- ajustado `mobile/.gitignore` para ignorar `.env` e `.env.*`, preservando `.env.example`

## Contexto utilizado

- fontes globais de orquestracao
- `tasks/slices/001-fundacao-contrato-base.md`
- `.gitignore` da raiz
- `front-end/.gitignore`
- `mobile/.gitignore`
- `backend/package.json`
- handoff `TASK-031` como referencia de change request infra no mesmo slice

## Handoff

- `.agents/state/handoffs/TASK-049.md`

## Arquivos alterados

- `backend/.gitignore`
- `front-end/.gitignore`
- `mobile/.gitignore`
- `tasks/change-requests/049-gitignore-stacks-backend-front-end-mobile.md`
- `tasks/slices/001-fundacao-contrato-base.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-049.md`

## Validacoes executadas

- verificacao estrutural de existencia e conteudo dos arquivos `.gitignore` em `backend/`, `front-end/` e `mobile/`

## Pendencias pos-task

- nenhuma

## Status final

done
