# Task 381 - Remover faixa superior residual em jogo e vídeo mobile

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

não se aplica

## Modo de execução

single-stack

## Slice vertical

- Slice 008 - Trilhas semanais e evolução
- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referência visual

- mobile; ajuste visual pedido na conversa para remover a faixa branca residual no topo de jogo e vídeo

## Objetivo

Eliminar a faixa superior residual nas telas de jogo e vídeo após a remoção da barra com seta/check.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-380.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts` | remover o espaçamento residual no topo de jogo e vídeo | sim |
| Shell visual | `mobile/src/shared/components/Screen/styles.ts` | confirmar a origem do padding padrão | sim |

## Orçamento de contexto

- baixo
- estratégia: ajuste pontual no content style da tela de atividade

## Critérios de conclusão

- [x] jogo e vídeo não exibem mais a faixa branca residual no topo
- [x] áudio preserva o espaçamento atual
- [x] `npm run typecheck` segue sem diagnósticos

## Resultado da execucao

- jogo e vídeo passaram a usar um `contentStyle` sem `paddingTop` na `TrailActivityScreen`
- o fluxo de áudio preservou o `contentStyle` anterior com espaçamento superior
- a faixa branca residual no topo foi removida na origem, sem alterar a `Screen` compartilhada

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-380`
- contexto sob demanda: `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts`
- shell visual: `mobile/src/shared/components/Screen/styles.ts`
- contexto evitado: outras stacks e renderers, porque a correção ficou na composição local da tela

## Handoff

- `.agents/state/handoffs/TASK-381.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- nenhuma

## Status final

done
