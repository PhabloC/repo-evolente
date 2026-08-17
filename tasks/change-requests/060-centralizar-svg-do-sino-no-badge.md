# Task 060 - Centralizar SVG do sino no badge de prioridades

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

- nao se aplica; ajuste visual sem alteracao de integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre desalinhamento persistente do sino

### Cobertura

- SVG do sino dentro do destaque de prioridades em `/dashboard`

### Lacunas

- sem novo print de referencia
- decisao: ajustar explicitamente o comportamento do SVG dentro do badge

## Objetivo

Centralizar visualmente o SVG do sino dentro do badge do card de prioridades.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-059.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar que o problema persiste | sim |
| Front-end | `front-end/src/pages/Main/ShellHome/styles.module.css` | corrigir o alinhamento do SVG | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao CSS do SVG no badge

## Criterios de conclusao

- [x] SVG do sino fica centralizado no badge
- [x] lint, build e teste focado aprovados

## Dependencias

- Task 059 - done

## Resultado da execucao

- o SVG do sino passou a usar `display: block` e `margin: auto` dentro do badge
- a correcao ficou restrita ao CSS do destaque de prioridades

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-059.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/src/pages/Main/ShellHome/styles.module.css`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao nova
- backend por estar fora do escopo
- `ShellHome/index.tsx` por nao precisar ajuste estrutural

## Handoff

- `.agents/state/handoffs/TASK-060.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/060-centralizar-svg-do-sino-no-badge.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-060.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
