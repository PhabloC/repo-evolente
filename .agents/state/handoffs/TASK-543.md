# Handoff — Task 543

## Identificador

TASK-543

## Título

Escreva a letra: frase-base + áudio da letra

## Status final

done

## Decisões preservadas

- Frase completa = `promptAudioUrl` (“Escreva a letra”) + `letterAudioUrls[letra]` (Alfabeto falado)
- Origem local estável: `audios-atividades/jogo_escreva_letra/escreva-a-letra.mp3`
- S3: `dev/games/escreva_letra/audio/escreva-a-letra.mp3`
- Upload: `npm run upload:escreva-letra-prompt-audio`
- Sem os dois clips → TTS da frase completa (não toca só a letra)

## Arquivos alterados

- backend: assets, bootstrap, script de upload, entity
- mobile: `speakGameAudioSequence` + `AlphabetWritingGameRenderer`
- front-end: `speakBrowserGameAudioSequence` + prévia em `GamePreviewModal`
- `AUDIO_ATIVIDADES.md`, task/slice/index

## Validações

- Upload S3 + update DB `alphabet-writing.promptAudioUrl` ok

## Pendências

- Smoke na prévia web / app: ouvir “Escreva a letra” + letra ao abrir e no botão Ouvir

## Próximo contexto recomendado

- Nenhuma follow-up obrigatória
