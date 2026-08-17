# Handoff — Task 530

## Identificador

TASK-530

## Título

Áudios das frases do Pare e Vá – Semáforo (vermelho/amarelo/verde)

## Status final

done

## Decisões preservadas

- Áudios por cor em `rules.{red|yellow|green}.audioUrl`
- S3: `dev/games/pare_e_va/audio/{vermelho|amarelo|verde}.mp3`
- Origem: `audios-atividades/jogo_semaforo/audio_atividades/`
- Upload: `cd backend && npm run upload:traffic-light-prompt-audios`
- Mobile: ao entrar em cada casa, toca o áudio da cor (~1,4s após intro/“Muito bem”)

## Validações

- Upload: 3 arquivos → S3; content Pare e Vá atualizado

## Pendências

- Smoke no app: abrir Semáforo e avançar casas R/A/V
