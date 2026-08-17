# Task 430 - Quem é o intruso: catálogo, assets, prévia e runtime

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `ContentGameType`, `OddOneOutGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/041-quem-e-o-intruso.md`

## Referencia visual

- print: `design-system/front/prints/quem-e-o-intruso-cognicao.png`
- governa: título, 4 grupos, 4 figuras + seleção do intruso
- lacunas: critério explícito nos grupos ambíguos (registrado no config)

## Objetivo

Criar `gameType: odd-one-out` com rodadas de 4 itens, `intruderId`, assets no S3, bootstrap em `raciocinio`, prévia web e mobile. Ao iniciar o jogo, as figuras de cada grupo entram em ordem aleatória.

## Comportamento esperado

- Setup + Começar
- Em cada grupo: 4 figuras embaralhadas; toque marca o intruso
- Acerto avança; erro feedback e tenta de novo
- Ordem aleatória a cada entrada no jogo

## Contexto mínimo

- AGENTS, GUIDE, context-map, 000-index, esta task, slice 041

## Orçamento de contexto

- risco: baixo-medio

## Criterios de aceite

- [x] `odd-one-out` no contrato e enums
- [x] assets no bucket
- [x] bootstrap em `raciocinio`
- [x] shuffle ao entrar
- [x] prévia web + mobile
- [x] testes essenciais

## Resultado da execucao

Implementado `odd-one-out` end-to-end: contrato, bootstrap, assets S3, prévia web com shuffle Fisher-Yates ao “Começar jogo”, renderer mobile com shuffle ao montar.

## Contexto utilizado

- print `quem-e-o-intruso-cognicao.png`
- padrão traffic-light / whats-missing
- `STORAGE_BUCKET_MAP.md`

## Handoff

- `.agents/state/handoffs/TASK-430.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/odd-one-out-game-assets.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.spec.ts`
- `backend/scripts/upload-odd-one-out-assets.mjs`
- `jogo_quem_e_o_intruso/` (assets locais)
- `front-end` tipos, `OddOneOutPreviewModal`, wiring, CSS
- `mobile` tipos, `OddOneOutGameRenderer`, wiring
- `STORAGE_BUCKET_MAP.md`
- `tasks/slices/041-quem-e-o-intruso.md`
- `tasks/000-index.md`

## Validacoes executadas

- Upload S3: 18 arquivos (`dev/games/quem_e_o_intruso/…`)
- `contents-catalog-bootstrap.service.spec.ts` — 8 passed (catálogo length 11)
- Backend hot-reload: `Default odd-one-out game` criado/atualizado

## Pendencias pos-task

- Validar visualmente a prévia na biblioteca web
- Confirmar capas geradas vs print (estilo ilustrativo)

## Status final

done
