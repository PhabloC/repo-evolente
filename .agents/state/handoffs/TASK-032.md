# Handoff - Task 032

## Task

- identificador: 032
- título: Remover formas de fundo da tela auth web
- tipo: front
- modo de execução: single-stack
- status final: done
- arquivo: `tasks/change-requests/032-remover-formas-fundo-auth-web.md`

## Decisões preservadas

- decisão: remover as formas no `AuthLayout` compartilhado
- motivo: login, cadastro e recovery/reset usam o mesmo template; evita divergência por página
- impacto: todas as telas auth web deixam de renderizar as bolinhas/formas do fundo

- decisão: apagar os seletores CSS das formas
- motivo: evitar estilos mortos após remover o markup
- impacto: folha de estilos do layout fica mais simples

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/032-remover-formas-fundo-auth-web.md`
- `tasks/slices/014-template-auth-unificado.md`
- `.agents/state/handoffs/TASK-031.md`

### Evitado

- backend
- mobile
- requirements
- contrato OpenAPI

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `tasks/change-requests/032-remover-formas-fundo-auth-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-032.md`

## Validações executadas

- `npm run lint` em `front-end/` — ok

## Próxima ação sugerida

- Se quiser reduzir ainda mais o visual, o próximo ajuste natural é revisar a coluna de branding/cards do `AuthLayout`, sem mexer nos fluxos dos formulários
