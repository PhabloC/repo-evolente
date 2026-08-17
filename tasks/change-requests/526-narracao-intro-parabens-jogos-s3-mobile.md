# Task 526 - Narração intro/parabéns dos jogos + letras alfabeto (S3 + mobile)

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- n/a (campos opcionais em `gameConfig` JSON já existente)

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- este arquivo + slice 048
- `AUDIO_ATIVIDADES.md`
- pasta `audios-atividades/`

## Contexto sob demanda

- scripts de upload existentes + bootstrap + `gameSpeechService` + renderers

## Orçamento de contexto

- médio

## Objetivo

Subir os áudios de `audios-atividades/` para o S3, vincular no `gameConfig` (intro por jogo, parabéns compartilhado, letras A–Z no alfabeto) e fazer o mobile falar intro ao entrar e parabéns ao finalizar.

## Criterios de aceite

- [x] Upload S3 nos paths `dev/games/.../audio/`
- [x] Conteúdos do catálogo com `introAudioUrl` / `finishAudioUrl`
- [x] Alfabeto: `letterAudioUrls` A–Z + `voiceMode: recorded`
- [x] Mobile toca intro ao montar o jogo
- [x] Mobile toca parabéns nos jogos com vitória
- [x] Fallback TTS se URL falhar (via `speakGameText` existente)

## Resultado da execucao

- Script `npm run upload:game-session-audios` enviou 16 intros + parabéns + 26 letras e atualizou os 16 conteúdos no banco
- Bootstrap do alfabeto passa a anexar `letterAudioUrls` + session audio; Escreva a letra anexa session audio
- `contents.service` preserva `introAudioUrl`/`finishAudioUrl` na validação
- Mobile: `GameSessionAudioProvider` no `GameActivityRenderer` + `announceFinish()` nos 13 jogos com vitória

## Contexto utilizado

- mínimo + upload script 329 + bootstrap alphabet + gameSpeechService + renderers

## Handoff

- `.agents/state/handoffs/TASK-526.md`

## Arquivos alterados

- `backend/scripts/upload-game-session-audios.mjs`
- `backend/package.json`
- `backend/src/modules/contents/game-session-audio-assets.ts`
- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `backend/src/modules/contents/contents.service.ts`
- `backend/src/modules/contents/entities/content.entity.ts`
- `mobile/src/features/games/components/GameSessionAudio/index.tsx`
- `mobile/src/features/games/renderers/GameActivityRenderer.tsx`
- 13 `*GameRenderer/index.tsx` (announceFinish)
- `mobile/src/features/trail/types/trail.ts`
- `AUDIO_ATIVIDADES.md`
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`
- `tasks/change-requests/526-narracao-intro-parabens-jogos-s3-mobile.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd backend && npm run upload:game-session-audios` — ok (16 jogos + 26 letras)
- revisão estática dos pontos `announceFinish`

## Pendencias pos-task

- Smoke no Expo: abrir um jogo (ouvir intro) e concluir (ouvir parabéns); alfabeto tocar letras gravadas
- Prioridade 2/3 do mapa de áudios (exercícios/prompts) fora deste escopo

## Status final

done
