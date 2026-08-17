# Task 544 - Descubra a palavra: áudios por categoria/dificuldade

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

Ligar os MP3s de `audios-atividades/jogo_descubra_palavra/{categoria}/{dificuldade}/` em cada palavra (`audioUrl`) e usar no botão Ouvir (web + mobile), com fallback TTS.

## Contexto mínimo

- `AUDIO_ATIVIDADES.md` (seção Descubra a palavra)
- `word-spell-game-assets.ts`
- `WordSpellPreviewModal` / `WordSpellGameRenderer`

## Entrega verificavel

- Upload S3 em `games/complete_a_palavra/audio/words/{categoria}/{dificuldade}/{wordId}.mp3`
- `gameConfig.categories[].words[].audioUrl` + `voiceMode: recorded`
- Ouvir toca áudio gravado quando existir

## Fora de escopo

- Gravar arquivos faltantes (ex.: avião/bicicleta no fácil, se ausentes)
