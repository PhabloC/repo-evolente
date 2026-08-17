# Task 540 - Prévia web Fluência: Ouvir usa áudio gravado da etapa

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (já coberto na Task 536)

## Contrato

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/045-fluencia-em-acao.md`

## Contexto mínimo

- este arquivo
- handoff TASK-536
- `FluencyPreviewModal.tsx`, `fluencyGame.ts`, tipos `FluencyStage`

## Contexto sob demanda

- mobile `FluencyGameRenderer` como referência

## Orçamento de contexto

- baixo

## Objetivo

No botão de áudio/Ouvir da prévia web de Fluência em Ação, reproduzir `stages[].audioUrl` (pasta `audio_atividades`), com fallback TTS.

## Entrega verificavel

- Clicar Ouvir toca o MP3 da etapa atual quando `audioUrl` existir

## Dependencias

- Task 536 (done)

## Resultado da execucao

- `FluencyStage.audioUrl` no tipo e no parse web
- Botão Ouvir usa `recorded` + URL da etapa (já no catálogo)

## Handoff

- `.agents/state/handoffs/TASK-540.md`

## Arquivos alterados

- `front-end/src/types/content.ts`
- `front-end/src/pages/Main/Library/fluencyGame.ts`
- `front-end/src/pages/Main/Library/FluencyPreviewModal.tsx`
- `tasks/change-requests/540-fluencia-previa-web-audio-gravado.md`
- `tasks/000-index.md`

## Validacoes executadas

- DB: 10/10 stages com audioUrl; voiceMode recorded

## Pendencias pos-task

- Smoke: Fluência → Jogar → Ouvir

## Status final

done
