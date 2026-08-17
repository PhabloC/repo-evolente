# Task 199 - Refinar modal de catálogo dos planejamentos para jogos

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

- O modal deve manter a linguagem visual do desktop com foco em cards, filtros no topo e ações claras, sem rodapé redundante.

## Contexto de negocio

### Por que

O modal de adicionar conteúdo ao planejamento ainda está denso, textual e pouco orientado para seleção visual dos jogos.

### O que

Refinar o modal "Adicionar do catálogo" para mostrar cards clicáveis, check visual de seleção, filtro, paginação, busca mais compacta e remoção do botão Fechar do rodapé.

### Comportamento esperado

- cards visuais substituem a lista textual de opções
- clicar em um card adiciona o conteúdo e mantém um check no canto superior direito
- o rodapé não mostra mais botão Fechar
- existe filtro local no modal
- existe paginação local no modal
- o campo de busca fica menor do que a versão atual

### Fora de escopo

- mudanças de API
- mudança no catálogo da biblioteca
- alteração da execução mobile

## Dependencias

- Task 157

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
- `.agents/state/handoffs/TASK-157.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `design-system/front/Design_System_Evolente_Desktop.md` | modal, cards, filtros e paginação | sim |
| Front-end | `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` e `ACCESSIBILITY.md` | implementação e acessibilidade | sim |
| Planejamentos | `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`, `PatientTrail/index.tsx`, `styles.module.css`, `AddCatalogContentModal.test.tsx` | alteração e validação localizadas | sim |
| Reuso visual de jogos | `front-end/src/pages/Main/Library/libraryGames.ts` | capa/placeholder dos jogos | sim |

## Orçamento de contexto

- Risco médio
- Estrategia de reducao: restringir a mudança ao modal de catálogo do fluxo de planejamentos e ao estado local da seleção do dia

## Criterios de conclusao

- o modal não tem botão Fechar no rodapé
- os conteúdos aparecem como cards clicáveis
- o card selecionado mostra check circular laranja com ícone branco no canto superior direito
- existe filtro e paginação local no modal
- o input de busca fica visualmente menor
- lint e teste isolado do modal passam

## Resultado da execucao

- O modal passou a renderizar cards visuais com capa/placeholder e seleção por clique.
- A seleção mantém o modal aberto e sinaliza o item adicionado com check no canto superior direito.
- Busca, filtro por tipo e paginação local foram adicionados ao catálogo do modal.
- O botão Fechar do rodapé foi removido; o fechamento continua no X do cabeçalho.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 199, slice 026 e `TASK-157`
- contexto sob demanda: `design-system/front/Design_System_Evolente_Desktop.md`; `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`; `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`, `PatientTrail/index.tsx`, `styles.module.css`, `AddCatalogContentModal.test.tsx`; `front-end/src/pages/Main/Library/libraryGames.ts`
- contexto evitado: `contracts/openapi.yaml`, `backend/`, `mobile/`

## Handoff

- `.agents/state/handoffs/TASK-199.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/utils/contentGames.ts`
- `tasks/change-requests/199-refinar-modal-catalogo-planejamentos-jogos.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-199.md`

## Validacoes executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npx vitest run src/pages/Main/Plans/AddCatalogContentModal.test.tsx` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
