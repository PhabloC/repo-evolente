# Task 432 - Complete a frase: catálogo, TTS, prévia e runtime

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml` — `ContentGameType`, `SentenceFillGameConfig`

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/042-complete-a-frase.md`

## Referencia visual

- print: `design-system/front/prints/complete-a-frase-linguagem.png`

## Objetivo

Criar `gameType: sentence-fill` com 10 frases, categoria `escrita` (Frases). Ao completar corretamente, TTS fala a frase completa.

## Criterios de aceite

- [x] `sentence-fill` no contrato e enums
- [x] 10 rounds no bootstrap (`escrita`)
- [x] TTS da frase completa no acerto (web + mobile)
- [x] prévia web + runtime mobile
- [x] testes bootstrap

## Resultado da execucao

Jogo Complete a frase implementado end-to-end com 10 frases, voiceMode TTS, shuffle de opções/rodadas, capas no S3.

## Handoff

- `.agents/state/handoffs/TASK-432.md`

## Status final

done
