# Handoff TASK-601

## Status

done

## Objetivo

Adicionar uma saída de conta ao fim do seletor de filho do responsável.

## Decisões

- Botão compartilhado `ghost`, com ícone `LogOut`, no rodapé rolável da tela.
- Reutiliza o logout existente e limpa seleção, sessão e cache.

## Contexto utilizado

- Task 601, Slice 051, handoff da Task 561, seletor e logout existente.

## Arquivos alterados

- `mobile/src/features/children/screens/SelectChildScreen.tsx`
- `mobile/src/features/children/screens/styles.ts`
- `mobile/src/features/children/hooks/useSelectChildScreen.ts`

## Validações

- eslint dos três arquivos alterados — passou
- jest `src/features/children` — passou

## Pendências

- Nenhuma.

## Próximo contexto recomendado

- Nenhum; task concluída.
