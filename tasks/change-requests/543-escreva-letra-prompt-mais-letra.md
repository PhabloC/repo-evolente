# Task 543 - Escreva a letra: frase-base + áudio da letra

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Contrato

nao aplicavel (campo em `gameConfig`, sem mudança de OpenAPI)

## Objetivo

Ao pedir a letra no jogo Escreva a letra, falar a frase completa juntando dois áudios gravados:

1. frase-base “Escreva a letra” (`audios-atividades/jogo_escreva_letra/escreva-a-letra.mp3`)
2. áudio da letra reusado do Alfabeto falado (`letterAudioUrls`)

Exemplo: Z → `escreva-a-letra.mp3` + `alphabet/audio/z.mp3`.

## Contexto mínimo

- `AUDIO_ATIVIDADES.md` (opção A de Escreva a letra)
- Task 528 (já reusa `letterAudioUrls`)
- `AlphabetWritingGameRenderer` / prévia web em `GamePreviewModal`

## Contexto sob demanda

- `backend/src/modules/contents/game-session-audio-assets.ts`
- `contents-catalog-bootstrap.service.ts` (`buildAlphabetWritingGameConfig`)
- `mobile/.../gameSpeechService.ts`
- `front-end/.../libraryGameSpeech.ts`

## Orçamento de contexto

medio — um campo `promptAudioUrl` + playback em sequência; sem redesign de UI

## Entrega verificavel

- Upload S3 em `games/escreva_letra/audio/escreva-a-letra.mp3`
- `gameConfig.promptAudioUrl` no conteúdo `alphabet-writing`
- Mobile e prévia web tocam prompt + letra em sequência (fallback TTS da frase completa)

## Fora de escopo

- 26 arquivos “Escreva a letra X” completos (opção B)
- Mudança no Alfabeto falado
