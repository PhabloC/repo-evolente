# Handoff TASK-517

## Task

Task 517 - Jogo dos erros: corrigir hotspot do coração no quadro (imagem2)

## Status final

done

## Decisões preservadas

- `quadro_coracao`: `(0.48, 0.26)`, radius `0.07`
- Migração: `hasMiscalibratedClassroomHeart` (round_2 + `quadro_coracao.x >= 0.7`) troca `differences` pelo template

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`

## Pendencias

- Reiniciar backend e clicar no coração na rodada 2

## Proximo contexto recomendado

- Só `spot-difference-game-assets.ts` + prévia web da rodada 2
