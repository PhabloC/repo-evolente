# Task 379 - Mover descrição e objetivo para card abaixo do vídeo mobile

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

- mobile; fluxo de vídeo existente no app e `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Objetivo

Exibir a descrição do vídeo e o objetivo abaixo do player dentro de um card dedicado.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-378.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts` | reorganizar o conteúdo textual da tela de vídeo | sim |
| Modelo da trilha | `mobile/src/features/trail/types/trail.ts` | confirmar quais campos existem para descrição e objetivo | sim |

## Orçamento de contexto

- baixo
- estratégia: alteração localizada na composição do ramo `isVideo`

## Critérios de conclusão

- [x] card de detalhes aparece abaixo do player
- [x] objetivo sai da área acima do vídeo
- [x] `npm run typecheck` segue sem diagnósticos

## Resultado da execucao

- o ramo `isVideo` da `TrailActivityScreen` passou a mostrar um card de detalhes logo abaixo do player
- o objetivo saiu da área superior do vídeo e foi agrupado com a descrição dentro desse card
- como o modelo da trilha não possui um campo dedicado de descrição, o card usa o título atual da atividade em `Descrição`

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-378`
- contexto sob demanda: `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts`
- validação de modelo: `mobile/src/features/trail/types/trail.ts`
- contexto evitado: contrato, outras stacks e renderers de jogo, porque a mudança ficou restrita à tela de vídeo

## Handoff

- `.agents/state/handoffs/TASK-379.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/trail/types/trail.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- existe apenas `title` e `therapeuticObjective` no modelo atual; se for necessário texto descritivo próprio para vídeo, isso precisa entrar no contrato e nos adapters

## Status final

done
