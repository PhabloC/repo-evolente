# Task 392 - Não revelar cartas fechadas ao leitor de tela no jogo da memória mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- não se aplica

## Modo de execução

single-stack

## Slice vertical

- Slice 032 - Jogo da memória educativo
- `tasks/slices/032-jogo-memoria.md`

## Referência visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

correção de acessibilidade, sem mudança de layout

### Fonte primaria visual

- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`

## Objetivo

Impedir que o leitor de tela anuncie o conteúdo das cartas fechadas no jogo da memória, preservando a jogabilidade para usuários de tecnologia assistiva.

## Contexto mínimo

- `AGENTS.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/032-jogo-memoria.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| Label das cartas | `mobile/src/features/games/components/MemoryGameRenderer/index.tsx` | remover a identidade da carta fechada | sim |
| Cobertura atual | `mobile/src/features/games/components/MemoryGameRenderer/index.test.tsx` | regressão de acessibilidade | sim |

## Orçamento de contexto

- baixo
- estratégia: ajuste localizado no renderer e no teste do jogo da memória

## Critérios de conclusão

- [x] carta fechada não anuncia `card.label`
- [x] carta revelada/encontrada continua anunciando o conteúdo
- [x] cartas fechadas permanecem distinguíveis por posição
- [x] regressão coberta por teste
- [x] `npm test -- --testPathPattern MemoryGameRenderer` executado

## Origem

- comentário de code review (`P2 MÉDIO`) apontando que `Carta escondida ${card.label}` revelava todos os pares ao leitor de tela

## Resultado da execucao

- carta fechada passou a anunciar apenas a posição (`Carta N escondida`)
- carta revelada anuncia posição + conteúdo; par encontrado usa rótulo próprio
- teste novo garante que as 6 cartas iniciais não mencionam Alce/Cachorro/Coelho

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 032
- contexto sob demanda: renderer e teste do jogo da memória
- contexto evitado: backend, front-end web e design system

## Handoff

- `.agents/state/handoffs/TASK-392.md`

## Arquivos alterados

- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/index.test.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm test -- --testPathPattern MemoryGameRenderer`
- `cd mobile && npx eslint src/features/games/components/MemoryGameRenderer/index.tsx src/features/games/components/MemoryGameRenderer/index.test.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done
