# Handoff - Task 063

## Task

- identificador: 063
- título: Equalizar largura do CTA de cadência no dashboard
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 019 - Reproducao de shell dashboard por referencia externa
- objetivo de negócio: manter consistencia visual entre os principais CTAs do dashboard
- entrega verificável: o CTA `Abrir pacientes` ocupa largura equivalente aos demais botoes principais

## Decisões preservadas

- decisão: aplicar uma classe dedicada apenas ao CTA do card de cadencia
- motivo: evitar alterar o comportamento do link `Ir para perfil` do fluxo não profissional
- impacto: o CTA do dashboard profissional ganhou largura total no card sem efeito colateral fora dele

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/063-equalizar-largura-cta-cadencia-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-062.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| feedback do usuario no chat | UI web | confirmar a consistencia de largura desejada |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI web | preservar area clicavel e legibilidade |
| `front-end/src/pages/Main/ShellHome/index.tsx` | implementacao atual | adicionar classe dedicada no CTA correto |
| `front-end/src/pages/Main/ShellHome/styles.module.css` | implementacao atual | aplicar largura total no menor escopo |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteracao de integracao |
| `backend/` | ajuste estritamente visual |
| outras paginas do front-end | escopo restrito ao dashboard |

## Resultado por stack

- front-end: CTA `Abrir pacientes` do card de cadencia com largura equivalente aos demais botoes principais
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/063-equalizar-largura-cta-cadencia-dashboard.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`

## Validações executadas

- `cd front-end && npm run test -- ShellHome`: ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- seguir apenas se houver novo ajuste fino de alinhamento ou altura entre os CTAs da grade principal

## Próximo contexto recomendado

- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/063-equalizar-largura-cta-cadencia-dashboard.md`

## Contexto que não deve ser carregado na próxima etapa

- `backend/src/`
- motivo: ajuste visual local do dashboard
