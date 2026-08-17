# Task 177 - Remover scroll-behavior smooth global no front-end

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

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| CSS global | `front-end/src/styles/global.css` | remoção do smooth scroll | sim |

## Orçamento de contexto

- Risco baixo

## Criterios de conclusao

- `scroll-behavior: smooth` removido de `html` em `global.css`

## Dependencias

- nenhuma

## Resultado da execucao

- Removido `scroll-behavior: smooth` do seletor `html` em `front-end/src/styles/global.css`

## Arquivos alterados

- `front-end/src/styles/global.css`
- `tasks/change-requests/177-remover-scroll-behavior-smooth-global.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-177.md`

## Validacoes executadas

- grep confirma ausência de `scroll-behavior` no front-end

## Pendencias pos-task

- nenhuma

## Status final

done
