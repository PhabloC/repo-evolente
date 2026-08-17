# Handoff - Task 090

## Task

- identificador: 090
- titulo: Sincronizar dropdowns do sidebar web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 019 - Reproducao de shell dashboard por referencia externa
- objetivo de negocio: manter o shell autenticado consistente durante a navegacao
- entrega verificavel: Configuracoes e menu do usuario deixam de permanecer abertos ao mesmo tempo

## Decisoes preservadas

- o ajuste ficou restrito ao estado local do `Sidebar`, sem criar store ou alterar o contrato de navegacao
- o fechamento do menu do usuario ocorre ao abrir grupos com filhos
- o clique no usuario colapsa explicitamente os grupos expansivos para nao depender do fallback de rota ativa

## Contexto efetivamente usado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/090-sincronizar-dropdowns-sidebar-web.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-075.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/REPO_MAP.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/index.test.tsx`

## Arquivos alterados

- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/index.test.tsx`
- `tasks/change-requests/090-sincronizar-dropdowns-sidebar-web.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-090.md`

## Validacoes executadas

- `cd front-end && npm run test -- src/layout/Sidebar/index.test.tsx`
- `cd front-end && npm run lint`
- `cd front-end && npm run build`

## Pendencias ou bloqueios

- nenhuma

## Proximo contexto recomendado

- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/constants/navigation.ts`
- `front-end/src/layout/MainLayout/index.tsx`
