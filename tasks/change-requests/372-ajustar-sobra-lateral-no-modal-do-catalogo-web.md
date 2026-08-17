# Task 372 - Ajustar sobra lateral no modal do catálogo web

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

- não se aplica; ajuste visual no modal sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 008 - Trilhas semanais e evolucao
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- screenshot enviado pelo usuário no chat

### Fonte primaria visual

- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`

### Lacunas

- sem novo print final; o ajuste deve preservar a composição atual do modal e só eliminar a sobra lateral perceptível

## Objetivo

Remover a sobra lateral no grid do modal `Adicionar do catálogo`, fazendo os cards ocuparem melhor a largura útil disponível.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Modal de catálogo | `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx` | confirmar a estrutura do grid e do conteúdo | sim |
| Estilos do modal | `front-end/src/pages/Main/Plans/styles.module.css` | ajustar a grade e a largura dos cards | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à grade do modal e ao limite de largura dos cards

## Criterios de conclusao

- [x] o grid do modal passa a aproveitar melhor a largura horizontal
- [x] a sobra lateral perceptível é reduzida
- [x] `npx eslint src/pages/Main/Plans/AddCatalogContentModal.tsx`

## Dependencias

- Task 199 - done

## Resultado da execucao

- os cards do modal passaram a expandir dentro da grade em vez de ficar presos a uma largura máxima estreita
- a grade agora usa melhor a área interna do modal, reduzindo a faixa vazia na lateral

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-372.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/372-ajustar-sobra-lateral-no-modal-do-catalogo-web.md`
- `tasks/000-index.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-372.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Plans/AddCatalogContentModal.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done
