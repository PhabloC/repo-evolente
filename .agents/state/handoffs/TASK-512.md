# Handoff TASK-512

## Task

Task 512 - Jogo dos erros: adicionar rodada 6 (praia)

## Slice

`tasks/slices/035-jogo-dos-erros.md`

## Status final

done

## Decisões preservadas

- imagem6 → `round_6` (`Na praia`)
- Hotspots: barquinho, bola_praia, balde, faixa_chapeu, estrela_mar
- Merge anexa rodadas de template ausentes (não só backfill de URLs)
- Cache-bust `v=20260814r6`
- Exercício oral novo: “Beijinho com os lábios”

## Contexto utilizado

- handoff 511, `erros.md` da imagem6, assets + specs

## Arquivos alterados

- `rounds/round_6_*.webp`
- `spot-difference-game-assets.ts` + specs
- task/índice/slice

## Validacoes

- Jest 17 PASS; upload S3 15 assets

## Pendencias

- Restart backend; QA da rodada 6

## Proxima ação sugerida

Reiniciar backend e validar a 6ª rodada na prévia.

## Proximo contexto recomendado

- handoffs 510–512
- não recarregar design-system
