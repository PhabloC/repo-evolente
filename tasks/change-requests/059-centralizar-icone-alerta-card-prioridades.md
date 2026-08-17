# Task 059 - Centralizar icone de alerta no card de prioridades

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

feedback direto do usuario sobre alinhamento do icone

### Cobertura

- bloco destacado do card "Foco da semana" em `/dashboard`

### Lacunas

- sem novo print de referencia
- decisao: ajustar apenas o container do icone no menor escopo possivel

## Objetivo

Centralizar visualmente o ícone de sino dentro do bloco destacado do card de prioridades no dashboard profissional.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-058.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar o desalinhamento do icone | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md`, `CODE_STYLE.md` | manter semantica e consistencia | sim |
| Implementacao atual | `front-end/src/pages/Main/ShellHome/styles.module.css` | ajustar o alinhamento no menor escopo possivel | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao CSS do container do icone

## Criterios de conclusao

- [x] icone de sino fica centralizado no bloco visual
- [x] lint, build e teste focado aprovados

## Dependencias

- Task 058 - done

## Resultado da execucao

- o container do sino recebeu dimensoes minimas e alinhamento explicito no eixo do grid
- a correcao ficou restrita ao CSS do destaque de prioridades

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-058.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ACCESSIBILITY.md`, `CODE_STYLE.md`
- `front-end/src/pages/Main/ShellHome/styles.module.css`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao nova
- backend por estar fora do escopo
- `ShellHome/index.tsx` por nao precisar ajuste estrutural

## Handoff

- `.agents/state/handoffs/TASK-059.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/059-centralizar-icone-alerta-card-prioridades.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-059.md`

## Validacoes executadas

- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok
- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
