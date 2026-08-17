# Task 174 - Tolerancia de tracos tortos na letra M

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

nao se aplica

## Modo de execucao

cross-stack

## Slice vertical

- `tasks/slices/030-escrita-guiada-de-letras.md`

## Contexto de negocio

### Por que

A letra M escrita de forma torta (vale mais largo/profundo, picos irregulares) estava sendo rejeitada.

### O que

Templates extras do M, limiares um pouco mais folgados e aceite estrutural (dois picos + vale + pernas).

## Criterios de aceite

- [x] M torto/com vale largo passa
- [x] forma claramente distinta (ex. linha) continua rejeitada
- [x] testes passam

## Resultado da execucao

M ganhou 3 templates adicionais, limiares 0.18/0.32 e `isSimpleM` para traços infantis com picos/vale irregulares.

## Arquivos alterados

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.test.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `tasks/change-requests/174-tolerancia-tracos-tortos-letra-m.md`
- `tasks/000-index.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-174.md`

## Validacoes executadas

- testes web — ok (12)
- testes mobile — ok (13)

## Status final

done
