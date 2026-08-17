# Task 517 - Jogo dos erros: corrigir hotspot do coração no quadro (imagem2)

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

- `jogo_dos_erros/imagem2/` + `erros.md` (desenho no quadro / coração de giz)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 035
- handoff `TASK-511.md` / `TASK-516.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`

## Contexto sob demanda

- specs de merge/bootstrap
- crop A/B do quadro para calibrar clique

## Orçamento de contexto

baixo — um hotspot + migração one-shot no merge

## Objetivo

Corrigir o hotspot `quadro_coracao` da rodada 2 (estava no laço da menina) para o coração de giz no quadro, e garantir que o bootstrap atualize configs já persistidas com a coordenada errada.

## Criterios de aceite

- [x] `quadro_coracao` centrado no coração do quadro (~0.48, 0.26)
- [x] Bootstrap substitui differences da round_2 quando o hotspot legado está em x ≥ 0.7
- [x] Specs merge relevantes PASS

## Dependencias

- Task 511

## Resultado da execucao

- Hotspot `quadro_coracao` movido de `(0.76, 0.33)` (laço) para `(0.48, 0.26)` (coração no quadro), radius `0.07`
- Merge one-shot: se `round_2` tiver `quadro_coracao` com `x >= 0.7`, differences vêm do template

## Contexto utilizado

- `jogo_dos_erros/imagem2/erros.md`
- crop A/B do quadro + diff pixel
- `catalog-config-merge.spec.ts`

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/517-jogo-dos-erros-corrigir-hotspot-quadro-imagem2.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest `catalog-config-merge.spec.ts`: 9 PASS
- Jest `contents-catalog-bootstrap.service.spec.ts`: 9 PASS

## Pendencias pos-task

- Reiniciar o backend para o bootstrap regravar o hotspot no catálogo
- Validar clique no coração na prévia da rodada 2

## Handoff

- `.agents/state/handoffs/TASK-517.md`

## Status final

done
