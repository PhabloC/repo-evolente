# Task 546 - Jogo das Emoções: áudios de situação/estratégia

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

nao aplicavel

## Objetivo

Ligar os 10 MP3s de `audios-atividades/jogo_emocoes/audio_atividades/` nas etapas com `sceneText` (`stages[].audioUrl`) e narrar ao entrar na etapa (web + mobile), com fallback TTS.

## Contexto mínimo

- `AUDIO_ATIVIDADES.md` (seção 13)
- `emotions-game-assets.ts`
- `EmotionsPreviewModal` / `EmotionsGameRenderer`

## Contexto sob demanda

- scripts `upload-*-audios.mjs` (padrão fluency)

## Orçamento de contexto

baixo — vertical slice de narração já conhecido

## Entrega verificavel

- Upload S3 em `games/jogo_das_emocoes/audio/stages/{stageId}.mp3`
- `gameConfig.stages[].audioUrl` nas 10 etapas situation/coping
- Prévia web e mobile tocam gravado ~1,4s após entrar na etapa

## Fora de escopo

- Áudio para etapas `identify_*` (só expressão)
- Gravação pela UI
