# Task 521 - Jogo dos erros: trocar rodada 7 para sala musical

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/035-jogo-dos-erros.md`

## Referencia visual

- `jogo_dos_erros/imagem7/` + `erros.md` (sala musical)

## Objetivo

Substituir a rodada 7 (fazenda) pela nova cena de sala musical.

## Criterios de aceite

- [x] `rounds/round_7_{a|b}.webp` atualizados (`img_2`→A, `img_1`→B conforme erros.md)
- [x] Título `Na sala musical` + 5 hotspots
- [x] Assets no S3
- [x] Bootstrap migra fazenda → sala musical
- [x] Specs PASS

## Resultado da execucao

- Hotspots: camiseta, vestido, coleira, tambor, ursinho
- Cache-bust `v=20260814r7b`
- Migração `hasLegacyFarmRound`

## Arquivos alterados

- `jogo_dos_erros/rounds/round_7_{a|b}.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `tasks/change-requests/521-jogo-dos-erros-trocar-rodada-7-sala-musical.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest merge + bootstrap: 21 PASS
- Upload S3: 23 assets

## Pendencias pos-task

- Validar cliques na prévia da rodada 7

## Handoff

- `.agents/state/handoffs/TASK-521.md`

## Status final

done
