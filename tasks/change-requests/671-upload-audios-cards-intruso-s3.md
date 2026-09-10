## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica; `audioUrl` é opcional no item do jogo.

## Modo de execução

cross-stack

## Slice vertical

`tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Objetivo

Publicar no S3 os áudios das gravuras do jogo Quem é o intruso e consumi-los no mobile.

## Entrega verificável

O script de upload envia os MP3s para `games/quem_e_o_intruso/audio/figuras/{id}.mp3`, vincula as URLs ao `game_config` e o mobile reproduz o áudio ao selecionar o card.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `audios-atividades/jogo_quem_intruso/audio_atividades/figuras/`
- `backend/scripts/upload-game-session-audios.mjs`

## Contexto sob demanda

- `backend/src/patterns/adapters/s3-media-storage.adapter.ts`: configuração S3.
- `mobile/src/features/games/services/gameSpeechService.ts`: reprodução e fallback.

## Orçamento de contexto

Baixo.

## Status final

done
