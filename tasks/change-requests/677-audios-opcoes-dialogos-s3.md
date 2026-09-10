## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile

## Contrato

Não se aplica; `audioUrl` opcional nas opções.

## Modo de execução

cross-stack

## Slice vertical

`tasks/slices/046-dialogos-em-acao.md`

## Objetivo

Publicar e consumir os áudios individuais das opções do Diálogos em ação.

## Entrega verificável

30 MP3s enviados ao S3; cada opção recebe URL derivada da frase e toca seu áudio ao ser selecionada.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `audios-atividades/jogo_dialogos_acao/audio_atividades/opções/`
- `backend/scripts/upload-game-session-audios.mjs`

## Contexto sob demanda

- `mobile/src/features/games/services/gameSpeechService.ts`: reprodução e fallback.

## Orçamento de contexto

Baixo.

## Status final

done
