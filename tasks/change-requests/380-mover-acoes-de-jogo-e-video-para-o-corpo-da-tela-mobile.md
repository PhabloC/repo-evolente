# Task 380 - Mover ações de jogo e vídeo para o corpo da tela mobile

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

- mobile; fluxo atual de atividade e referência enviada na conversa para remover o topo com seta/check em jogo e vídeo

## Objetivo

Remover a seção superior com seta/check nas telas de jogo e vídeo, deixando as ações `Concluir atividade` e `Voltar` dentro da própria página.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-379.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts` | mover as ações de jogo e vídeo para o corpo da tela | sim |

## Orçamento de contexto

- baixo
- estratégia: alteração localizada na composição e nos estilos da tela de atividade

## Critérios de conclusão

- [x] jogo e vídeo deixam de exibir a barra superior com seta/check
- [x] jogo e vídeo passam a exibir `Concluir atividade` e `Voltar` no corpo da página
- [x] `npm run typecheck` segue sem diagnósticos

## Resultado da execucao

- a barra superior com seta/check foi mantida apenas para áudio
- os fluxos de jogo e vídeo passaram a renderizar as ações no corpo da página, com `Concluir atividade` seguido por `Voltar`
- o botão de concluir do vídeo foi consolidado nesse bloco compartilhado de ações

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-379`
- contexto sob demanda: `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts`
- contexto evitado: outras stacks, contrato e renderers específicos dos jogos, porque a mudança ficou centralizada na tela de atividade

## Handoff

- `.agents/state/handoffs/TASK-380.md`

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
