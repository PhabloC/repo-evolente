# Handoff - Task 313

## Task

- identificador: 313
- titulo: Unificar componente global de tabelas web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: reforcar consistencia visual entre as tabelas da area autenticada web
- entrega verificavel: pacientes, planejamentos, relatorios e admin passam a consumir o mesmo padrao visual de tabela a partir do `ui/Table`

## Decisoes preservadas

- o componente `ui/Table` permaneceu agnostico de dominio, concentrando apenas o padrao visual compartilhado
- a unificacao foi feita removendo overrides locais de skin em vez de criar variantes por pagina
- o cabecalho padrao adotado usa o gradiente suave ja alinhado ao design system web

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/313-unificar-componente-global-de-tabelas-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-312.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `COMPONENT_REUSE.md`, `ACCESSIBILITY.md` | componente compartilhado + UI web | posicionar o refactor no `ui/Table` e preservar semantica |
| `front-end/src/ui/Table/{index.tsx,styles.module.css}` | componente global existente | consolidar layout e cabecalho padrao |
| `front-end/src/pages/Main/Patients/**` | override visual local | remover skin propria da tabela de pacientes |
| `front-end/src/pages/Main/Plans/**` | override visual local | remover skin propria da tabela de planejamentos |
| `front-end/src/pages/Main/Reports/**` | override visual local | remover override global do cabecalho de relatorios |
| `front-end/src/pages/Main/{Admin,AdminUsers}/**` | compatibilidade | conferir que as demais tabelas continuam sobre o componente base |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteracao de contrato |
| `backend/` | sem mudanca funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: tabelas unificadas visualmente pelo componente global `Table`
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/ui/Table/index.test.tsx`
- `front-end/src/ui/Table/styles.module.css`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/styles.module.css`
- `front-end/src/pages/Main/Plans/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/313-unificar-componente-global-de-tabelas-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/ui/Table/index.test.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.test.tsx`: ok
- `cd front-end && npx eslint src/ui/Table/index.tsx src/ui/Table/index.test.tsx src/pages/Main/Patients/index.tsx src/pages/Main/Plans/index.tsx`: ok
- `rg -n ":global\\(\\.table th\\)|\\.patientsTable|\\.plansTable|className=\\{styles\\.(patientsTable|plansTable)\\}" front-end/src`: sem ocorrencias

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido para aplicar o mesmo nivel de consolidacao tambem nas barras de paginacao das tabelas

## Proximo contexto recomendado

- `front-end/src/ui/Table/index.tsx`
- `front-end/src/ui/Table/styles.module.css`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Plans/index.tsx`
- `front-end/src/pages/Main/Reports/index.tsx`
