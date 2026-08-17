# Handoff TASK-511

## Task

Task 511 - Jogo dos erros: trocar imagens das rodadas 2–5

## Slice

`tasks/slices/035-jogo-dos-erros.md`

## Status final

done

## Decisões preservadas

- Mapeamento: imagem2→round_2, imagem3→round_3, imagem4→round_4, imagem5→round_5
- Títulos: Na sala de aula / Piquenique no parque / Na cozinha / No quarto
- 5 hotspots por rodada conforme cada `erros.md`, calibrados por amostragem de regiões
- Cache-bust `v=20260814r25` nas URLs `round_2`–`round_5`
- Migração por IDs legados de diferenças (não sobrescreve edições admin custom)
- Exercícios orais das rodadas 2–5 mantidos

## Contexto mínimo lido

- índice, slice 035, task 511, handoff 510
- `spot-difference-game-assets.ts`, script de upload

## Contexto sob demanda carregado

- `jogo_dos_erros/imagem{2-5}/erros.md`
- specs merge/bootstrap

## Arquivos alterados

- `jogo_dos_erros/rounds/round_{2-5}_*.webp`
- `spot-difference-game-assets.ts` + `catalog-config-merge.spec.ts`
- task/índice/slice

## Validacoes executadas

- Jest: 16 PASS
- Upload S3: ok

## Pendencias

- Restart do backend
- QA de precisão dos cliques nas 4 cenas novas (+ rodada 1)

## Proxima ação sugerida

Reiniciar backend e validar as 5 rodadas na prévia web.

## Proximo contexto recomendado

- handoffs TASK-510 e TASK-511
- não recarregar design-system / requirements

## Contexto que nao deve ser carregado

- docs front/mobile completos
- requirements globais
- histórico longo do slice 035
