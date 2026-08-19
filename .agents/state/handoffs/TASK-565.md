# Handoff - Task 565

## Task

- identificador: `565`
- título: Remover CTA do dashboard do responsável e reduzir espaçamento
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 052
- status do slice: done

## Decisões preservadas

- “Cadastrar filho” permanece somente em Filhos e no empty state sem filhos; não no header do dashboard.
- `MainLayout.contentSpacing="compact"` reduz o espaço Header→conteúdo apenas onde for solicitado.

## Contexto efetivamente usado

- Task 565, Slice 052, handoff Task 564, dashboard, página Filhos, MainLayout e acessibilidade.

## Arquivos alterados

- Dashboard do responsável e teste.
- MainLayout e seus estilos.
- task, slice e índice.

## Validações executadas

- eslint focado: ok.
- `git diff --check`: ok.

## Pendências ou bloqueios

- Nenhuma.

## Próximo contexto recomendado

- Nenhum, salvo novo ajuste visual do dashboard web do responsável.
