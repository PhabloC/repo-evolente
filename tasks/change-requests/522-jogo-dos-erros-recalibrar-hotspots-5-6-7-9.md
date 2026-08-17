# Task 522 - Jogo dos erros: recalibrar hotspots imagens 5, 6, 7 e 9

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

## Objetivo

Corrigir hotspots desalinhados nas rodadas 5, 6, 7 e 9.

## Criterios de aceite

- [x] Hotspots alinhados
- [x] Bootstrap migra coords antigas
- [x] Specs PASS

## Resultado da execucao

- round_5 `estrela_parede` `(0.80, 0.06)`
- round_6 `bola_praia` `(0.07, 0.70)`
- round_7 `ursinho` `(0.22, 0.52)` — estante esquerda
- round_9 `poster_peixes` `(0.22, 0.29)` — Ocean Friends na parede

## Arquivos alterados

- `backend/src/modules/contents/spot-difference-game-assets.ts`
- `backend/src/modules/contents/catalog-config-merge.spec.ts`
- `tasks/change-requests/522-jogo-dos-erros-recalibrar-hotspots-5-6-7-9.md`
- `tasks/000-index.md`
- `tasks/slices/035-jogo-dos-erros.md`

## Validacoes executadas

- Jest merge: 13 PASS

## Pendencias pos-task

- Validar cliques nas rodadas 5, 6, 7 e 9

## Handoff

- `.agents/state/handoffs/TASK-522.md`

## Status final

done
