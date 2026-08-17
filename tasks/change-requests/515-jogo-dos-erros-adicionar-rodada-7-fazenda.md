# Task 515 - Jogo dos erros: adicionar rodada 7 (fazenda)

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

- `jogo_dos_erros/imagem7/` + `erros.md`

## Objetivo

Completar o set com a rodada 7 (fazenda/horta) a partir de `imagem7`.

## Criterios de aceite

- [x] `rounds/round_7_{a|b}.webp`
- [x] 5 hotspots: espantalho, vestido, regador, girassóis, maçãs
- [x] Assets no S3
- [x] Specs PASS

## Resultado da execucao

- Rodada `round_7` / `Na fazenda`
- Cache-bust `?v=20260814r7`
- Catálogo completo com 10 rodadas (1–10)
- Upload S3: 23 assets

## Arquivos alterados

- `jogo_dos_erros/rounds/round_7_a.webp`, `round_7_b.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- specs merge/bootstrap
- índice e slice 035

## Validacoes executadas

- Jest: 17 PASS
- Upload S3: ok

## Pendencias pos-task

- Reiniciar backend
- QA da rodada 7

## Handoff

- `.agents/state/handoffs/TASK-515.md`

## Status final

done
