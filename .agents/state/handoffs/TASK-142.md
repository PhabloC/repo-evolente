# Handoff - Task 142

## Identificador

- Task 142 - Corrigir cache dos SVGs dos heroes no Android mobile
- `tasks/change-requests/142-corrigir-cache-dos-svgs-dos-heroes-no-android-mobile.md`

## Slice vertical

- Slice 022 - Linguagem visual do print aplicada as telas mobile
- `tasks/slices/022-linguagem-visual-print-telas-mobile.md`

## Status final

done

## Decisoes preservadas

- O cache dos SVGs foi mantido, mas a leitura mudou de `fetch` para `readAsStringAsync`
- A mudanca ficou isolada no utilitario de preload, sem alterar os heroes consumidores

## Arquivos alterados

- `mobile/src/shared/assets/heroBackgroundSvgCache.ts`

## Validacoes executadas

- `npm run lint` ok
- `npm run typecheck` ok
