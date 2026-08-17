# Task 410 - Memória articulação: capa dedicada e polish do prompt

## Status

todo

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem alteração obrigatória; pode só refrescar `coverUrl` / `modalCoverUrl` / `cardBackUrl` no bootstrap

## Modo de execucao

cross-stack

## Slice vertical

- Slice 034 - Jogo da memória de articulação
- `tasks/slices/034-jogo-memoria-articulacao.md`

## Objetivo

Garantir capas dedicadas do jogo de articulação (card, modal e verso) distintas do memória cognitivo, e refinar copy/acessibilidade do prompt de exercício.

## Dependencias

- Task 408
- Task 409

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/034-jogo-memoria-articulacao.md`
- handoffs Task 408 e 409

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| capas | `jogo_memoria_articulacao/` + script upload | publicar capas dedicadas |
| UI prompt | front-end Library preview + mobile memory renderer | polish |

## Orçamento de contexto

- risco: baixo

## Criterios de aceite

- [ ] capas do card/modal/verso não reutilizam as do memória cognitivo
- [ ] prompt pós-par com copy alinhada ao objetivo do print
- [ ] checks locais relevantes passam

## Status final

todo
