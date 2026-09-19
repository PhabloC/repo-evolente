# Slice 034 - Jogo da memória de articulação

## Status

in_progress

## Objetivo de negocio

Incluir um jogo da memória terapêutico de articulação (motricidade orofacial) no catálogo, com cartas de exercícios orais, assets no bucket, prévia web e execução no app do responsável — modos fácil, médio e difícil.

## Entrega verificavel

- Conteúdo `memory` dedicado na categoria `articulatorio`
- Categorias `facil` (9), `medio` (16) e `dificil` (12) com imagens públicas no bucket
- Prompt pós-acerto pedindo que a criança execute o exercício
- Prévia jogável na biblioteca web (aba Articulação)
- Execução individual no mobile com fluxo infantil

## Fora de escopo

- Validação automática do exercício por câmera/IA
- Narração/áudio específico por carta
- Multiplayer ou ranking
- Editor visual de cartas pela UI

## Tasks relacionadas

- Task 408 — done
- Task 409 — done
- Task 410 — todo
- Task 411 — done
- Task 412 — done
- Task 413 — done
- Task 712 — done (áudio de instrução após o feedback de acerto)

## Dependencias do slice

- Slice 028
- Slice 029
- Slice 032

## Resultado parcial

- Assets no S3 + bootstrap + contrato (408)
- Prompt pós-par na prévia web e no mobile (409)
- Índice único (game_type, category) (411)
- Modo difícil (ex-intermediário) com 12 cartas (412)
- Modo fácil com 9 cartas (413)
- Pendente: polish de capas/prompt (410)
- Áudio global de instrução pós-acerto publicado e encadeado no mobile e na prévia web (712)
