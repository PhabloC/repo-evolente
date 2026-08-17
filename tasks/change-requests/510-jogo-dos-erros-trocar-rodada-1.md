# Task 510 - Jogo dos erros: trocar imagens da rodada 1

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

- n/a (só assets + hotspots do `SpotDifferenceGameConfig` já existente)

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/035-jogo-dos-erros.md`

## Referencia visual

- origem local: `jogo_dos_erros/imagem1/img_1.webp` + `jogo_dos_erros/imagem1/img_2.webp`
- diferenças documentadas: `jogo_dos_erros/imagem1/erros.md`
- governa: par A/B e hotspots clicáveis da rodada 1
- lacunas: coordenadas calibradas por diff pixel; validar clique em QA web/mobile

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/035-jogo-dos-erros.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/scripts/upload-spot-difference-assets.mjs`

## Contexto sob demanda

- `jogo_dos_erros/imagem1/erros.md` — labels das 5 diferenças
- specs de bootstrap/merge — migração da cena antiga “escrivaninha”
- upload S3 via script existente

## Orçamento de contexto

baixo — troca de um par de assets + hotspots da rodada 1; sem UI nova

## Objetivo

Substituir o par de imagens da rodada 1 do Jogo dos erros pela cena de `jogo_dos_erros/imagem1/`, atualizar os 5 hotspots conforme `erros.md`, publicar no S3 e fazer o bootstrap refrescar config legada.

## Criterios de aceite

- [x] `rounds/round_1_a.webp` e `round_1_b.webp` iguais a `imagem1/img_1.webp` e `img_2.webp`
- [x] Hotspots da rodada 1: borboleta, roupa da menina, bola, bandeirinha, banco
- [x] Assets no S3 sob `games/jogo_dos_erros/rounds/`
- [x] Bootstrap migra rodada legada “Na escrivaninha” para a nova cena
- [x] Specs de assets/bootstrap relevantes PASS

## Dependencias

- Slice 035 / Task 414

## Resultado da execucao

- Par local da rodada 1 substituído pela cena do parque (`imagem1`)
- Template com título `Brincando no parque` e 5 hotspots calibrados
- Cache-bust `?v=20260814r1` nas URLs da rodada 1
- Migração automática da cena legada “escrivaninha” no bootstrap
- Upload S3 concluído (13 assets do jogo)

## Contexto utilizado

- `jogo_dos_erros/imagem1/erros.md`
- `spot-difference-game-assets.ts` + specs de merge/bootstrap
- script `upload-spot-difference-assets.mjs`

## Arquivos alterados

- `jogo_dos_erros/rounds/round_1_a.webp`
- `jogo_dos_erros/rounds/round_1_b.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `tasks/change-requests/510-jogo-dos-erros-trocar-rodada-1.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npx jest catalog-config-merge.spec.ts contents-catalog-bootstrap.service.spec.ts` — 15 PASS
- upload S3 — ok

## Pendencias pos-task

- Reiniciar o backend para o bootstrap aplicar hotspots/URLs novos no banco
- QA de cliques nos 5 hotspots (web prévia + mobile)
- Próximas cenas (`imagem2`…) quando disponíveis

## Handoff

- `.agents/state/handoffs/TASK-510.md`

## Status final

done
