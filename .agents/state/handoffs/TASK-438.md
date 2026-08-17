# Handoff - Task 438

## Task

- identificador: 438
- título: Paginação dos jogos e cache da biblioteca web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 006
- objetivo de negócio: catálogo de conteúdos master
- entrega verificável: biblioteca web mais leve com jogos paginados e listagem cacheada

## Decisões preservadas

- decisão: paginação local do grid de jogos (6 itens), sem paginação server-side
- motivo: aliviar DOM/render sem alterar contrato `GET /contents` usado por outras stacks
- impacto: API e mobile/planejamentos intactos

- decisão: cache em memória com TTL 5 min + invalidação em mutações
- motivo: evitar refetch/reparse do catálogo ao navegar e voltar para `/biblioteca`
- impacto: dados frescos após criar/editar/status/excluir

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/438-paginacao-e-cache-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/*` | UI biblioteca | paginação + cache |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI | aria da paginação |

### Contexto evitado

- `contracts/openapi.yaml`
- backend
- mobile
- design-system completo

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/LibraryPaginationBar.tsx`
- `front-end/src/pages/Main/Library/libraryContentsCache.ts`
- `front-end/src/pages/Main/Library/libraryContentsCache.test.ts`
- `front-end/src/pages/Main/Library/index.test.tsx`
- tasks/index/slice/handoff

## Validacoes executadas

- vitest Library + cache — 19 passed

## Pendencias

- nenhuma

## Proxima acao sugerida

- se o payload de `GET /contents` ainda pesar na rede, considerar listagem slim / paginação no contrato em task separada

## Proximo contexto recomendado

- nenhum obrigatório

## Contexto que nao deve ser carregado

- mobile, openapi completo, design-system
