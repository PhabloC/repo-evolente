# Handoff — Task 535

## Título

Áudios das frases do Complete a frase

## Status final

done

## Decisões

- `rounds[].audioUrl` → `dev/games/complete_a_frase/audio/frase-01..10.mp3`
- Origem: `audios-atividades/Jogo_complete_frase/audio_atividades/`
- Upload: `npm run upload:sentence-fill-phrase-audios`
- No acerto, mobile toca áudio gravado (fallback TTS)
- `voiceMode: recorded` quando as 10 frases têm URL
