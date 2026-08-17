# Handoff - Task 226

## Task

- 226 — done
- Página do jogo sem divisão de fundo no topo

## Decisão

- `Screen` aceita `backgroundColor`; atividade usa `colors.surface` (branco)
- Top bar e conteúdo do jogo no mesmo fundo; card do jogo sem borda de painel

## Arquivos

- `mobile/src/shared/components/Screen/*`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `AlphabetGameRenderer/styles.ts`, `AlphabetWritingGameRenderer/styles.ts`
