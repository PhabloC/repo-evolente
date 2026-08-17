# Task 511 - Jogo dos erros: trocar imagens das rodadas 2–5

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

- `jogo_dos_erros/imagem2/` … `imagem5/` + `erros.md` de cada pasta
- governa: pares A/B e hotspots das rodadas 2–5
- lacunas: coordenadas por diff pixel; calibrar cliques em QA

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 035
- handoff `TASK-510.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/scripts/upload-spot-difference-assets.mjs`

## Contexto sob demanda

- `jogo_dos_erros/imagem{2-5}/erros.md`
- specs merge/bootstrap

## Orçamento de contexto

baixo — troca dos 4 pares restantes + hotspots; sem UI nova

## Objetivo

Substituir as rodadas 2–5 do Jogo dos erros pelas cenas de `imagem2`–`imagem5`, com hotspots conforme cada `erros.md`, upload S3 e migração no bootstrap das cenas legadas.

## Criterios de aceite

- [x] `rounds/round_{2-5}_{a|b}.webp` atualizados a partir de `imagem2`–`imagem5`
- [x] 5 hotspots por rodada alinhados aos `erros.md`
- [x] Assets no S3
- [x] Bootstrap migra configs legadas das rodadas 2–5
- [x] Specs relevantes PASS

## Dependencias

- Task 510

## Resultado da execucao

- Rodada 2: Na sala de aula (maçã, roupa, mochila, coração no quadro, sol)
- Rodada 3: Piquenique no parque (balão, laço, borboleta, maçãs, coleira)
- Rodada 4: Na cozinha (estrela geladeira, avental, coleira gato, bebida, frutas)
- Rodada 5: No quarto (bola, travesseiro, laço ursinho, foguete, estrela parede)
- Cache-bust `?v=20260814r25` nas URLs das rodadas 2–5
- Migração automática das cenas legadas no bootstrap
- Upload S3 concluído

## Contexto utilizado

- `erros.md` de imagem2–5
- handoff TASK-510
- specs merge/bootstrap
- script de upload

## Arquivos alterados

- `jogo_dos_erros/rounds/round_{2-5}_{a|b}.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/511-jogo-dos-erros-trocar-rodadas-2-a-5.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest merge + bootstrap: 16 PASS
- Upload S3: 13 assets

## Pendencias pos-task

- Reiniciar o backend para aplicar `gameConfig` novo
- QA de cliques nas 5 rodadas (web + mobile)

## Handoff

- `.agents/state/handoffs/TASK-511.md`

## Status final

done
