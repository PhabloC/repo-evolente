# Task 794 - Selecionar várias categorias na atividade da biblioteca

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (fora de escopo; `category` continua existindo)

## Contrato

- `contracts/openapi.yaml` — schemas `Content`, `CreateContentRequest`, `UpdateContentRequest`
- campo novo `categories` (array); `category` permanece como categoria principal (primeiro item)

## Modo de execucao

cross-stack

## Slice vertical

- Slice 006 — `tasks/slices/006-catalogo-conteudos-master.md`

## Referencia de design system

- Stack de referência visual: front-end
- Tipo: UI existente do modal Nova atividade
- Fonte primária: `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- Lacuna: sem prints de multi-select; manter o visual do select atual e mostrar as categorias escolhidas no trigger e nos cards/tabela

## Origem da solicitacao

Pedido humano: no modal de nova atividade, o input de categoria deve permitir selecionar mais de uma; onde a categoria aparece, mostrar as selecionadas.

## Objetivo

Permitir que uma atividade tenha várias categorias terapêuticas, persistidas e exibidas na biblioteca web.

## Dependências

- Task 459 (layout do modal)

## Comportamento esperado

- O select de categoria no modal aceita múltipla escolha (mínimo 1).
- A API aceita `categories` e devolve o array; `category` continua sendo o primeiro item para clientes atuais.
- Cards, tabela, prévia do modal e demais superfícies da biblioteca listam as categorias selecionadas.
- Filtro por aba da biblioteca considera qualquer categoria do conteúdo.

## Fora de escopo

- Mobile (continua lendo `category`)
- Relatórios, dashboard e gráficos
- Alterar unicidade de jogo por `gameType + category`

## Criterios de aceite

- [x] OpenAPI declara `categories` em Content/create/update
- [x] Backend persiste array e filtra por qualquer categoria
- [x] Modal permite selecionar mais de uma categoria
- [x] Biblioteca web mostra as categorias selecionadas
- [x] Testes focados passam

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 006

## Contexto sob demanda

| Gatilho | Fonte | Para quê |
|---|---|---|
| Contrato | `contracts/openapi.yaml` schemas Content | declarar `categories` |
| Persistência | `backend/src/modules/contents/` | coluna, DTOs, filtro |
| UI | `front-end/src/pages/Main/Library/ContentFormModal.tsx` e `index.tsx` | multi-select e exibição |

## Orçamento de contexto

- Fontes obrigatórias: 6
- Estratégia de redução: não carregar mobile, reports nem docs/ai inteiros

## Resultado da execucao

- Coluna `contents.categories` (varchar[]) com backfill a partir de `category`
- Modal usa multi-select; trigger e sidebar listam as escolhidas
- Cards, tabela e prévia da biblioteca usam `getContentCategoriesLabel`

## Contexto utilizado

- Contrato Content, módulo contents, modal e listagem da biblioteca

## Handoff

- `.agents/state/handoffs/TASK-794.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/database/migrations/1940000000000-AddCategoriesToContents.ts`
- `backend/src/modules/contents/content-categories.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/dto/create-content.dto.ts`
- `backend/src/modules/contents/dto/update-content.dto.ts`
- `backend/src/modules/contents/contents.repository.ts`
- `backend/src/modules/contents/contents.typeorm.repository.ts`
- `backend/src/modules/contents/contents.in-memory.repository.ts`
- `backend/src/modules/contents/contents.service.ts`
- `front-end/src/types/content.ts`
- `front-end/src/constants/contentOptions.ts`
- `front-end/src/pages/Main/Library/CategoryMultiSelect.tsx`
- `front-end/src/pages/Main/Library/ContentFormModal.tsx`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/MediaPreviewModal.tsx`
- `front-end/src/pages/Main/Library/ProfessionalLibraryAside.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/utils.ts`

## Validacoes executadas

- Backend: 21 testes do contents/categories
- Front: 10 testes do ContentFormModal
- Migration aplicada no banco
- Página da biblioteca: timeouts de worker neste ambiente

## Pendencias pos-task

- Mobile ainda consome só `category`
- Relatórios/dashboard continuam na categoria principal

## Status final

done
