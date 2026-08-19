# Handoff - Task 574

## Task

- identificador: `574`
- título: Aplicar claymorphism aos cards do perfil do responsável mobile
- status final: done

## Slice vertical

- Slice 010 — done

## Decisões preservadas

- `HomeActionCard` recebeu uma variação `clay` opt-in, usada exclusivamente nos cards do perfil do responsável.
- Dados, navegação, acessibilidade e ações dos cards não foram alterados.

## Contexto efetivamente usado

- Perfil mobile, componente compartilhado de cards, estilos e guia de reutilização.

## Arquivos alterados

- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/components/HomeActionCard/index.tsx`
- `mobile/src/features/shell/components/HomeActionCard/styles.ts`
- Task, slice e índice.

## Validações executadas

- ESLint focado e `git diff --check`: ok.
- Lint e typecheck globais têm falhas preexistentes fora deste escopo.

## Pendências

- Validar sombras no dispositivo/Expo quando disponível.

## Próximo contexto recomendado

- Nenhum, salvo ajuste visual em dispositivo.
