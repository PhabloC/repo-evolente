# Handoff - Task 199

## Task

- identificador: 199
- título: Refinar modal de catálogo dos planejamentos para jogos
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 026 - Jogos terapeuticos e alfabeto falado
- objetivo de negócio: tornar a seleção de conteúdo do planejamento mais visual e operacional
- entrega verificável: modal com cards, check visual, filtro, busca compacta e paginação

## Decisões preservadas

- decisão: manter o modal aberto após selecionar um item
- motivo: o check visual só faz sentido se o usuário puder ver o estado selecionado
- impacto: o profissional pode adicionar mais de um conteúdo no mesmo fluxo sem reabrir o modal

- decisão: usar cards para todos os conteúdos e reaproveitar capa/placeholder dos jogos
- motivo: preservar consistência com a biblioteca sem bifurcar a lógica de render
- impacto: jogos ganham superfície mais rica e áudio/vídeo deixam de depender de lista textual

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/199-refinar-modal-catalogo-planejamentos-jogos.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-157.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `design-system/front/Design_System_Evolente_Desktop.md` | UI web | diretriz do modal, filtros e cards |
| `front-end/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementação front | padrões e acessibilidade |
| `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx` | modal | refino da UX |
| `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | seleção | manter modal aberto e evitar duplicação |
| `front-end/src/pages/Main/Plans/styles.module.css` | visual | layout do modal, cards e paginação |
| `front-end/src/pages/Main/Plans/AddCatalogContentModal.test.tsx` | validação | cobertura do novo comportamento |
| `front-end/src/pages/Main/Library/libraryGames.ts` | reuso | extração das helpers de capa/placeholder |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem alteração de API |
| `backend/` | fora de escopo |
| `mobile/` | fora de escopo |

## Resultado por stack

- front-end: modal de catálogo dos planejamentos redesenhado com cards, seleção persistente, filtro, busca compacta e paginação
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/AddCatalogContentModal.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/libraryGames.ts`
- `front-end/src/utils/contentGames.ts`
- `tasks/change-requests/199-refinar-modal-catalogo-planejamentos-jogos.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-199.md`

## Validações executadas

- `cd front-end && npm run lint` — ok
- `cd front-end && npx vitest run src/pages/Main/Plans/AddCatalogContentModal.test.tsx` — ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validação visual rápida no fluxo de `/planejamentos` com pelo menos dois jogos e um conteúdo não-jogo

## Próximo contexto recomendado

- `front-end/src/pages/Main/Plans/AddCatalogContentModal.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, `mobile/`
- motivo: a mudança foi exclusivamente da UX web do modal
