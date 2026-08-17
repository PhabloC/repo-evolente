# Handoff - Task 061

## Task

- identificador: 061
- título: Alinhar atalhos do card de prioridades no dashboard
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 019 - Reproducao de shell dashboard por referencia externa
- objetivo de negócio: melhorar a leitura operacional do card de prioridades com atalhos paralelos e equivalentes
- entrega verificável: os links "Ver pacientes prioritários" e "Abrir planejamentos" aparecem lado a lado com a mesma largura

## Decisões preservadas

- decisão: resolver apenas via CSS no `ShellHome`
- motivo: o JSX já tinha dois links sem necessidade de nova semântica ou mudança estrutural
- impacto: desktop ganhou duas colunas equivalentes e o mobile manteve empilhamento em uma coluna

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/061-alinhar-atalhos-card-prioridades-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-060.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| feedback do usuario no chat | UI web | confirmar o pedido de layout |
| `front-end/AGENTS.md` | governanca local | validar stack e referencia visual |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | preservar acessibilidade basica no novo layout |
| `front-end/src/pages/Main/ShellHome/styles.module.css` | implementacao atual | ajustar a grade dos atalhos |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteracao de integracao |
| `front-end/src/pages/Main/ShellHome/index.tsx` | sem necessidade de alterar markup |
| `backend/` | ajuste estritamente visual |

## Resultado por stack

- front-end: card de prioridades com dois atalhos paralelos, largura igual e comportamento responsivo preservado
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/061-alinhar-atalhos-card-prioridades-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`

## Validações executadas

- `cd front-end && npm run test -- ShellHome`: ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- seguir apenas se houver novo ajuste fino de alinhamento, altura ou quebra de linha nos CTAs do dashboard

## Próximo contexto recomendado

- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/061-alinhar-atalhos-card-prioridades-dashboard.md`

## Contexto que não deve ser carregado na próxima etapa

- `backend/src/`
- motivo: ajuste visual local do dashboard
