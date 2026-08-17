# Task 405 - Filtrar jogos da biblioteca pelas abas de categoria

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

- sem alteração; filtro client-side na listagem já carregada

## Modo de execução

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web (follow-up das Tasks 401–403)
- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Fazer as abas de categoria da biblioteca filtrarem também o catálogo jogável (a Task 401 filtrava só a tabela editorial).

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-401.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Bug de filtro | `front-end/src/pages/Main/Library/index.tsx` | aplicar filtro em `gameItems` |
| Regressão | `front-end/src/pages/Main/Library/index.test.tsx` | cobrir clique na aba |

## Orçamento de contexto

- baixo

## Critérios de conclusão

- [x] `gameItems` respeita a aba de categoria ativa
- [x] aba "Todas" continua exibindo todos os jogos
- [x] teste de regressão cobrindo o filtro
- [x] checks locais do front relevantes passam

## Resultado da execucao

- `gameItems` passou a usar o mesmo critério de categoria da tabela editorial.
- Aba Cognição inclui também `matematica` (mesmo rótulo visual).
- Troca de aba reseta a paginação da tabela.
- Teste cobre filtro Cognição/Vocabulário no catálogo jogável.

## Contexto utilizado

- Library `index.tsx`/`index.test.tsx`, handoff Task 401, Slice 017

## Handoff

- `.agents/state/handoffs/TASK-405.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/405-filtrar-jogos-biblioteca-pelas-abas-categoria.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-405.md`

## Validacoes executadas

- `npx vitest run src/pages/Main/Library/index.test.tsx -t "filters featured games"` — OK

## Pendencias pos-task

- nenhuma

## Status final

done
