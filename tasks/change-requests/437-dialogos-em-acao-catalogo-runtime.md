# Task 437 - Diálogos em Ação: catálogo, prévia e runtime

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

- `contracts/openapi.yaml` — `ContentGameType`, `DialogueGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/046-dialogos-em-acao.md`

## Referencia visual

- print: `design-system/front/prints/dialogos-em-acao.png`
- governa: situação + ilustração + opções de fala + feedback
- fora: menu, níveis, conquistas, mic, dica

## Objetivo

Criar `gameType: dialogue` com 10 stages, bootstrap em `socializacao`, prévia web, renderer mobile e ilustrações.

## Criterios de aceite

- [x] `dialogue` no contrato e enums
- [x] bootstrap em `socializacao` com 10 stages
- [x] prévia web e runtime mobile
- [x] 10 imagens de etapa no S3
- [x] pasta `dialogos_em_acao/` para capas
- [x] sem menu / níveis / mic / dica

## Resultado da execucao

Diálogos em Ação end-to-end: 10 situações sociais, categoria Diálogo, prévia e mobile com escolha de fala; artes de etapa publicadas.

## Contexto utilizado

- Slice 046, print, padrão emotions, openapi

## Handoff

- `.agents/state/handoffs/TASK-437.md`

## Arquivos alterados

- contracts, backend dialogue assets/bootstrap/validate, front DialoguePreviewModal, mobile DialogueGameRenderer, dialogos_em_acao/stages, upload script, STORAGE_BUCKET_MAP, tasks

## Validacoes executadas

- jest bootstrap — PASS
- upload-dialogue-assets — 10 stages uploaded

## Pendencias pos-task

- Colocar capas em `dialogos_em_acao/` e rodar `node scripts/upload-dialogue-assets.mjs`

## Status final

done
