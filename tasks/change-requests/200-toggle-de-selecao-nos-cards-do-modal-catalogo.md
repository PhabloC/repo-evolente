# Task 200 - Toggle de seleção nos cards do modal de catálogo

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

nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- O card selecionado no modal deve continuar usando o check visual existente, mas agora com comportamento de toggle por clique.

## Contexto de negocio

### Por que

Depois do refino visual do modal, o card selecionado ainda não permite desfazer a escolha com o mesmo gesto direto de clique.

### O que

Permitir que clicar novamente em um card já marcado remova o conteúdo daquele dia e desmarque o check.

### Comportamento esperado

- primeiro clique marca e adiciona o conteúdo
- segundo clique no mesmo card desmarca e remove o conteúdo do dia atual
- o estado visual do check acompanha a seleção

### Fora de escopo

- mudanças de API
- alteração da paginação, filtro ou layout do modal

## Dependencias

- Task 199

## Slice vertical

### Identificador do slice

Slice 026 - Jogos terapeuticos e alfabeto falado

### Arquivo do slice

- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-199.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Front-end | `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` e `ACCESSIBILITY.md` | implementação e acessibilidade | sim |
| Planejamentos | `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`, `PatientTrail/index.tsx`, `AddCatalogContentModal.test.tsx` | alteração e validação localizadas | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: restringir a mudança ao toggle do estado selecionado no modal de catálogo

## Criterios de conclusao

- card selecionado desmarca ao segundo clique
- o conteúdo é removido do dia atual ao desmarcar
- o check visual acompanha o toggle
- lint e teste isolado do modal passam

## Resultado da execucao

- O modal passou a disparar seleção e desmarcação pelo mesmo clique no card.
- O `PatientTrail` agora remove o conteúdo correspondente do dia atual quando o card selecionado é clicado novamente.
- O teste do modal foi atualizado para cobrir o toggle.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 200, slice 026 e `TASK-199`
- contexto sob demanda: `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`; `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`, `PatientTrail/index.tsx`, `AddCatalogContentModal.test.tsx`
- contexto evitado: `contracts/openapi.yaml`, `backend/`, `mobile/`

## Handoff

- `.agents/state/handoffs/TASK-200.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.test.tsx`
- `tasks/change-requests/200-toggle-de-selecao-nos-cards-do-modal-catalogo.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-200.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npx vitest run src/pages/Main/Plans/AddCatalogContentModal.test.tsx` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
