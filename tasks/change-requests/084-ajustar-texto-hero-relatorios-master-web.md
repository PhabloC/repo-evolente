# Task 084 - Ajustar texto do hero em relatórios do master web

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

- nao se aplica; ajuste textual sem alterar dados, estrutura ou integrações

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

- `front-end/src/pages/Main/AdminReports/index.tsx`

### Lacunas

- sem nova referência externa; decisao: trocar apenas título e texto do hero por cópia mais informativa

## Objetivo

Deixar o hero da página de relatórios do master mais informativo e menos explicativo sobre o que a tela não faz.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-083.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/src/pages/Main/AdminReports/index.tsx` | substituir título e texto principal do hero | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | garantir semântica preservada no ajuste textual | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a mudança ao hero da rota `AdminReports`

## Criterios de conclusao

- [x] título do hero comunica melhor a utilidade da central
- [x] texto principal fica mais informativo para o perfil master
- [x] lint do front-end aprovado

## Dependencias

- Task 083 - done

## Resultado da execucao

- o título do hero passou a comunicar a tela como visão executiva do master
- o texto principal deixou de enfatizar o que a rota não faz e passou a explicar os recortes operacionais que ela consolida

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-083.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/AdminReports/index.tsx`

### Contexto evitado

- styles, backend e requisitos do domínio por se tratar apenas de ajuste textual localizado

## Handoff

- `.agents/state/handoffs/TASK-084.md`

## Arquivos alterados

- `front-end/src/pages/Main/AdminReports/index.tsx`
- `tasks/change-requests/084-ajustar-texto-hero-relatorios-master-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-084.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
