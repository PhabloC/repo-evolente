# Handoff - Task 307

## Task

- identificador: 307
- titulo: Limitar largura do heading no header da trilha web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: corrigir a regressao visual do header sem alterar sua estrutura geral
- entrega verificavel: o texto da esquerda deixa de ser empurrado ao abrir a busca, com o layout original preservado

## Decisoes preservadas

- a abordagem em duas linhas da Task 306 foi revertida a pedido do usuario
- o header voltou à estrutura anterior, com mitigação por largura maxima no bloco textual
- a busca permaneceu com o comportamento funcional das Tasks 298 e 305

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/307-limitar-largura-do-heading-no-header-da-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-306.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | UI web | preservar semantica e isolar a mudança ao layout |
| `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | header compartilhado | reverter a estrutura especial e limitar a largura do heading |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteracao de contrato |
| `backend/` | sem mudanca funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: header restaurado ao layout anterior com heading limitado por largura maxima
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `tasks/change-requests/307-limitar-largura-do-heading-no-header-da-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx`: ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- reavaliar apenas se ainda houver overflow real do texto em larguras intermediarias especificas

## Proximo contexto recomendado

- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.tsx`

## Contexto que nao deve ser carregado

- `backend/`
- `mobile/`
