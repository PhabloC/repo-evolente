# Task 528 - Escreva a letra: reusar áudios do Alfabeto falado

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile

## Slice vertical

- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Objetivo

O jogo Escreva a letra reaproveita `letterAudioUrls` A–Z do Alfabeto falado.

## Resultado

- Upload/bootstrap vinculam as mesmas URLs em `alphabet-writing`
- Renderer usa `speakGameLetter` com o áudio gravado da letra (fallback TTS se faltar)

## Status final

done
