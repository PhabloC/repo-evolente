# Task 064 - Reduzir altura do CTA de cadência no dashboard

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

feedback direto do usuario sobre proporcao do CTA no card de cadencia

### Cobertura

- card "Cadência recente" em `/dashboard`
- CTA `Abrir pacientes`

### Lacunas

- sem novo print de referencia
- decisao: manter a largura total e reduzir apenas altura/padding do CTA dedicado

## Objetivo

Reduzir a altura do botão `Abrir pacientes` no card de cadência para ficar proporcional aos demais CTAs.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-063.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar o problema de proporcao | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | preservar area clicavel minima mesmo com altura menor | sim |
| Front-end | `front-end/src/pages/Main/ShellHome/styles.module.css` | ajustar a altura do CTA dedicado | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas a classe dedicada do CTA de cadencia

## Criterios de conclusao

- [x] o CTA `Abrir pacientes` fica visualmente menos alto
- [x] a largura total do CTA e a responsividade anterior são preservadas
- [x] teste focado do `ShellHome` permanece aprovado

## Dependencias

- Task 063 - done

## Resultado da execucao

- a classe dedicada do CTA de cadencia passou a sobrescrever `min-height` e `padding`
- o botao manteve largura total, mas ficou mais proporcional ao card

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-063.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/styles.module.css`

### Contexto evitado

- `front-end/src/pages/Main/ShellHome/index.tsx` por nao exigir novo ajuste estrutural
- `contracts/openapi.yaml` por nao haver integracao nova
- backend e mobile por estarem fora do escopo

## Handoff

- `.agents/state/handoffs/TASK-064.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/064-reduzir-altura-cta-cadencia-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-064.md`

## Validacoes executadas

- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
