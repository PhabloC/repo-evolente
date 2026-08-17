# Handoff TASK-519

## Task

Task 519 - Jogo dos erros: recalibrar hotspots das imagens 4–6

## Status final

done

## Decisões preservadas

- round_4: estrela `(0.05,0.25)`, bananas `(0.86,0.44)`
- round_5: estrela parede `(0.74,0.12)` (não o sol)
- round_6: bola `(0.11,0.77)`, faixa/laço `(0.70,0.35)`
- Migrações: cozinha `estrela.x>=0.1`; quarto `estrela.x<0.7`; praia `faixa.x<0.65`

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`

## Pendencias

- Validar cliques nas rodadas 4–6

## Proximo contexto recomendado

- Só hotspots round_4–6 / prévia web
