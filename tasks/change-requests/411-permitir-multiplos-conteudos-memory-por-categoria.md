# Task 411 - Permitir múltiplos conteúdos memory por categoria no banco

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Slice vertical

- Slice 034 - Jogo da memória de articulação
- `tasks/slices/034-jogo-memoria-articulacao.md`

## Resultado da execucao

- Removido índice único `ux_contents_game_type`
- Criado `ux_contents_game_type_category` em `(game_type, category)` com `WHERE game_type IS NOT NULL`
- Entity alinhada; migration `1840000000000` aplicada

## Handoff

- `.agents/state/handoffs/TASK-411.md`

## Validacoes executadas

- `npm run migration:run` ok

## Status final

done
