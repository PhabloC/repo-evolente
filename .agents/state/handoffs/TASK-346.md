# Handoff - Task 346

## Task

- identificador: 346
- título: Reposicionar CTA do dashboard profissional abaixo do header
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 019 - Reproducao de shell dashboard por referencia externa
- objetivo de negócio: preservar a legibilidade do header do dashboard profissional sem reabrir o layout global
- entrega verificável: CTA `Criar planejamento` abaixo do heading, com busca e notificações mantidas no topo

## Decisões preservadas

- decisão: adicionar uma variante explícita de layout no `Header`
- motivo: isolar o ajuste ao dashboard profissional sem regressão nas demais páginas
- impacto: `ShellHome` passa a usar `actionsLayout="below-heading"`; o padrão do restante do shell permanece inline

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/346-reposicionar-cta-do-dashboard-profissional-abaixo-do-header.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-055.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| print enviado pelo usuario no chat em 2026-07-29 | UI web | confirmar que o CTA deveria descer uma linha |
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | preservar a linguagem do shell |
| `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementação front | seguir padrões estruturais e de acessibilidade |
| `front-end/src/layout/Header/index.tsx` e `styles.module.css` | header compartilhado | introduzir a variante abaixo do heading |
| `front-end/src/layout/Header/index.test.tsx` | validação | cobrir a nova variante |
| `front-end/src/layout/MainLayout/index.tsx` | composição do shell | propagar a nova prop |
| `front-end/src/pages/Main/ShellHome/index.tsx` e `index.test.tsx` | dashboard profissional | ativar o layout só nesta rota |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem mudança de API |
| `backend/` | fora de escopo |
| `mobile/` | fora de escopo |
| outras telas do shell | sem gatilho para reposicionamento |

## Resultado por stack

- front-end: header suporta CTA abaixo do heading; dashboard profissional usa a nova variante
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `tasks/change-requests/346-reposicionar-cta-do-dashboard-profissional-abaixo-do-header.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-346.md`

## Validações executadas

- `cd front-end && npx vitest run src/layout/Header/index.test.tsx src/pages/Main/ShellHome/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx src/layout/MainLayout/index.tsx src/pages/Main/ShellHome/index.tsx src/pages/Main/ShellHome/index.test.tsx` - ok
- `cd front-end && npm run lint` - falhou por erros preexistentes fora do escopo em `src/components/PatientAvatar/*`, `src/pages/Main/Library/*`

## Pendências ou bloqueios

- sem bloqueio da CR; permanece dívida de lint global fora do escopo desta mudança

## Próxima ação sugerida

- validação visual rápida do dashboard profissional em largura desktop intermediária, onde a quebra apareceu

## Próximo contexto recomendado

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, `mobile/`, `contracts/openapi.yaml`
- motivo: a mudança foi exclusivamente visual no shell web
