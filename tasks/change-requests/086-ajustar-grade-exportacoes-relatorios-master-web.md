# Task 086 - Ajustar grade de exportações em relatórios do master web

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

- nao se aplica; ajuste visual sem alterar endpoints ou integrações

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste incremental solicitado no chat

### Fonte primaria visual

- `front-end/src/pages/Main/AdminReports/{index.tsx,styles.module.css}`

### Lacunas

- sem print novo; decisao: remover o card lateral da seção e reorganizar as exportações em duas colunas por linha

## Objetivo

Simplificar a seção de exportações da central de relatórios do master, removendo o card lateral e exibindo os cards de exportação em grade de duas colunas.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-085.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/AdminReports/index.tsx` | remover o card `Estado desta fase` da composição | sim |
| Estilos locais | `front-end/src/pages/Main/AdminReports/styles.module.css` | ajustar a grade de exportações para duas colunas | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | garantir semântica e responsividade após a mudança | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à seção `Exportações e governança` da rota `AdminReports`

## Criterios de conclusao

- [x] card `Estado desta fase` removido da página
- [x] exportações ficam em duas colunas por linha no desktop
- [x] responsividade e lint do front-end aprovados

## Dependencias

- Task 085 - done

## Resultado da execucao

- a seção de exportações foi simplificada com remoção do card lateral `Estado desta fase`
- os cards de exportação passaram a ocupar duas colunas por linha no desktop e uma coluna no mobile

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-085.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/AdminReports/index.tsx`
- `front-end/src/pages/Main/AdminReports/styles.module.css`

### Contexto evitado

- backend, contrato OpenAPI e services de exportação por nao participarem deste ajuste de layout

## Handoff

- `.agents/state/handoffs/TASK-086.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminReports/index.tsx`
- `front-end/src/pages/Main/AdminReports/styles.module.css`
- `tasks/change-requests/086-ajustar-grade-exportacoes-relatorios-master-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-086.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
