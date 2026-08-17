# Slice 035 - Jogo dos erros (articulação)

## Status

done

## Objetivo de negocio

Incluir um jogo terapêutico de “encontre as diferenças” no catálogo de articulação: a criança compara duas imagens, clica nos erros e pratica um exercício oral por rodada.

## Entrega verificavel

- Conteúdo `spot-difference` no catálogo (`category: articulatorio`)
- 10 rodadas (1–10) com pares de imagens e hotspots clicáveis
- Após achar todas as diferenças da rodada, prompt do exercício oral
- Prévia web e execução mobile

## Fora de escopo

- Modos fácil/médio/difícil separados
- Validação automática do exercício por câmera
- Editor visual de hotspots na UI

## Tasks relacionadas

- Task 414 — done
- Task 510 — done (troca do par A/B e hotspots da rodada 1)
- Task 511 — done (troca dos pares A/B e hotspots das rodadas 2–5)
- Task 512 — done (nova rodada 6 — praia)
- Task 513 — done (nova rodada 8 — biblioteca)
- Task 514 — done (rodadas 9 aquário e 10 acampamento)
- Task 515 — done (rodada 7 fazenda; set 1–10 completo)
- Task 516 — done (imagens empilhadas no modal de prévia web)
- Task 517 — done (hotspot coração no quadro da rodada 2)
- Task 518 — done (recalibrar hotspots da rodada 3 / imagem3)
- Task 519 — done (recalibrar hotspots das rodadas 4–6)
- Task 520 — done (estrela acima do menino na imagem5 B)
- Task 521 — done (rodada 7 → sala musical)
- Task 522 — done (recalibrar hotspots 5/6/7/9)
- Task 523 — done (estrela meio img5 + balde img6)
- Task 524 — done (mobile: aspect ratio 4/3 nas imagens do runtime)

## Dependencias do slice

- Slice 028
- Slice 029
- Slice 034 (referência de exercício oral)

## Resultado

- Assets S3 + bootstrap + contrato + prévia web + runtime mobile
