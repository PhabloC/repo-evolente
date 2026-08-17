# Handoff - Task 079

## Task

- identificador: 079
- status final: done

## Decisoes preservadas

- o ajuste ficou no `MainLayout`, porque o scroll extra vinha do documento externo e nao de uma página específica
- `html/body` ficam travados apenas no desktop autenticado; em viewport mobile o documento permanece liberado
- o scroll interno da área `.content` foi mantido como único scroll do shell

## Contexto efetivamente usado

- `tasks/change-requests/079-remover-scroll-externo-shell-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-078.md`
- `front-end/src/layout/MainLayout/{index.tsx,styles.module.css}`
- `front-end/src/styles/global.css`

## Arquivos alterados

- `front-end/src/layout/MainLayout/index.tsx`
- `tasks/change-requests/079-remover-scroll-externo-shell-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-079.md`

## Validacoes executadas

- `cd front-end && npm run lint`
- `cd front-end && npm run build`

## Pendencias ou bloqueios

- nenhuma

## Proximo contexto recomendado

- carregar a task 079 e o `MainLayout` se houver novo ajuste de scroll/comportamento global do shell autenticado
