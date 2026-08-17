# Handoff - Task 297

## Task

- identificador: 297
- titulo: Unificar design dos CTAs de dashboard, pacientes e planejamentos web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: reforcar consistencia visual entre os principais CTAs operacionais da area autenticada
- entrega verificavel: `Criar planejamento`, `Vincular por código` e `Ver pacientes` compartilham o mesmo design

## Decisoes preservadas

- o estilo de referencia adotado foi o CTA azul-claro usado na pagina de pacientes
- a padronizacao ficou isolada em `PageActionButton`, sem alterar o componente base `Button`
- os mesmos CTAs dos estados vazios em pacientes e planejamentos tambem foram alinhados ao padrao comum

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/297-unificar-design-dos-ctas-de-dashboard-pacientes-e-planejamentos-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-296.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ARCHITECTURE.md`, `COMPONENT_REUSE.md`, `ACCESSIBILITY.md` | componente compartilhado + UI web | orientar reuso e semântica |
| `front-end/src/ui/Button/**` | composição | reutilizar primitiva existente |
| `front-end/src/components/PageActionButton/**` | nova abstração | concentrar o estilo comum |
| `front-end/src/pages/Main/ShellHome/**` | CTA do dashboard | aplicar o padrão em `Criar planejamento` |
| `front-end/src/pages/Main/Patients/**` | CTA de pacientes | reaproveitar o padrão em `Vincular por código` |
| `front-end/src/pages/Main/Plans/**` | CTA de planejamentos | aplicar o padrão em `Ver pacientes` |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de contrato |
| `backend/` | sem mudança funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: CTAs operacionais de dashboard, pacientes e planejamentos unificados visualmente
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/components/PageActionButton/index.tsx`
- `front-end/src/components/PageActionButton/styles.module.css`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Plans/index.tsx`
- `tasks/change-requests/297-unificar-design-dos-ctas-de-dashboard-pacientes-e-planejamentos-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/ShellHome/index.test.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.test.tsx`: ok
- `cd front-end && npx eslint src/components/PageActionButton/index.tsx src/pages/Main/ShellHome/index.tsx src/pages/Main/ShellHome/index.test.tsx src/pages/Main/Patients/index.tsx src/pages/Main/Plans/index.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido para estender o mesmo CTA compartilhado a outras páginas internas

## Proximo contexto recomendado

- `front-end/src/components/PageActionButton/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Plans/index.tsx`
