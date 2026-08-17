# Handoff — Task 546

## Identificador

TASK-546

## Título

Jogo das Emoções: áudios de situação/estratégia

## Status final

done

## Decisões preservadas

- Origem: `audios-atividades/jogo_emocoes/audio_atividades/*.mp3`
- S3: `dev/games/jogo_das_emocoes/audio/stages/{stageId}.mp3`
- Campo: `stages[].audioUrl`
- Identify: um MP3 compartilhado `identify_prompt.mp3` ligado a todas as `identify_*`
- Upload: `npm run upload:emotions-stage-audios`
- Runtime: web + mobile narram ~1,4s após entrar na etapa

## Matchers (11)

- identify_prompt (compartilhado)
- situation_festa, situation_queda, situation_trovao, situation_brinquedo, situation_excluido
- coping_raiva, coping_medo, coping_agitado, coping_triste, coping_nervoso

## Validações

- Upload + vínculo no `game_config` do conteúdo `emotions`

## Próximo contexto recomendado

- Smoke na prévia Biblioteca (web) e no app (mobile) em etapas situation/coping
