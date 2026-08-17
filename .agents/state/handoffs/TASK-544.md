# Handoff — Task 544

## Identificador

TASK-544

## Título

Descubra a palavra: áudios por categoria/dificuldade

## Status final

done

## Decisões preservadas

- Origem: `audios-atividades/jogo_descubra_palavra/{categoria}/{dificuldade}/*.mp3`
- S3: `dev/games/complete_a_palavra/audio/words/{categoria}/{dificuldade}/{wordId}.mp3`
- Campo: `words[].audioUrl`; `voiceMode: recorded` quando houver áudio
- Upload: `npm run upload:word-spell-word-audios`
- Ouvir (web/mobile) usa gravado com fallback TTS

## Sem áudio local (TTS)

- nenhum (120/120)

## Validações

- Upload: 117 arquivos matched; 0 unmatched

## Próximo contexto recomendado

- Smoke no botão Ouvir por categoria/dificuldade
- Opcional: gravar os 3 MP3s faltantes
