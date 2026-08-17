# Slice 044 - Jogo das Emoções (socioemocionais)

## Status

done

## Objetivo de negocio

Incluir o Jogo das Emoções no catálogo master, na categoria Socioemocionais (`emocoes`), para a criança praticar reconhecimento emocional, empatia situacional e estratégias de autorregulação.

## Entrega verificavel

- Conteúdo `emotions` no catálogo (`category: emocoes` / Socioemocionais)
- Partida com várias etapas sequenciais (identificar / situação / estratégia)
- Conteúdo sorteado do pool a cada entrada na sessão
- Prévia web e runtime mobile
- Sem mapa de fases e sem conquistas

## Fora de escopo

- Mapa / caminho / cadeados / presente
- Conquistas, medalhas e coração persistentes
- Modo Aprender separado
- Editor visual de itens pela UI

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task relacionada

## Contexto sob demanda

- print `design-system/front/prints/jogo-das-emocoes-socioemocionais.png`
- padrões `sentence-fill` / `odd-one-out` (shuffle + vitória sem mapa)
- `contracts/openapi.yaml` (ContentGameType + EmotionsGameConfig)

## Orçamento de contexto

- risco: medio — novo gameType + pool editorial + UI em 3 mecânicas

## Tasks relacionadas

- Task 434 — done
