# Handoff - Task 308

## Task

- identificador: 308
- titulo: Limitar largura maxima das acoes do header web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 017 - Redesign da interface interna web
- objetivo de negocio: conter o bloco da direita do header para preservar o heading
- entrega verificavel: busca, notificacoes e acoes ficam com largura maxima controlada e deixam de pressionar o texto da esquerda

## Decisoes preservadas

- a correção ficou apenas no CSS do `Header`
- o limite foi aplicado ao conjunto da direita, sem remover a reserva de largura da busca
- a estrutura do header e o comportamento da busca permaneceram iguais

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/308-limitar-largura-maxima-das-acoes-do-header-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-307.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | UI web | preservar semantica e isolar a mudança ao layout |
| `front-end/src/layout/Header/{index.tsx,styles.module.css,index.test.tsx}` | header compartilhado | limitar a largura maxima do bloco de acoes |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteracao de contrato |
| `backend/` | sem mudanca funcional |
| `mobile/` | escopo exclusivo da web |

## Resultado por stack

- front-end: bloco da direita do header contido por largura maxima
- backend: sem alteracoes
- mobile: sem alteracoes

## Arquivos alterados

- `front-end/src/layout/Header/styles.module.css`
- `tasks/change-requests/308-limitar-largura-maxima-das-acoes-do-header-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/layout/Header/index.test.tsx`: ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- reavaliar apenas se ainda houver quebra em uma largura específica da viewport

## Proximo contexto recomendado

- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/layout/Header/index.tsx`

## Contexto que nao deve ser carregado

- `backend/`
- `mobile/`
