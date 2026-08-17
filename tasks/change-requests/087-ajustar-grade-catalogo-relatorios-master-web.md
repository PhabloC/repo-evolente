# Task 087 - Ajustar grade do catálogo de relatórios do master web

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

- nao se aplica; ajuste visual sem alterar dados ou integrações

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

- `front-end/src/pages/Main/AdminReports/styles.module.css`

### Lacunas

- sem nova referência externa; decisao: manter a composição atual e alterar apenas a grade do catálogo ideal

## Objetivo

Deixar os cards da seção `Catálogo ideal de relatórios` em duas colunas por linha no desktop.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-086.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/AdminReports/styles.module.css` | ajustar a grade da seção `Catálogo ideal de relatórios` | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | preservar responsividade e leitura após a mudança | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a mudança à classe `reportGrid`

## Criterios de conclusao

- [x] cards do catálogo ficam em duas colunas por linha no desktop
- [x] mobile continua com uma coluna
- [x] lint e build do front-end aprovados

## Dependencias

- Task 086 - done

## Resultado da execucao

- a grade da seção `Catálogo ideal de relatórios` passou a usar duas colunas por linha no desktop
- a responsividade foi preservada com queda para uma coluna no mobile

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-086.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/AdminReports/styles.module.css`

### Contexto evitado

- markup da página, backend e contrato por nao serem necessários para o ajuste da grade

## Handoff

- `.agents/state/handoffs/TASK-087.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminReports/styles.module.css`
- `tasks/change-requests/087-ajustar-grade-catalogo-relatorios-master-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-087.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
