# Handoff — Task 538

## Identificador

TASK-538

## Título

Religar introAudioUrl do catálogo (web/mobile)

## Slice vertical

`tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Status final

done

## Decisões preservadas

- Bootstrap deve sempre anexar `introAudioUrl`/`finishAudioUrl` via `withCatalogSessionAudio` ao rebuildar configs
- Feedbacks (`praiseAudioUrl` etc.) e `promptAudioUrls` são preservados do JSON atual
- Áudios já estavam no S3; o problema era só o vínculo no DB sendo apagado no refresh

## Contexto mínimo lido

- slice 048 + handoff 526 + bootstrap + game-session-audio-assets

## Arquivos alterados

- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`

## Validações executadas

- DB: 16/16 jogos com introAudioUrl

## Pendências

- Smoke de áudio na biblioteca web

## Próxima ação sugerida

- Abrir qualquer jogo além do Alfabeto na `/biblioteca` e confirmar a intro
