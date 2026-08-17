# Slice 048 - Narração intro/conclusão dos jogos

## Status

done

## Objetivo de negocio

Reproduzir áudios gravados ao entrar e ao concluir os jogos terapêuticos, e completar as letras do Alfabeto falado com voz humana.

## Entrega verificavel

- Áudios de `audios-atividades/` no S3
- `introAudioUrl` + `finishAudioUrl` no `gameConfig` de cada jogo
- Alfabeto falado com `letterAudioUrls` A–Z e `voiceMode: recorded`
- Mobile: intro ao abrir o jogo; parabéns ao finalizar (quando houver vitória)

## Fora de escopo

- Prioridade 2/3 do `AUDIO_ATIVIDADES.md` (exercícios, prompts, etapas) — parcial via Task 527
- Gravação pela UI

## Tasks relacionadas

- Task 526 — done (upload S3 + vínculo no catálogo + runtime mobile)
- Task 527 — done (feedbacks curtos Prioridade 2)
- Task 538 — done (religar intros no catálogo; bootstrap não apaga mais)
- Task 542 — done (religar feedbacks curtos + prévia web)
- Task 543 — done (Escreva a letra: prompt + letra do alfabeto)
- Task 544 — done (Descubra a palavra: áudios por categoria/dificuldade)
- Task 546 — done (Jogo das Emoções: áudios de situação/estratégia)
- Task 547 — done (prévia web: parar áudio ao fechar e não cortar o parabéns)
- Task 550 — done (mobile: parar fala ao sair do jogo e não cortar o elogio na escrita)
- Task 553 — done (bootstrap: preservar intro/conclusão personalizados)

## Dependencias do slice

- Slice 026–046 (jogos do catálogo)
- Task 329 (áudio gravado alfabeto — base)

## Resultado

- S3 + DB + runtime mobile da prioridade 1 entregues
- Task 538 corrigiu wipe do bootstrap: todos os jogos do catálogo voltam a ter `introAudioUrl`
- Task 547 corrigiu cleanup da prévia web ao fechar e o corte do áudio de parabéns na conclusão
- Task 550 corrigiu stop ao sair do jogo mobile e a fila elogio → enunciado na escrita
- Task 553: bootstrap preserva intro/conclusão (e feedbacks) persistidos sobre o URL gerado
