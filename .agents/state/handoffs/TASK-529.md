# Handoff — Task 529

## Identificador

TASK-529

## Título

Áudios dos exercícios entre rodadas do Jogo dos erros

## Status final

done

## Decisões preservadas

- Cada round tem `exercise.audioUrl` no `gameConfig` (S3: `dev/games/jogo_dos_erros/audio/exercicio-round-{1..10}.mp3`)
- Origem: `audios-atividades/jogo_erros/frases_atividades/`
- Upload: `cd backend && npm run upload:spot-difference-exercise-audios`
- Mobile: ao entrar em `phase === 'exercise'`, toca áudio gravado (~1,4s após o “Muito bem”); fallback TTS com a instrução

## Arquivos alterados

- `backend/scripts/upload-spot-difference-exercise-audios.mjs`
- `backend/package.json` (script npm)
- tipos/assets/bootstrap + parser mobile + `SpotDifferenceGameRenderer`
- `AUDIO_ATIVIDADES.md` (status Prioridade 3 / Jogo dos erros)

## Validações

- Upload: 10 arquivos → S3; content `Jogo dos erros` atualizado com `audioUrl` nas 10 rodadas
- Matching por texto da instrução alinhado às frases do mapa

## Pendências

- Smoke no app: achar todas as diferenças → ouvir exercício da rodada
- Recarregar trilha/atividade se o app ainda tiver cache do `gameConfig` antigo

## Próximo contexto recomendado

- Prioridade 3 restante (Semáforo, Complete a frase, etc.) conforme `AUDIO_ATIVIDADES.md`
