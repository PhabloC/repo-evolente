# Handoff - Task 354

## Task

- identificador: 354
- título: Refinar subtítulo do dashboard web
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign interface interna web
- objetivo de negócio: melhorar a leitura do contexto do dashboard profissional no header
- entrega verificável: dashboard com subtítulo hierarquizado e atualização destacada

## Decisões preservadas

- decisão: abrir o `subtitle` compartilhado para `ReactNode` em vez de resolver só com string e CSS
- motivo: a melhoria exigia composição semântica e visual mais rica
- impacto: o header compartilhado ficou apto a receber subtítulos compostos sem markup inválido

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/354-refinar-subtitulo-do-dashboard-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-353.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/layout/MainLayout/index.tsx` | shell | abrir a tipagem do subtítulo |
| `front-end/src/layout/Header/index.tsx` e `styles.module.css` | header | aceitar conteúdo rico e manter semântica correta |
| `front-end/src/pages/Main/ShellHome/index.tsx` e `styles.module.css` | dashboard | compor o novo bloco visual do subtítulo |
| `front-end/src/layout/Header/index.test.tsx`, `front-end/src/pages/Main/ShellHome/index.test.tsx` | validação | garantir estabilidade do shell |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| outras páginas internas | sem necessidade de ajuste nesta etapa |
| `backend/` e `mobile/` | fora do escopo |

## Resultado por stack

- front-end: subtítulo do dashboard profissional com melhor hierarquia e header compartilhado mais flexível
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/layout/Header/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/354-refinar-subtitulo-do-dashboard-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-354.md`

## Validações executadas

- `cd front-end && npm test -- --run src/layout/Header/index.test.tsx src/pages/Main/ShellHome/index.test.tsx` - ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente se o mesmo padrão de subtítulo composto deve ser aplicado a outras telas com contexto temporal forte

## Próximo contexto recomendado

- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/layout/Header/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, `mobile/`, páginas sem subtítulo composto
- motivo: a mudança foi isolada ao dashboard e ao shell compartilhado
