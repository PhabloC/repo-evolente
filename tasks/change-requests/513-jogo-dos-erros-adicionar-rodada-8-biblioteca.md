# Task 513 - Jogo dos erros: adicionar rodada 8 (biblioteca)

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

- `jogo_dos_erros/imagem8/` + `erros.md`

## Objetivo

Adicionar a rodada 8 (biblioteca infantil) a partir de `imagem8`, com 5 hotspots, upload S3 e append no bootstrap.

## Criterios de aceite

- [x] `rounds/round_8_{a|b}.webp` a partir de `imagem8`
- [x] 5 hotspots: mochila, camiseta, coleira, capa do livro, maçã
- [x] Número da rodada derivado do `id` (não do índice), para não conflitar com a ausência da 7
- [x] Assets no S3
- [x] Specs PASS

## Resultado da execucao

- Rodada `round_8` / título `Na biblioteca`
- Cache-bust `?v=20260814r8`
- Upload S3: 17 assets

## Arquivos alterados

- `jogo_dos_erros/rounds/round_8_a.webp`, `round_8_b.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- specs de merge/bootstrap
- `tasks/000-index.md`, slice 035

## Validacoes executadas

- Jest: 17 PASS
- Upload S3: ok

## Pendencias pos-task

- Reiniciar backend
- `imagem7` ainda não implementada (pronta na pasta)
- QA da rodada 8

## Handoff

- `.agents/state/handoffs/TASK-513.md`

## Status final

done
