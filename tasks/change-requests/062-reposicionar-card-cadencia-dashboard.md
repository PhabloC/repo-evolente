# Task 062 - Reposicionar card de cadência no dashboard

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

feedback direto do usuario sobre distribuicao dos cards no dashboard

### Cobertura

- area principal do `/dashboard`
- relacao entre os cards "Acompanhamento clínico" e "Cadência recente"

### Lacunas

- sem novo print de referencia
- decisao: mover apenas o card de cadência para a grade principal, sem redesenhar os demais blocos

## Objetivo

Posicionar o card "Cadência recente" ao lado do card de acompanhamento clínico para eliminar o vazio visual na grade principal do dashboard.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-061.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | feedback do usuario no chat | confirmar o ajuste de composicao pedido | sim |
| Front-end | `front-end/docs/ai/ACCESSIBILITY.md` | garantir que a reorganizacao preserve a semantica e navegacao | sim |
| Front-end | `front-end/src/pages/Main/ShellHome/index.tsx` | reposicionar o card na grade correta | sim |
| Front-end | `front-end/src/pages/Main/ShellHome/styles.module.css` | validar se a grade atual suporta a nova ordem sem ajuste adicional | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudanca ao `ShellHome` e manter o CSS existente se a grade atual ja suportar a nova composicao

## Criterios de conclusao

- [x] o card "Cadência recente" passa a ocupar a segunda linha da grade principal ao lado de "Acompanhamento clínico"
- [x] a seção inferior continua com composicao coerente após a remoção do card
- [x] teste focado do `ShellHome` permanece aprovado

## Dependencias

- Task 061 - done

## Resultado da execucao

- o card "Cadência recente" foi movido da grade inferior para a grade principal
- a segunda linha da `mainGrid` passou a combinar "Acompanhamento clínico" e "Cadência recente"
- a grade inferior ficou restrita a alertas e relatórios

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-061.md`

### Sob demanda

- feedback do usuario no chat
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integracao nova
- backend e mobile por estarem fora do escopo
- demais modulos do front-end por nao participarem da composicao desta tela

## Handoff

- `.agents/state/handoffs/TASK-062.md`

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `tasks/change-requests/062-reposicionar-card-cadencia-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-062.md`

## Validacoes executadas

- `cd front-end && npm run test -- ShellHome` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
