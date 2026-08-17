# Task 063 - Equalizar largura do CTA de cadência no dashboard

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

feedback direto do usuario sobre consistencia visual dos botoes do dashboard

### Cobertura

- card "Cadência recente" em `/dashboard`
- CTA `Abrir pacientes`

### Lacunas

- sem novo print de referencia
- decisao: equalizar apenas a largura do CTA do card de cadencia, sem alterar os demais links accentuados fora desse contexto

## Objetivo

Deixar o botão `Abrir pacientes` com o mesmo tamanho visual dos outros CTAs principais do dashboard.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-062.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar o ajuste fino pedido | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | preservar legibilidade e area clicavel do CTA | sim |
| Front-end | `front-end/src/pages/Main/ShellHome/index.tsx` | aplicar classe dedicada ao CTA correto | sim |
| Front-end | `front-end/src/pages/Main/ShellHome/styles.module.css` | equalizar a largura sem impactar outros links | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca a uma classe dedicada no CTA de cadencia

## Criterios de conclusao

- [x] o CTA `Abrir pacientes` ocupa largura equivalente aos outros botoes principais
- [x] o CTA do card do responsável nao muda de comportamento
- [x] teste focado do `ShellHome` permanece aprovado

## Dependencias

- Task 062 - done

## Resultado da execucao

- o CTA `Abrir pacientes` passou a usar uma classe dedicada de largura total
- o ajuste ficou restrito ao card de cadencia dentro do dashboard profissional

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-062.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao nova
- backend e mobile por estarem fora do escopo
- demais paginas do front-end por nao participarem do ajuste

## Handoff

- `.agents/state/handoffs/TASK-063.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/063-equalizar-largura-cta-cadencia-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-063.md`

## Validacoes executadas

- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
