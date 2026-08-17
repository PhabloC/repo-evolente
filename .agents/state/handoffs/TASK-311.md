# Handoff - Task 311

## Task

- identificador: 311
- titulo: Mover feedback da sugestao para baixo dos botoes da trilha web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: reposicionar o feedback da sugestão para uma leitura mais operacional
- entrega verificavel: a mensagem de sugestão aparece abaixo dos botões da semana

## Decisoes preservadas

- o callout de feedback foi mantido visualmente igual
- apenas sua posição no layout mudou, saindo da coluna de status para baixo dos CTAs
- a mudança ficou local à página da trilha

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/311-mover-feedback-da-sugestao-para-baixo-dos-botoes-da-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-310.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | UI web | preservar semântica e isolar a mudança |
| `front-end/src/pages/Main/Plans/{PatientTrail/index.tsx,styles.module.css}` | seção da trilha | mover o callout para baixo dos botões |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de contrato |
| `backend/` | sem mudança funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: feedback da sugestão reposicionado abaixo dos botões da semana
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/311-mover-feedback-da-sugestao-para-baixo-dos-botoes-da-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx`: ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se quiser reorganizar também a posição dos erros/sucessos dos outros cards da trilha

## Proximo contexto recomendado

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`

## Contexto que nao deve ser carregado

- `backend/`
- `mobile/`
