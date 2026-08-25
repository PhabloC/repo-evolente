# Handoff - Task 624

## Task

- identificador: `624`
- título: Remover borda duplicada dos ícones no perfil mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- Slice 010 — App do responsável: home, perfil e notificações
- status: done

## Decisões preservadas

- A segunda borda percebida era a sombra/elevation da pastilha clay.
- `flatIconPill` desativa essa elevação somente onde for aplicado; o Perfil usa a opção em todos os seus cards, enquanto outras telas preservam o clay existente.

## Contexto efetivamente usado

- Task/Slice, handoff 575, HomeActionCard, SubscriptionManagementCard, tela de Perfil, design system mobile e docs locais de mobile.

## Arquivos alterados

- Componentes e tela de perfil em `mobile/src/features/shell`.
- Ajuste defensivo no utilitário de data da feature children.
- Task 624, Slice 010, índice e este handoff.

## Validações executadas

- Jest da máscara: 1 suíte / 2 testes passaram.
- ESLint do escopo e `git diff --check` passaram.
- Typecheck global segue com erros preexistentes fora do escopo (Admin, Auth, jogos e trilha); sem erro nesta alteração.

## Pendências ou bloqueios

- Nenhuma para a task.

## Próximo contexto recomendado

- Nenhum, salvo novo refinamento visual do perfil mobile.
