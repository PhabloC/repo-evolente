# Task 058 - Ajustar dashboard para duas colunas apos as metricas

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

feedback direto do usuario sobre distribuicao dos cards

### Cobertura

- manter os 4 cards superiores de metricas como estao
- reorganizar o restante do dashboard para duas colunas por linha

### Lacunas

- sem novo print de referencia
- decisao: ajustar somente a grade das secoes abaixo das metricas, preservando componentes e conteudo atuais

## Objetivo

Manter a faixa superior de métricas como está e reorganizar os demais cards do dashboard profissional em layout de duas colunas por linha.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-057.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar a distribuicao desejada | sim |
| Front-end | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | manter estrutura e responsividade | sim |
| Implementacao atual | `front-end/src/pages/Main/ShellHome/index.tsx`, `styles.module.css` | ajustar a grade no menor escopo possivel | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao CSS de grade do dashboard e ao menor ajuste estrutural necessario

## Criterios de conclusao

- [x] os 4 cards de metricas superiores permanecem inalterados
- [x] os demais cards passam a respeitar duas colunas por linha em desktop
- [x] responsividade permanece funcional
- [x] lint, build e teste focado aprovados

## Dependencias

- Task 057 - done

## Resultado da execucao

- os 4 cards superiores de metricas foram preservados sem mudanca
- as grades `mainGrid` e `bottomGrid` foram reorganizadas para duas colunas por linha no desktop
- a responsividade existente para tablet e mobile foi mantida

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-057.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/styles.module.css`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao nova
- backend e mobile por estarem fora do escopo

## Handoff

- `.agents/state/handoffs/TASK-058.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/058-dashboard-duas-colunas-apos-metricas.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-058.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
