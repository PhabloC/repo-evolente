# Handoff - Task 566

## Task

- identificador: `566`
- título: Dashboard do responsável: visão consolidada e filtro por filho
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 052
- status do slice: done

## Decisões preservadas

- Com 2+ filhos, a opção inicial é “Todos os filhos”; com 1 filho não há seletor.
- A visão agregada combina séries, atividades, áreas e relatórios de todos os filhos; adesão usa concluídos ÷ planejados totais.
- Selecionar um filho envia somente esse perfil ao summary. O filtro não é persistido.

## Contexto efetivamente usado

- Task 566, Slice 052, handoff Task 565, cadeia de summary do responsável, tipos, painéis e testes.

## Arquivos alterados

- Tipo, serviço, hook e testes de summary.
- Página, painéis e testes do dashboard do responsável.
- task, slice e índice.

## Validações executadas

- prettier e eslint focados: ok.
- `git diff --check`: ok.
- Vitest permanece impedido pelo worker do ambiente.

## Pendências ou bloqueios

- Nenhuma funcional.

## Próximo contexto recomendado

- Nenhum, salvo nova demanda sobre os gráficos do dashboard web do responsável.
