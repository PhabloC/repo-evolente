# Handoff - Task 793

## Task

- identificador: 793
- título: Mover Encontrar profissionais para a sidebar web do responsável
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 063
- objetivo de negócio: responsável descobre profissionais cadastrados na web
- entrega verificável: item **Profissionais** na sidebar do responsável abre `/profissionais`

## Decisões preservadas

- decisão: item de nav **Profissionais**, não botão solto no rodapé da sidebar
- motivo: a página já existe e os demais destinos do responsável são itens de menu
- impacto: label curta no padrão Dashboard/Filhos/Relatórios; copy “Encontrar profissionais” ficou no `title` e no h2 da página
- decisão: botão removido só de Filhos; Cadastrar filho permanece
- motivo: o pedido era mover o atalho do diretório, não o cadastro de filho

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/793-mover-encontrar-profissionais-sidebar-web.md`
- `tasks/slices/063-diretorio-profissionais-responsavel-web.md`
- `.agents/state/handoffs/TASK-752.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/constants/navigation.ts` | itens da sidebar | incluir item só para responsável |
| `front-end/src/layout/Sidebar/index.tsx` | ícone do item | mapear Profissionais → Search |
| `front-end/src/pages/Main/Guardian/Children/` | CTA de Filhos | remover o botão |
| `front-end/docs/ai/ACCESSIBILITY.md` | UI | link com texto visível |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `requirements/` | sem ambiguidade de negócio |
| `contracts/openapi.yaml` | sem mudança de API |
| `design-system/front/` inteiro | só reuso do padrão da sidebar |
| `mobile/` | fora de escopo |
| `backend/` | fora de escopo |

## Resultado por stack

- front-end: item **Profissionais** na sidebar do responsável; botão removido de Filhos
- backend: não alterado
- mobile: não alterado

## Arquivos alterados

- `front-end/src/constants/navigation.ts`
- `front-end/src/constants/navigation.test.ts`
- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.test.tsx`
- `tasks/slices/063-diretorio-profissionais-responsavel-web.md`
- `tasks/000-index.md`
- `tasks/change-requests/793-mover-encontrar-profissionais-sidebar-web.md`

## Validações executadas

- validação: vitest navigation + Children — passou
- validação: ReadLints — sem erros
- validação: teste Sidebar de download do app — falha pré-existente de href, fora do escopo
- validação: browser autenticado — não executada (login)

## Pendências ou bloqueios

- item: nenhuma da task; validação visual autenticada pendente de conta local

## Próxima ação sugerida

- conferir no browser, logado como responsável, se o item **Profissionais** aparece entre Filhos e Relatórios e se Filhos ficou só com Cadastrar filho

## Próximo contexto recomendado

- `front-end/src/constants/navigation.ts`
- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/pages/Main/Guardian/Children/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: OpenAPI, backend, mobile, requirements
- motivo: a mudança foi só de navegação web
