# Handoff TASK-510

## Task

Task 510 - Jogo dos erros: trocar imagens da rodada 1

## Slice

`tasks/slices/035-jogo-dos-erros.md`

## Status final

done

## Decisões preservadas

- Rodada 1 usa a cena de `jogo_dos_erros/imagem1/` (parque com crianças)
- 5 diferenças: borboleta, roupa da menina, bola, bandeirinha, banco
- Hotspots calibrados por diff pixel entre `img_1` e `img_2`
- Cena legada “Na escrivaninha” (ids `camisa`/`urso`/…) é migrada no bootstrap
- Cache-bust `v=20260814r1` nas URLs `round_1_*`
- Edições admin com diferenças custom (não legadas) continuam preservadas

## Contexto mínimo lido

- `AGENTS.md`, context-map, índice, slice 035, task 510
- `spot-difference-game-assets.ts`, script de upload

## Contexto sob demanda carregado

- `jogo_dos_erros/imagem1/erros.md`
- specs de merge/bootstrap

## Arquivos alterados

- `jogo_dos_erros/rounds/round_1_a.webp`, `round_1_b.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`
- specs de merge e bootstrap
- task/índice/slice

## Validacoes executadas

- Jest merge + bootstrap: 15 PASS
- Upload S3: 13 assets

## Pendencias

- Restart do backend para refrescar `gameConfig` no banco
- QA de precisão dos cliques
- Aguardar próximas imagens (`imagem2`+)

## Proxima ação sugerida

Reiniciar backend e validar a rodada 1 na prévia web; depois receber as demais cenas.

## Proximo contexto recomendado

- handoff desta task
- `jogo_dos_erros/imagemN/` quando existir
- não recarregar slice 035 inteiro nem histórico da 414

## Contexto que nao deve ser carregado

- design-system completo
- mobile/front docs (sem mudança de UI nesta task)
- requirements globais
