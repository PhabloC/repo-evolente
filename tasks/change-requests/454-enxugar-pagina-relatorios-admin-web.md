# Task 454 - Enxugar página de relatórios do admin web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- nao se aplica; preservar exportacoes CSV existentes (`users`, `professionals`, `subscriptions`, `audit-logs`)

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Remover conteudo documental/planejado da central `/admin/relatorios` e deixar apenas o necessario para exportar CSVs, com layout mais limpo.

## Criterios de conclusao

- [x] hero, resumo, catalogo e filtros recomendados removidos
- [x] grade de exportacoes CSV preservada e legivel
- [x] testes da pagina atualizados/passando
- [x] handoff e indice atualizados

## Entrega

- `/admin/relatorios` mostra apenas 4 cards de exportação CSV
- Copy curta; feedback de sucesso/erro mantido
