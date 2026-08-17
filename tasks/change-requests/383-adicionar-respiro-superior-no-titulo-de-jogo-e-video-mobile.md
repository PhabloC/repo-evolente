# Task 383 - Adicionar respiro superior no título de jogo e vídeo mobile

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

- mobile; ajuste visual pedido na conversa para afastar o título do topo em jogo e vídeo

## Objetivo

Adicionar um pequeno respiro superior no conteúdo de jogo e vídeo, afastando o título do topo sem reintroduzir a faixa branca anterior.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-382.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts` | adicionar margem superior no conteúdo de jogo e vídeo | sim |

## Orçamento de contexto

- baixo
- estratégia: ajuste pontual de espaçamento no conteúdo imersivo

## Critérios de conclusão

- [x] jogo ganha respiro superior sem voltar a faixa branca
- [x] vídeo ganha respiro superior sem voltar a faixa branca
- [x] `npm run typecheck` segue sem diagnósticos

## Resultado da execucao

- o container imersivo compartilhado de jogo e vídeo recebeu `paddingTop` leve para afastar o conteúdo do topo
- o respiro foi aplicado no `gameBackground`, evitando reintroduzir a faixa branca removida no ajuste anterior

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-382`
- contexto sob demanda: `mobile/src/features/trail/screens/styles.ts`
- contexto evitado: outras stacks e mudanças estruturais na tela, porque o pedido era apenas de espaçamento visual

## Handoff

- `.agents/state/handoffs/TASK-383.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/styles.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- nenhuma

## Status final

done
