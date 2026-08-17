# Task 539 - Prévia web Diálogos: falar prompt ao iniciar situação

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (já coberto na Task 537)

## Contrato

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/046-dialogos-em-acao.md`

## Contexto mínimo

- este arquivo + slice 046
- handoff TASK-537
- `DialoguePreviewModal.tsx`, `dialogueGame.ts`, `libraryGameSpeech.ts`

## Contexto sob demanda

- mobile `DialogueGameRenderer` só como referência de comportamento

## Orçamento de contexto

- baixo

## Objetivo

Na prévia web de Diálogos em Ação, ao iniciar/entrar em cada situação, reproduzir o áudio gravado de `promptAudioUrls` (`falar` / `fazer`) vindo de `audio_atividades`.

## Entrega verificavel

- Ao clicar Jogar e em cada nova situação, toca o MP3 correspondente ao prompt
- Fallback TTS se URL ausente

## Dependencias

- Task 537 (done) — URLs no catálogo

## Resultado da execucao

- `parseDialogueGameConfig` preserva `promptAudioUrls`
- Modal toca áudio gravado (~400ms) ao entrar em cada situação, escolhendo `falar` ou `fazer` pelo texto do prompt
- Para o áudio ao fechar/voltar

## Contexto utilizado

- handoff 537, DialoguePreviewModal, dialogueGame mobile/web

## Handoff

- `.agents/state/handoffs/TASK-539.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/DialoguePreviewModal.tsx`
- `front-end/src/pages/Main/Library/dialogueGame.ts`
- `front-end/src/types/content.ts`
- `tasks/change-requests/539-dialogos-previa-web-prompt-audio.md`
- `tasks/000-index.md`

## Validacoes executadas

- DB já tinha `promptAudioUrls.falar/fazer`
- Lint limpo nos arquivos editados

## Pendencias pos-task

- Smoke: abrir Diálogos → Jogar → ouvir “O que você pode falar?” / “fazer ou falar”

## Status final

done
