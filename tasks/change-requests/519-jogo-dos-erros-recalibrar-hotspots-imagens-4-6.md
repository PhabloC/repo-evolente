# Task 519 - Jogo dos erros: recalibrar hotspots das imagens 4–6

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

- `jogo_dos_erros/imagem{4,5,6}/` + respectivos `erros.md`

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, slice 035
- handoff `TASK-518.md`
- `backend/src/modules/contents/spot-difference-game-assets.ts`

## Contexto sob demanda

- specs merge
- pares A/B imagem4–6

## Orçamento de contexto

baixo — recalibrar hotspots pontuais + migração bootstrap

## Objetivo

Corrigir hotspots desalinhados:
- rodada 4: estrela da geladeira e bananas na tigela
- rodada 5: estrela decorativa na parede
- rodada 6: faixa/laço do chapéu e bola de praia

## Criterios de aceite

- [x] Hotspots alinhados aos objetos reais
- [x] Bootstrap recalibra rounds 4–6 quando coords antigas forem detectadas
- [x] Specs merge PASS

## Dependencias

- Task 511 / 512

## Resultado da execucao

- round_4: `estrela_geladeira` `(0.05,0.25)`, `frutas` `(0.86,0.44)`
- round_5: `estrela_parede` `(0.74,0.12)`
- round_6: `bola_praia` `(0.11,0.77)`, `faixa_chapeu` `(0.70,0.35)`
- Migrações one-shot por rodada no merge do bootstrap

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/519-jogo-dos-erros-recalibrar-hotspots-imagens-4-6.md`
- `tasks/slices/035-jogo-dos-erros.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest `catalog-config-merge.spec.ts`: 11 PASS

## Pendencias pos-task

- Validar cliques nas rodadas 4–6 após restart do backend

## Handoff

- `.agents/state/handoffs/TASK-519.md`

## Status final

done
