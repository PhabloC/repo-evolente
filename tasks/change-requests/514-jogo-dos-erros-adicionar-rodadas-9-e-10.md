# Task 514 - Jogo dos erros: adicionar rodadas 9 e 10

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

- `jogo_dos_erros/imagem9/` + `erros.md` (aquário)
- `jogo_dos_erros/imagem10/` + `erros.md` (acampamento)

## Objetivo

Adicionar as rodadas 9 e 10 do Jogo dos erros a partir de `imagem9` e `imagem10`, com hotspots, upload S3 e append no bootstrap.

## Criterios de aceite

- [x] `rounds/round_9_{a|b}.webp` e `round_10_{a|b}.webp`
- [x] 5 hotspots por rodada conforme `erros.md`
- [x] Assets no S3
- [x] Specs PASS

## Resultado da execucao

- Rodada 9 `No aquário` (camiseta, laço, mochila, pôster, estrela-do-mar)
- Rodada 10 `No acampamento` (mochila, casaco, coleira, lampião, cogumelos)
- Cache-bust `?v=20260814r910`
- Upload S3: 21 assets

## Arquivos alterados

- `jogo_dos_erros/rounds/round_9_*.webp`, `round_10_*.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- specs merge/bootstrap
- índice e slice 035

## Validacoes executadas

- Jest: 17 PASS
- Upload S3: ok

## Pendencias pos-task

- Reiniciar backend
- `imagem7` ainda pendente
- QA das rodadas 9 e 10

## Handoff

- `.agents/state/handoffs/TASK-514.md`

## Status final

done
