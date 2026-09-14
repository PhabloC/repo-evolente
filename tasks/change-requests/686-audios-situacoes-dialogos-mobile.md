## Status

done

## Título

Publicar e reproduzir áudios das situações em Diálogos em Ação

## Tipo

shared

## Stacks envolvidos

- backend
- mobile

## Contrato

Não se aplica; campo opcional `situationAudioUrl` no game config.

## Modo de execução

cross-stack

## Slice vertical

`tasks/slices/046-dialogos-em-acao.md`

## Objetivo

Adicionar narração da situação, da pergunta e das opções no jogo mobile.

## Resultado da execucao

Os 10 áudios da pasta `situações` foram enviados ao S3 e associados às etapas do catálogo. Ao abrir uma etapa, o mobile toca situação e pergunta em sequência; ao selecionar uma opção, toca o respectivo áudio.

## Contexto utilizado

- `backend/scripts/upload-game-session-audios.mjs`
- `backend/src/modules/contents/dialogue-game-assets.ts`
- `mobile/src/features/games/components/DialogueGameRenderer/index.tsx`
- `backend/src/modules/contents/contents.service.ts`
- `mobile/src/features/games/services/gameSpeechService.ts`

## Handoff

Áudios publicados sob `dev/games/dialogos_em_acao/audio/situacoes/`; vínculo persistido no game config de Diálogos em Ação.

## Arquivos alterados

- `backend/scripts/upload-game-session-audios.mjs`
- `backend/src/modules/contents/entities/content.entity.ts`
- `backend/src/modules/contents/contents.service.ts`
- `mobile/src/features/trail/types/trail.ts`
- `mobile/src/features/games/components/DialogueGameRenderer/index.tsx`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-686.md`

## Validacoes executadas

- `npm run upload:game-session-audios` — concluído; S3 e banco atualizados. Config corrigido para não enviar `voiceMode` inválido ao parser mobile.

## Pendencias pos-task

- Nenhuma.

## Status final

done
