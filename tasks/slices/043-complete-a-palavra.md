# Slice 043 - Complete a palavra (leitura e escrita)

## Status

done

## Objetivo de negocio

Jogo de ortografia: montar a palavra com letras embaralhadas, figura e TTS, por categoria e dificuldade.

## Entrega verificavel

- `gameType: word-spell`, categoria `leitura` (Leitura e Escrita)
- Várias categorias além de Insetos
- Níveis fácil / médio / difícil (palavra maior; difícil = duas palavras)
- Progresso 0/10, letras embaralhadas, botão TTS
- Prévia web + runtime mobile

## Fora de escopo

- Moedas / pontuação do print de referência
- Áudio gravado (MVP = TTS)

## Tasks relacionadas

- Task 433 — done
- Task 544 — done
- Task 552 — done (bootstrap: mesclar palavras por ID)

## Resultado

- Wiring completo do `word-spell` (contrato, bootstrap, web, mobile). Assets locais/S3 pendentes do parent.
- Task 552: bootstrap mescla palavras por ID e não apaga ajustes do admin.
