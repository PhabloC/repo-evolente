# Handoff TASK-513

## Task

Task 513 - Jogo dos erros: adicionar rodada 8 (biblioteca)

## Status final

done

## Decisões preservadas

- imagem8 → `round_8` (`Na biblioteca`)
- Hotspots: mochila, camiseta, coleira, capa_livro, maca
- `roundNumber` vem do id (`round_N`), não do índice do array (permite pular a 7)
- Cache-bust `v=20260814r8`
- imagem7 existe mas ficou de fora deste pedido

## Validacoes

- Jest 17 PASS; upload S3 17 assets

## Pendencias

- Restart backend
- Implementar imagem7 quando solicitado

## Proximo contexto recomendado

- handoffs 510–513
- `jogo_dos_erros/imagem7/` se for a próxima
