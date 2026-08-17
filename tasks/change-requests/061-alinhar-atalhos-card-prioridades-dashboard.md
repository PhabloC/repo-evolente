# Task 061 - Alinhar atalhos do card de prioridades no dashboard

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

feedback direto do usuario sobre composicao dos atalhos do card de prioridades

### Cobertura

- card "Foco da semana" em `/dashboard`
- links "Ver pacientes prioritários" e "Abrir planejamentos"

### Lacunas

- sem novo print de referencia
- decisao: seguir o pedido objetivo do usuario e ajustar apenas disposicao e largura dos dois atalhos

## Objetivo

Colocar os atalhos principais do card de prioridades lado a lado, com a mesma largura, preservando responsividade.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-060.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar o ajuste visual pedido | sim |
| Front-end | `front-end/AGENTS.md` | validar governanca local da stack | sim |
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | confirmar que os links continuam acessiveis no novo layout | sim |
| Front-end | `front-end/src/pages/Main/ShellHome/styles.module.css` | ajustar a composicao dos atalhos | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao CSS do card de prioridades e evitar alterar estrutura JSX sem necessidade

## Criterios de conclusao

- [x] os links "Ver pacientes prioritários" e "Abrir planejamentos" ficam lado a lado no desktop
- [x] ambos passam a ocupar larguras equivalentes
- [x] o layout continua empilhando de forma segura no mobile
- [x] teste focado do `ShellHome` permanece aprovado

## Dependencias

- Task 060 - done

## Resultado da execucao

- o container `focusActions` passou a usar duas colunas equivalentes em telas maiores
- os dois links do card de prioridades passaram a ocupar toda a largura de suas respectivas colunas
- o empilhamento em uma coluna no breakpoint mobile foi preservado

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-060.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/styles.module.css`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao nova
- `front-end/src/pages/Main/ShellHome/index.tsx` por nao precisar ajuste estrutural
- backend e mobile por estarem fora do escopo

## Handoff

- `.agents/state/handoffs/TASK-061.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/061-alinhar-atalhos-card-prioridades-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-061.md`

## Validacoes executadas

- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
