# Task 438 - Paginação dos jogos e cache da biblioteca web

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

- nao se aplica (paginação e cache locais na página; sem mudança de API)

## Modo de execucao

single-stack

## Slice vertical

- Slice 006 - Catálogo de conteúdos master
- `tasks/slices/006-catalogo-conteudos-master.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- refinamento incremental solicitado via chat

### Fonte primaria visual

- padrão de paginação já usado na tabela editorial da biblioteca (`paginationBar` / `paginationNav`)

### Regra de aderencia visual

- reutilizar o mesmo padrão compacto de paginação da tabela; não redesenhar a prateleira de jogos

## Objetivo

Aliviar o peso da página `/biblioteca`: paginar o grid de jogos (hoje renderiza todos) e cachear a listagem de conteúdos na sessão de navegação para evitar refetch e reparse do catálogo completo a cada visita.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página biblioteca | `front-end/src/pages/Main/Library/index.tsx` | paginar jogos e integrar cache | sim |
| Estilos/paginação | `front-end/src/pages/Main/Library/styles.module.css` | reusar barra de paginação | sim |
| Cache util | `front-end/src/pages/Main/Library/` (novo util) | cache em memória com TTL e invalidação | sim |
| Testes | `front-end/src/pages/Main/Library/index.test.tsx` | cobrir paginação de jogos e hit de cache | sim |
| Acessibilidade UI | `front-end/docs/ai/ACCESSIBILITY.md` | nav/aria da paginação de jogos | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar ao front da biblioteca; não abrir contrato OpenAPI nem backend
- Não carregar mobile, next-js nem design-system completo

## Criterios de conclusao

- [x] grid de jogos renderiza apenas uma página (tamanho fixo) com controles de paginação no mesmo padrão da tabela
- [x] troca de aba/filtro reseta a página dos jogos
- [x] listagem da biblioteca usa cache em memória com TTL; revisitação com cache fresco não chama `listContents` de novo
- [x] mutações (criar/editar/status/excluir) invalidam o cache e forçam reload
- [x] testes cobrem paginação de jogos e comportamento de cache
- [x] acessibilidade: `nav` com `aria-label`, resumo `aria-live`, botões com labels

## Dependencias

- Task 340 (paginação da tabela editorial)
- Task 405 (filtros por categoria nos jogos)

## Fora de escopo

- paginação server-side em `GET /contents`
- alteração do contrato OpenAPI
- cache em `localStorage`/`sessionStorage`
- mudanças em mobile ou planejamentos

## Resultado da execucao

- Grid de jogos paginado (6 por página) com `LibraryPaginationBar`
- Cache em memória (`libraryContentsCache`) com TTL de 5 min; hit evita refetch ao remontar a página
- Mutações invalidam o cache e forçam reload
- Tabela editorial passou a usar o mesmo componente de paginação

## Contexto utilizado

- Task 438, Slice 006, `ACCESSIBILITY.md`, arquivos da Library

## Handoff

- `.agents/state/handoffs/TASK-438.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/LibraryPaginationBar.tsx`
- `front-end/src/pages/Main/Library/libraryContentsCache.ts`
- `front-end/src/pages/Main/Library/libraryContentsCache.test.ts`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/438-paginacao-e-cache-biblioteca-web.md`
- `tasks/000-index.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-438.md`

## Validacoes executadas

- `npm run test -- --run src/pages/Main/Library/index.test.tsx src/pages/Main/Library/libraryContentsCache.test.ts` — 19 passed

## Acessibilidade aplicada

- `nav` com `aria-label` distinto para jogos e tabela
- resumo com `aria-live="polite"`
- botões Anterior/Próxima com `aria-label`
- página ativa com `aria-current="page"`

## Pendencias pos-task

- nenhuma

## Status final

done
