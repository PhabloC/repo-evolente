# Handoff TASK-518

## Task

Task 518 - Jogo dos erros: recalibrar hotspots da imagem3 (rodada 3)

## Status final

done

## Decisões preservadas

- Hotspots round_3: balão `(0.92,0.25)`, laço `(0.80,0.40)`, borboleta `(0.49,0.23)`, maçãs `(0.33,0.88)`, coleira `(0.52,0.72)`
- Migração: `borboleta.x < 0.35` → substitui `differences` pelo template

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`

## Pendencias

- Validar cliques na rodada 3 no browser

## Proximo contexto recomendado

- Só hotspots round_3 / prévia web
