# Handoff - Task 154

## Task

- identificador: 154
- status final: done

## Decisoes preservadas

- o ajuste permaneceu no `MainLayout`, porque a regressão voltou a surgir no documento externo e nao em uma página específica
- `html`, `body` e `#root` ficam travados apenas no desktop autenticado; abaixo de `960px` o documento continua livre
- o scroll da área `.content` segue como único scroll vertical do shell

## Contexto efetivamente usado

- `tasks/change-requests/154-restaurar-bloqueio-scroll-externo-shell-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-079.md`
- `front-end/src/layout/MainLayout/{index.tsx,styles.module.css}`
- `front-end/src/styles/global.css`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Arquivos alterados

- `front-end/src/layout/MainLayout/index.tsx`
- `tasks/change-requests/154-restaurar-bloqueio-scroll-externo-shell-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-154.md`

## Validacoes executadas

- `cd front-end && npm run lint`
- `cd front-end && npm run build`

## Pendencias ou bloqueios

- nenhuma

## Proximo contexto recomendado

- carregar a task 154 e o `MainLayout` se houver novo ajuste no comportamento global de scroll do shell autenticado
