# Handoff TASK-454

## Task

Enxugar página de relatórios do admin web

## Slice

`tasks/slices/017-redesign-interface-interna-web.md`

## Status final

done

## Decisões preservadas

- Removidos hero, “leituras do master”, catálogo ideal, filtros recomendados e textos de governança
- Página fica só com as 4 exportações CSV funcionais
- Comportamento de export (bloqueio enquanto uma roda, fallback de filename) preservado

## Contexto mínimo lido

- `front-end/src/pages/Main/AdminReports/index.tsx`
- `front-end/src/pages/Main/AdminReports/index.test.tsx`

## Contexto sob demanda carregado

- nenhum

## Arquivos alterados

- `front-end/src/pages/Main/AdminReports/index.tsx`
- `front-end/src/pages/Main/AdminReports/styles.module.css`
- `tasks/change-requests/454-enxugar-pagina-relatorios-admin-web.md`
- `tasks/000-index.md`
- `tasks/slices/017-redesign-interface-interna-web.md`

## Validações

- `npm run test -- src/pages/Main/AdminReports/index.test.tsx` — 2 passed

## Pendências

- nenhuma

## Nota

- Task 453 alterou `/relatorios` do profissional por engano de escopo; admin é `/admin/relatorios`

## Próxima ação sugerida

- conferir visualmente `/admin/relatorios`

## Não carregar

- mobile/, design-system completo, página de relatórios do profissional
