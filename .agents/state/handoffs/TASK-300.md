# Handoff - Task 300

## Task

- identificador: 300
- titulo: Arraste com mãozinha na grade semanal do planejamento web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: tornar o scroll horizontal da grade semanal mais evidente e operacional
- entrega verificavel: a grade semanal mostra cursor de mão e permite arraste horizontal com o mouse

## Decisoes preservadas

- a mudança evoluiu o contêiner de scroll da Task 299 em vez de criar nova abstração
- o arraste horizontal é iniciado apenas em áreas não interativas, preservando cliques em botões e controles da grade
- o estado de arraste fica explícito no DOM via `data-dragging` e no cursor `grab/grabbing`

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/300-arraste-com-maozinha-na-grade-semanal-do-planejamento-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-299.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | validar interação por mouse e semântica mínima |
| `front-end/docs/ai/COMPONENT_REUSE.md` | escopo local | limitar a mudança ao contêiner da grade |
| `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | gesto de arraste | implementar o drag horizontal |
| `front-end/src/pages/Main/Plans/styles.module.css` | affordance visual | aplicar cursor de mão e estado de dragging |
| `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | validação | cobrir o gesto de arraste |
| `front-end/src/pages/Main/Plans/index.test.tsx` | regressão leve | garantir integridade da área de planejamentos |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de contrato |
| `backend/` | sem mudança funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: grade semanal com cursor de mão e arraste horizontal por mouse
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/300-arraste-com-maozinha-na-grade-semanal-do-planejamento-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx`: ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido para adicionar hint visual persistente de “arraste para o lado”

## Proximo contexto recomendado

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
