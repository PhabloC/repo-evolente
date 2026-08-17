# Task 538 - Religar introAudioUrl do catálogo (web/mobile)

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- n/a (campos opcionais em `gameConfig` JSON)

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/048-narracao-intro-conclusao-jogos.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- este arquivo + slice 048
- handoff TASK-526
- `contents-catalog-bootstrap.service.ts` + `game-session-audio-assets.ts`

## Contexto sob demanda

- `scripts/upload-game-session-audios.mjs` se precisar reenviar/religar no S3/DB
- preview web `useGameIntroAudio` só para validação manual

## Orçamento de contexto

- baixo/médio

## Objetivo

Restaurar `introAudioUrl`/`finishAudioUrl` em todos os jogos do catálogo (hoje só Alfabeto/Escreva a letra têm) e impedir que o bootstrap apague esses campos no refresh.

## Entrega verificavel

- DB: todos os jogos `media_type=game` com `introAudioUrl` preenchido
- Bootstrap anexa session audio ao rebuild de cada jogo
- Abrir modal na biblioteca (exceto só alfabeto) toca a intro

## Fora de escopo

- Prioridade 3 de áudios
- Mudança de UI web

## Dependencias

- Task 526 (done)

## Resultado da execucao

- Causa: bootstrap refresh salvava `gameConfig` sem `introAudioUrl` e apagava os links do upload (só alfabeto sobrevivia porque o build reanexa).
- Fix: `withCatalogSessionAudio` + `needsSessionAudioAttach` em todos os `ensure*` de jogos.
- Após restart, 16/16 jogos no DB com `introAudioUrl` apontando para o S3.

## Contexto utilizado

- slice 048, handoff 526, bootstrap, game-session-audio-assets, query DB

## Handoff

- `.agents/state/handoffs/TASK-538.md`

## Arquivos alterados

- `backend/src/modules/contents/contents-catalog-bootstrap.service.ts`
- `tasks/change-requests/538-religar-intro-audio-catalogo-jogos.md`
- `tasks/slices/048-narracao-intro-conclusao-jogos.md`
- `tasks/000-index.md`

## Validacoes executadas

- Nest compilou sem erros e bootstrap refreshou todos os jogos
- Query DB: todos os 16 jogos com `introAudioUrl` = yes

## Pendencias pos-task

- Smoke manual: abrir 2–3 modais na biblioteca (ex.: memória, caça-palavras) e confirmar intro

## Status final

done
