# Task 512 - Jogo dos erros: adicionar rodada 6 (praia)

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

- n/a (só assets + hotspots)

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/035-jogo-dos-erros.md`

## Referencia visual

- `jogo_dos_erros/imagem6/` + `erros.md`
- governa: par A/B e hotspots da rodada 6

## Contexto mínimo

- handoff TASK-511
- `spot-difference-game-assets.ts`
- script de upload

## Contexto sob demanda

- `jogo_dos_erros/imagem6/erros.md`

## Orçamento de contexto

baixo

## Objetivo

Adicionar a 6ª rodada do Jogo dos erros com a cena de praia de `imagem6`, 5 hotspots, upload S3 e append no bootstrap para configs que ainda têm só 5 rodadas.

## Criterios de aceite

- [x] `rounds/round_6_a.webp` e `round_6_b.webp` a partir de `imagem6`
- [x] 5 hotspots: barquinho, bola, balde, faixa do chapéu, estrela-do-mar
- [x] Bootstrap anexa `round_6` quando ausente
- [x] Assets no S3
- [x] Specs PASS

## Dependencias

- Task 511

## Resultado da execucao

- Rodada 6 `Na praia` com 5 hotspots calibrados
- Merge passa a anexar rodadas de template ausentes (inclui `round_6` em catálogos com 5 rodadas)
- Cache-bust `?v=20260814r6`
- Upload S3: 15 assets

## Arquivos alterados

- `jogo_dos_erros/rounds/round_6_a.webp`, `round_6_b.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `tasks/change-requests/512-jogo-dos-erros-adicionar-rodada-6-praia.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest merge + bootstrap: 17 PASS
- Upload S3: ok

## Pendencias pos-task

- Reiniciar backend para anexar `round_6` no `gameConfig`
- QA de cliques na cena de praia

## Handoff

- `.agents/state/handoffs/TASK-512.md`

## Status final

done
