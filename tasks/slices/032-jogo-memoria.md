# Slice 032 - Jogo da memória educativo

## Status

done

## Objetivo de negocio

Incluir um jogo da memória infantil educativo no catálogo master, com cartas ilustradas por categoria, prévia web e execução no app do responsável.

## Entrega verificavel

- Conteúdo `memory` no catálogo com capa e categorias ilustradas
- Assets das cartas publicados no bucket sob prefixo estável
- Prévia jogável na biblioteca web
- Execução individual no mobile com fluxo infantil e feedback de acerto

## Fora de escopo

- Multiplayer
- Cronômetro competitivo ou ranking
- Editor visual para montar novas categorias pela UI
- Narração/áudio por carta

## Tasks relacionadas

- Task 343
- Task 344
- Task 345
- Task 392

## Dependencias do slice

- Slice 006
- Slice 028
- Slice 029

## Resultado consolidado adicional

- novo `gameType` `memory` integrado ao contrato, bootstrap do catálogo, prévia web e renderer mobile
- capa `capa_jogo_memoria.webp`, verso `capinha_jogo.webp` e 66 imagens das categorias `animais`, `cores`, `frutas` e `objetos` publicados no bucket sob `dev/games/memoria/...`
- o jogo roda em fluxo individual infantil, com escolha de categoria, pares ilustrados e feedback de acerto
- a prévia web ganhou animação de flip nas cartinhas para a troca de verso/frente
- Task 392: cartas fechadas no mobile deixam de anunciar o conteúdo ao leitor de tela; só a posição permanece na label até a carta ser revelada
