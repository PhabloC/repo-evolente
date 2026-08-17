# Slice 031 - Jogo caça-palavras

## Status

done

## Objetivo de negocio

Incluir um jogo de caça-palavras terapêutico no catálogo master, com execução no app do responsável.

## Entrega verificavel

- Conteúdo `word-search` no catálogo (bootstrap) com capa
- Seleção de categoria e dificuldade no mobile
- Grade com palavras em horizontal, vertical e diagonal
- Prévia jogável na biblioteca web (categoria, dificuldade, grade)

## Fora de escopo

- Editor visual de caça-palavras no master
- Multiplayer / ranking

## Tasks relacionadas

- Task 249
- Task 250
- Task 251
- Task 257
- Task 259

## Resultado consolidado adicional

- o backend do caça-palavras agora garante catálogo padrão compatível com o nível difícil e script funcional para publicação da capa
- a edição web deixou de reutilizar `WordSearchGameConfig` ao migrar um conteúdo do caça-palavras para jogos alfabéticos, evitando payload sem `letters`
