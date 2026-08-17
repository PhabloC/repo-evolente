# Handoff - Task 349

## Task

- identificador: 349
- título: Reposicionar ações da trilha do paciente abaixo do header
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negócio: preservar a legibilidade do header da trilha do paciente
- entrega verificável: ações `Voltar` e `Perfil do paciente` renderizadas abaixo do heading

## Decisões preservadas

- decisão: reutilizar a variante `actionsLayout="below-heading"` já existente
- motivo: corrigir a quebra visual sem reabrir o layout global do shell
- impacto: somente a página da trilha passou a usar a variante

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/349-reposicionar-acoes-da-trilha-do-paciente-abaixo-do-header.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-348.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | UI web | manter consistência técnica e acessibilidade |
| `front-end/src/layout/Header/index.tsx` | header compartilhado | reaproveitar a variante abaixo do heading |
| `front-end/src/layout/MainLayout/index.tsx` | shell | confirmar propagação da prop |
| `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` e `index.test.tsx` | trilha do paciente | ativar e validar o novo posicionamento |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem mudança de API |
| `backend/` | fora de escopo |
| `mobile/` | fora de escopo |
| outras páginas do shell | sem gatilho explícito neste pedido |

## Resultado por stack

- front-end: trilha do paciente usa ações abaixo do heading; shell compartilhado permanece estável
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `tasks/change-requests/349-reposicionar-acoes-da-trilha-do-paciente-abaixo-do-header.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-349.md`

## Validações executadas

- `cd front-end && npx vitest run src/layout/Header/index.test.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/MainLayout/index.tsx src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente a trilha do paciente em largura desktop intermediária

## Próximo contexto recomendado

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, `mobile/`, `contracts/openapi.yaml`
- motivo: o ajuste foi exclusivamente visual no shell web
