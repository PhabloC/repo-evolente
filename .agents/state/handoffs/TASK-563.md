# Handoff - Task 563

## Task

- identificador: `563`
- título: Remover cards de filhos duplicados do dashboard web do responsável
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 052
- status do slice: done

## Decisões preservadas

- A grade de atalhos de filhos não pertence ao dashboard analítico; a página Filhos continua sendo o local para esses perfis.
- Seletor de filho com 2+ filhos, painel analítico e empty state com 0 filhos permanecem.
- As consultas de progresso/trilhas exclusivas da grade removida não são mais disparadas pelo dashboard.

## Contexto efetivamente usado

- Task 563, Slice 052, handoff Task 562, componente/teste do dashboard e diretriz de acessibilidade do front-end.

## Arquivos alterados

- `front-end/src/pages/Main/Guardian/Dashboard/index.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/index.test.tsx`
- `front-end/src/pages/Main/Guardian/Dashboard/GuardianChildrenGrid.tsx` (removido)
- task, slice e índice.

## Validações executadas

- eslint focado: ok.
- Vitest não iniciou o worker; TypeScript global bloqueado por `ignoreDeprecations` inválido, ambos problemas pré-existentes do ambiente.

## Pendências ou bloqueios

- Nenhuma funcional.

## Próximo contexto recomendado

- Nenhum, salvo nova demanda para o dashboard web do responsável.
