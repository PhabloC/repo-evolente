# Task 527 - Feedbacks curtos compartilhados (Prioridade 2)

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Objetivo

Subir e vincular os 4 áudios de feedback de `audios-atividades/` e reproduzi-los nos jogos.

## Criterios de aceite

- [x] Upload S3 em `dev/games/_voz/audio/`
- [x] URLs no `gameConfig` de todos os jogos
- [x] Mobile: Escreva a letra → tente novamente / muito bem; Complete a frase → quase; Emoções → isso muito bem; Jogo dos erros / Semáforo → muito bem

## Resultado da execucao

- Uploaded: `muito-bem`, `tente-novamente`, `quase-escolha-outra`, `isso-muito-bem`
- Campos: `praiseAudioUrl`, `retryAudioUrl`, `almostAudioUrl`, `greatJobAudioUrl`
- `GameSessionAudio` expõe announcePraise/Retry/Almost/GreatJob

## Status final

done
