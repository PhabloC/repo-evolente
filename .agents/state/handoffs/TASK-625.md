# Handoff - Task 625

## Task

- identificador: `625`
- título: Corrigir card duplicado e pastilha de avisos na Home mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- Slice 010 — App do responsável: home, perfil e notificações
- status: done

## Decisões preservadas

- O primeiro card da seção, `Avisos da trilha`, é o único mantido na Home.
- O bloco `Assinatura sem acesso` era o segundo alerta visual e foi removido da Home.
- A pastilha do card mantido usa `flatIconPill`, sem elevation/sombra externa.

## Contexto efetivamente usado

- Task/Slice, handoff 624, tela Home, HomeActionCard, design system mobile e docs locais de mobile.

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`.
- Task 625, Slice 010, índice e este handoff.

## Validações executadas

- ESLint focado e `git diff --check` passaram.

## Pendências ou bloqueios

- Nenhuma.

## Próximo contexto recomendado

- Nenhum, salvo novo refinamento da Home mobile.
