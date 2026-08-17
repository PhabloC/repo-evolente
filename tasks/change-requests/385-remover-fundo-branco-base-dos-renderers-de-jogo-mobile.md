# Task 385 - Remover fundo branco base dos renderers de jogo mobile

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

- mobile; ajuste visual pedido na conversa para remover o fundo branco atrás do jogo e deixar o `bg-app.webp` aparente

## Objetivo

Remover o fundo branco estrutural dos renderers de jogo no mobile, preservando apenas superfícies internas necessárias.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-383.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/games/components/*/styles.ts` | remover o fundo branco base dos cards de jogo | sim |

## Orçamento de contexto

- baixo
- estratégia: alteração pontual só nos estilos base dos renderers de jogo

## Critérios de conclusão

- [x] jogo não exibe mais o fundo branco estrutural atrás do conteúdo
- [x] superfícies internas do jogo continuam legíveis
- [x] `npm run typecheck` segue sem diagnósticos

## Resultado da execucao

- os renderers de jogo deixaram de pintar `backgroundColor: colors.surface` no container base `card`
- o `bg-app.webp` agora aparece atrás do conteúdo principal do jogo
- painéis internos como feedback, grade, chips e áreas de escrita foram preservados com seus próprios fundos para manter legibilidade

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-383`
- contexto sob demanda: `mobile/src/features/games/components/AlphabetGameRenderer/styles.ts`, `mobile/src/features/games/components/WordSearchGameRenderer/styles.ts`, `mobile/src/features/games/components/MemoryGameRenderer/styles.ts`, `mobile/src/features/games/components/AlphabetWritingGameRenderer/styles.ts`
- contexto evitado: telas de vídeo/áudio, backend e web, porque a mudança ficou restrita à base visual dos renderers de jogo

## Handoff

- `.agents/state/handoffs/TASK-385.md`

## Arquivos alterados

- `mobile/src/features/games/components/AlphabetGameRenderer/styles.ts`
- `mobile/src/features/games/components/WordSearchGameRenderer/styles.ts`
- `mobile/src/features/games/components/MemoryGameRenderer/styles.ts`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/styles.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- nenhuma

## Status final

done
