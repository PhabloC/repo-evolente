# Task 518 - Jogo dos erros: recalibrar hotspots da imagem3 (rodada 3)

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

- `jogo_dos_erros/imagem3/` + `erros.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 035
- handoff `TASK-517.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`

## Contexto sob demanda

- specs merge
- pares A/B de `imagem3`

## Orçamento de contexto

baixo — recalibrar 5 hotspots + migração one-shot

## Objetivo

Corrigir hotspots da rodada 3 (piquenique) que estavam desalinhados: borboleta, laço, maçãs, coleira (e balão no corpo do balão). Garantir refresh no bootstrap para configs já persistidas.

## Criterios de aceite

- [x] Hotspots alinhados aos objetos reais da cena
- [x] Bootstrap recalibra round_3 quando a borboleta ainda está na posição antiga (x &lt; 0.35)
- [x] Specs merge PASS

## Dependencias

- Task 511

## Resultado da execucao

- `balao` `(0.92, 0.25)` · `laco_menina` `(0.80, 0.40)` · `borboleta` `(0.49, 0.23)` · `macas_chao` `(0.33, 0.88)` · `coleira` `(0.52, 0.72)`
- Migração `hasMiscalibratedPicnicHotspots` (borboleta.x &lt; 0.35)

## Contexto utilizado

- `imagem3/erros.md` + diff A/B
- handoff TASK-517

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/518-jogo-dos-erros-recalibrar-hotspots-imagem3.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest `catalog-config-merge.spec.ts`: 10 PASS

## Pendencias pos-task

- Validar cliques na prévia da rodada 3 após restart do backend

## Handoff

- `.agents/state/handoffs/TASK-518.md`

## Status final

done
