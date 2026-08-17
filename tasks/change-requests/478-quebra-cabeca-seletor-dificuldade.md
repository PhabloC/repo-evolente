# Task 478 - Quebra-cabeça: seletor de dificuldade no setup

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem mudança de schema (`difficulty` já existe nas rodadas)

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/038-quebra-cabeca.md`

## Objetivo

No setup do Quebra-cabeça, permitir escolher Fácil, Médio ou Difícil antes de começar; a partida usa só as rodadas da dificuldade selecionada.

## Criterios de aceite

- [x] Setup web com seletor Fácil/Médio/Difícil
- [x] Partida filtra rodadas pela dificuldade
- [x] Mobile com o mesmo fluxo de escolha
- [x] Handoff gerado

## Resultado da execucao

Setup com cards Fácil 3×3 / Médio 4×4 / Difícil 5×5; partida só nas cenas da dificuldade escolhida (web + mobile).

## Handoff

- `.agents/state/handoffs/TASK-478.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/jigsawGame.ts`
- `front-end/src/pages/Main/Library/JigsawPreviewModal.tsx`
- `mobile/src/features/games/utils/jigsawGame.ts`
- `mobile/src/features/games/components/JigsawGameRenderer/index.tsx`
- `mobile/src/features/games/components/JigsawGameRenderer/styles.ts`

## Status final

done
