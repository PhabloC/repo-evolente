# Task 520 - Jogo dos erros: restaurar estrela acima do menino na imagem5 B

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- n/a

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/035-jogo-dos-erros.md`

## Referencia visual

- `jogo_dos_erros/imagem5/ChatGPT Image 14 de ago. de 2026, 14_29_46 (2).webp`
- estrela de referência em `(1).webp` acima da cabeça do menino

## Contexto mínimo

- pasta `imagem5`, `rounds/round_5_b.webp`, `spot-difference-game-assets.ts`

## Contexto sob demanda

- n/a

## Orçamento de contexto

baixo

## Objetivo

Na imagem B do quarto, preencher o espaço vazio acima da cabeça do menino com a mesma estrela amarela presente na imagem A (artefato de geração, não era a diferença intencional da parede direita).

## Criterios de aceite

- [x] Estrela copiada de A para B no mesmo lugar
- [x] `round_5_b.webp` atualizado
- [x] Upload S3 + cache-bust

## Resultado da execucao

- Estrela composta em `(2).webp` e `rounds/round_5_b.webp`
- Cache-bust `v=20260814r25b`

## Arquivos alterados

- `jogo_dos_erros/imagem5/ChatGPT Image 14 de ago. de 2026, 14_29_46 (2).webp`
- `jogo_dos_erros/rounds/round_5_b.webp`
- `backend/src/modules/contents/spot-difference-game-assets.ts`

## Validacoes executadas

- Inspeção visual do crop acima do menino

## Pendencias pos-task

- Reiniciar backend e hard-refresh da prévia

## Handoff

- `.agents/state/handoffs/TASK-520.md`

## Status final

done
