# Task 057 - Refinar alinhamento do card de prioridades no dashboard

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

feedback direto do usuario sobre desalinhamento visual

### Cobertura

- card "Foco da semana" em `/dashboard`
- alinhamento entre heading, badge, destaque interno, lista e CTAs

### Lacunas

- sem novo print de referencia
- decisao: refinar o layout no menor escopo possivel preservando a linguagem atual

## Objetivo

Corrigir o desalinhamento visual do card de prioridades do dashboard profissional para que os blocos internos tenham hierarquia e respiro mais coerentes.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-056.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | identificar o problema de alinhamento percebido | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | manter estrutura e a11y | sim |
| Implementacao atual | `front-end/src/pages/Main/ShellHome/index.tsx`, `styles.module.css` | ajustar o card no menor escopo possivel | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao card de prioridades e ao teste focado existente se necessario

## Criterios de conclusao

- [x] badge, titulo e bloco destacado deixam de competir visualmente
- [x] lista e CTAs passam a ter alinhamento e largura mais coerentes
- [x] lint, build e teste focado aprovados

## Dependencias

- Task 056 - done

## Resultado da execucao

- o card de prioridades recebeu wrappers específicos para heading, badge e bloco destacado
- o destaque interno passou a usar grade mais estável entre copy e ícone
- os CTAs deixaram de flutuar de forma irregular e passaram a respeitar uma largura mais coerente com o card

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-056.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao nova
- backend e mobile por estarem fora do escopo

## Handoff

- `.agents/state/handoffs/TASK-057.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/057-refinar-alinhamento-card-prioridades-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-057.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
