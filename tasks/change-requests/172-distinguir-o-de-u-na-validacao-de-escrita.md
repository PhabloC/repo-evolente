# Task 172 - Distinguir O de U na validacao de escrita

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

## Referencia de design system

- sem mudança visual

## Contexto de negocio

### Por que

Ao pedir `O`, um `U` largo estava sendo aceito.

### O que

Exigir topo fechado para `O` (pontos perto do centro do topo), mantendo topo aberto para `U`.

### Fora de escopo

- biblioteca `$P`/TensorFlow.js
- UI

## Contexto mínimo

- esta task
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-171.md`
- utilitarios de escrita web/mobile

## Contexto sob demanda

| Gatilho | Fonte | Obrigatorio? |
|---|---|---|
| regra O vs U | utilitarios de escrita | sim |

## Orçamento de contexto

- baixo

## Criterios de aceite

- [x] `U` escrito quando a letra é `O` é rejeitado
- [x] `O` reconhecível continua aceito
- [x] `U` quando a letra é `U` continua aceito
- [x] testes atualizados passam

## Resultado da execucao

Adicionada regra `hasClosedTopForO` (gap ao centro do topo ≤ 0.2). Um `U` largo deixa de passar como `O`; `O` fechado continua válido.

## Arquivos alterados

- `front-end/src/pages/Main/Library/letterWritingGame.ts`
- `front-end/src/pages/Main/Library/letterWritingGame.test.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.ts`
- `mobile/src/features/games/utils/alphabetWritingGame.test.ts`
- `tasks/change-requests/172-distinguir-o-de-u-na-validacao-de-escrita.md`
- `tasks/000-index.md`
- `tasks/slices/030-escrita-guiada-de-letras.md`
- `.agents/state/handoffs/TASK-172.md`

## Validacoes executadas

- testes web letterWritingGame — ok (10)
- testes mobile alphabetWritingGame — ok (11)

## Pendencias pos-task

- smoke manual: pedir O e escrever U deve falhar; escrever O deve passar

## Status final

done
