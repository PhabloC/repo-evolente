# Handoff - Task 200

## Task

- identificador: 200
- título: Toggle de seleção nos cards do modal de catálogo
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 026 - Jogos terapeuticos e alfabeto falado
- objetivo de negócio: permitir marcar e desmarcar conteúdo diretamente no card do modal
- entrega verificável: segundo clique no card remove o check e desfaz a seleção

## Decisões preservadas

- decisão: manter o mesmo card como ponto único de interação para marcar e desmarcar
- motivo: reduzir fricção e evitar controles extras no modal
- impacto: a UX do modal fica consistente com um toggle visual simples

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/200-toggle-de-selecao-nos-cards-do-modal-catalogo.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-199.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementação front | padrões e acessibilidade |
| `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx` | modal | toggle do card |
| `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | seleção | remoção do item do dia atual |
| `front-end/src/pages/Main/Plans/AddCatalogContentModal.test.tsx` | validação | cobertura do toggle |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de API |
| `backend/` | fora de escopo |
| `mobile/` | fora de escopo |

## Resultado por stack

- front-end: modal do catálogo agora permite marcar e desmarcar o mesmo card por clique
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.test.tsx`
- `tasks/change-requests/200-toggle-de-selecao-nos-cards-do-modal-catalogo.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-200.md`

## Validações executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npx vitest run src/pages/Main/Plans/AddCatalogContentModal.test.tsx` — ok

## Pendências ou bloqueios

- nenhuma
