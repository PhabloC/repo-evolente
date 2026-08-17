# Task 429 - Pare e Vá Semáforo: catálogo, assets, prévia e runtime

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

- `contracts/openapi.yaml` — `ContentGameType`, `TrafficLightGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/040-pare-e-va-semaforo.md`

## Referencia visual

- print: `design-system/front/prints/pare-e-va-semaforo-atencao.png`
- governa: título, regras R/A/V, casas com semáforo + figura + rótulo, percurso INÍCIO/CHEGADA
- lacunas: timer; layout serpentina; estrelas persistentes

## Objetivo

Criar `gameType: traffic-light` com passos de semáforo + nomeação, assets no S3, bootstrap em `atencao`, prévia web e renderer mobile.

## Comportamento esperado

- Setup com capa modal + Como jogar (3 cores) + Começar
- Uma casa por vez: luz + figura + instrução da cor
- Avançar após nomeação (confirmação do adulto)
- Chegada ao fim do percurso

## Contexto mínimo

- AGENTS, GUIDE, context-map, 000-index, esta task, slice 040

## Contexto sob demanda

- print `pare-e-va-semaforo-atencao.png`
- padrões de spot-difference / shadow-match para bootstrap e prévia

## Orçamento de contexto

- risco: medio — 16 figuras + UI passo a passo

## Criterios de aceite

- [x] `traffic-light` no contrato e enums
- [x] assets no bucket
- [x] bootstrap em `atencao`
- [x] prévia web
- [x] mobile
- [x] testes essenciais

## Resultado da execucao

- `gameType: traffic-light` com 16 steps, regras R/A/V, bootstrap em `atencao`
- 21 assets no S3
- Prévia web e renderer mobile passo a passo

## Contexto utilizado

- print, padrões jigsaw/shadow-match, handoff implícito de jogos cognitivos

## Handoff

- `.agents/state/handoffs/TASK-429.md`

## Arquivos alterados

- backend (entity, assets, bootstrap, validation, upload, specs)
- contracts/openapi.yaml
- front-end (types, modal, wiring, CSS)
- mobile (types, renderer, wiring)
- design-system print, STORAGE_BUCKET_MAP, tasks/slice/index

## Validacoes executadas

- Upload S3: 21 assets
- Bootstrap specs pass (catálogo length 10)

## Pendencias pos-task

- Reiniciar backend se necessário; validar card na biblioteca (categoria Atenção)

## Status final

done
