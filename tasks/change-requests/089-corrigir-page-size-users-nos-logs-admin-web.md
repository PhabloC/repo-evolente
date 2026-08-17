# Task 089 - Corrigir pageSize de usuários no fluxo de logs do admin web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica; correção de consumo do endpoint existente conforme limite já imposto pelo backend

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

correção funcional sem impacto visual

### Fonte primaria visual

- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`

### Lacunas

- sem referência visual; decisao: alinhar o consumo do endpoint de usuários ao limite aceito pela API

## Objetivo

Corrigir o erro `400 Bad Request` ao abrir a página de logs, ajustando o `pageSize` usado para carregar o diretório de usuários auxiliar.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-088.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Erro 400 nos logs | `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx` | ajustar a busca auxiliar de usuários para respeitar o limite aceito pela API | sim |
| Contrato observado no código | `backend/src/modules/users/dto/list-users-query.dto.ts` | confirmar que o backend aceita no máximo 100 itens por página | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a mudança ao parâmetro `pageSize` usado no carregamento auxiliar dos logs

## Criterios de conclusao

- [x] página de logs deixa de solicitar `pageSize=200` em `/users`
- [x] consumo passa a respeitar o limite aceito pela API
- [x] lint e build do front-end aprovados

## Dependencias

- Task 088 - done

## Resultado da execucao

- o carregamento auxiliar de usuários no fluxo de logs passou a usar `pageSize=100`, respeitando o limite máximo aceito pela API
- a página de logs deixa de disparar `400 Bad Request` por excesso no `pageSize`

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-088.md`

### Sob demanda

- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `backend/src/modules/users/dto/list-users-query.dto.ts`

### Contexto evitado

- backend funcional, contrato OpenAPI e componentes visuais por nao serem necessários para a correção do parâmetro

## Handoff

- `.agents/state/handoffs/TASK-089.md`

## Arquivos alterados

- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `tasks/change-requests/089-corrigir-page-size-users-nos-logs-admin-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-089.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
