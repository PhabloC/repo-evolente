# Handoff - Task 644

## Task

- TASK-644 - Corrigir salto de scroll nas abas de usuários master mobile
- Slice 009 — Administração master
- status final: done

## Decisões preservadas

- A tela mantém `ScrollView` vertical e usa `nestedScrollEnabled`/`directionalLockEnabled` para a faixa horizontal das abas.
- O conteúdo horizontal usa `alignItems: 'flex-start'` para impedir que as abas sejam esticadas verticalmente.
- Os contêineres da tela não usam mais `flexGrow`, evitando espaço artificial após listas curtas.
- O bloco principal ocupa toda a largura da tela, sem margem horizontal externa.

## Contexto efetivamente usado

- `AdminUsersScreen.tsx`, estilos da tela, padrões mobile e QA.

## Arquivos alterados

- `mobile/src/features/admin/screens/AdminUsersScreen.tsx`
- `mobile/src/features/admin/screens/usersStyles.ts`

## Validações

- Lint sem erro reportado.
- Typecheck com falhas preexistentes fora do escopo.
- 40 suites Jest aprovadas; falha preexistente em `MemoryGameRenderer`/`expo-audio`.

## Pendências

- Smoke em dispositivo/emulador para confirmar o comportamento visual nos dois sistemas.

## Próximo contexto recomendado

- Caso a regressão persista no dispositivo, investigar migração da tela para `FlatList` com cabeçalho fixo.
