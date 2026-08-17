# Slice 045 - Fluência em Ação

## Status

done

## Objetivo de negocio

Incluir o jogo Fluência em Ação no catálogo master, na categoria Fluência (`fala`), para a criança praticar leitura com ritmo e clareza em etapas de texto e de palavras.

## Entrega verificavel

- Conteúdo `fluency` no catálogo (`category: fala` / Fluência)
- Pool de 10 etapas (passagem + ritmo), `roundsPerRun: 10`
- Botão ouvir com TTS e suporte a áudio gravado por etapa quando configurado; sem gravação/microfone
- Prévia web e runtime mobile
- Sem menu de níveis, conquistas ou configurações do print

## Fora de escopo

- Menu JOGAR / NÍVEIS / CONQUISTAS / CONFIGURAÇÕES
- Mapa de níveis, cadeados, estrelas e medalhas
- Microfone / gravação / avaliação por STT
- Editor visual de textos pela UI
- Capas ilustradas no S3 (pode ficar placeholder)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este slice
- task relacionada

## Contexto sob demanda

- print `design-system/front/prints/fluencia-em-acao.png`
- padrões `emotions` / `word-spell` (shuffle + TTS + vitória sem mapa)
- `contracts/openapi.yaml` (ContentGameType + FluencyGameConfig)

## Orçamento de contexto

- risco: medio — novo gameType + 2 mecânicas de UI + TTS

## Tasks relacionadas

- Task 436 — done
- Task 483 — done

## Decisões humanas confirmadas

1. Cortar menu, níveis, conquistas e configurações
2. Só botão ouvir (sem gravação)
3. 10 versões/etapas
4. Categoria Fluência (`fala`)
