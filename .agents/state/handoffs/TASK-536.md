# Handoff — Task 536

## Título

Áudios das etapas da Fluência em Ação

## Status final

done

## Decisões

- `stages[].audioUrl` nas 10 etapas do pool
- S3: `dev/games/fluencia_em_acao/audio/{stage}.mp3` (`rhythm_passaro` sem acento no arquivo)
- Origem: `audios-atividades/jogo_fluencia_acao/audio_atividades/`
- Upload: `npm run upload:fluency-stage-audios`
- Botão Ouvir usa `voiceMode: recorded` quando há `audioUrl`
