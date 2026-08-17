# Handoff - Task 209

## Task

- identificador: 209
- título: Lupa da home: busca local de atividades e avisos
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 010 - App do responsavel: home, perfil e notificacoes
- objetivo de negócio: Completar mobile do responsavel com home, perfil e base de notificacoes
- entrega verificável: Lupa abre busca funcional sobre atividades e avisos

## Decisões preservadas

- decisão: busca client-side em modal, sem endpoint novo
- motivo: OpenAPI sem search; dados já em React Query
- impacto: `ResponsavelSearchModal` + `filterResponsavelSearch`

- decisão: tocar atividade → `TrailActivity`; tocar aviso → aba Avisos
- motivo: reutilizar navegação existente
- impacto: `onOpenActivity` no shell + home

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- task 209, slice 010, handoff 208

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| HomeHeader / HomeScreen / Shell | wire lupa | abrir modal e navegar |
| trail + notifications hooks | fontes de busca | filtrar resultados |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` completo | sem endpoint de search |
| `front-end/` / `backend/` | task mobile only |

## Resultado por stack

- mobile: lupa funcional com modal de busca local

## Arquivos alterados

- `mobile/src/features/shell/utils/filterResponsavelSearch.ts`
- `mobile/src/features/shell/utils/filterResponsavelSearch.test.ts`
- `mobile/src/features/shell/components/ResponsavelSearchModal/index.tsx`
- `mobile/src/features/shell/components/ResponsavelSearchModal/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `tasks/change-requests/209-lupa-busca-local-home-responsavel-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-209.md`

## Validações executadas

- `npm run typecheck` — ok
- `npm test -- --testPathPattern=filterResponsavelSearch` — ok (4 testes)

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- nenhuma obrigatória; eventual busca no catálogo completo exigiria nova task + contrato

## Próximo contexto recomendado

- `ResponsavelSearchModal/` se for ampliar fontes de busca

## Contexto que não deve ser carregado na próxima etapa

- fonte: backend/openapi search
- motivo: ainda fora de escopo
