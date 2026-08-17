# Handoff - Task 347

## Task

- identificador: 347
- título: Reposicionar CTAs de pacientes e planejamentos abaixo do header
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negócio: evitar a compressão do heading nas páginas de pacientes e planejamentos
- entrega verificável: CTAs principais dessas duas páginas renderizados abaixo do heading

## Decisões preservadas

- decisão: reutilizar a variante `actionsLayout="below-heading"` já existente
- motivo: corrigir as páginas afetadas sem reabrir o layout global do shell
- impacto: apenas `/pacientes` e `/planejamentos` passaram a usar a variante

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/347-reposicionar-ctas-de-pacientes-e-planejamentos-abaixo-do-header.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-346.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | UI web | manter consistência técnica e acessibilidade |
| `front-end/src/layout/Header/index.tsx` e `index.test.tsx` | header compartilhado | reaproveitar a variante abaixo do heading |
| `front-end/src/layout/MainLayout/index.tsx` | shell | confirmar propagação da prop |
| `front-end/src/pages/Main/Patients/index.tsx` e `index.test.tsx` | página de pacientes | ativar e validar o novo posicionamento |
| `front-end/src/pages/Main/Plans/index.tsx` e `index.test.tsx` | página de planejamentos | ativar e validar o novo posicionamento |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem mudança de API |
| `backend/` | fora de escopo |
| `mobile/` | fora de escopo |
| outras páginas do shell | sem gatilho explícito neste pedido |

## Resultado por stack

- front-end: pacientes e planejamentos usam CTAs abaixo do heading; header compartilhado permanece estável
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`
- `tasks/change-requests/347-reposicionar-ctas-de-pacientes-e-planejamentos-abaixo-do-header.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-347.md`

## Validações executadas

- `cd front-end && npx vitest run src/layout/Header/index.test.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx src/layout/MainLayout/index.tsx src/pages/Main/Patients/index.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.tsx src/pages/Main/Plans/index.test.tsx` - ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente o header em larguras intermediárias nas rotas `/pacientes` e `/planejamentos`

## Próximo contexto recomendado

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Plans/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, `mobile/`, `contracts/openapi.yaml`
- motivo: o ajuste foi exclusivamente visual no shell web
