# Task 377 - Usar bg-app nas páginas de jogos mobile

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

- mobile; asset local `mobile/assets/bg-app.webp` e `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Objetivo

Aplicar o fundo `bg-app.webp` nas páginas de jogos do fluxo de atividades mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-376.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts` | aplicar o background apenas no fluxo de jogos | sim |
| Referência visual mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | validar aderência ao uso de fundo acolhedor e lúdico | sim |

## Orçamento de contexto

- baixo
- estratégia: alteração localizada na tela orquestradora dos jogos, sem reabrir os renderers individuais

## Critérios de conclusão

- [x] jogos usam `bg-app.webp` como fundo
- [x] vídeo e áudio permanecem sem esse fundo
- [x] build TypeScript segue sem diagnósticos

## Resultado da execucao

- o fluxo `isGame` da `TrailActivityScreen` passou a renderizar os jogos sobre `ImageBackground` com o asset local `bg-app.webp`
- vídeo e áudio permaneceram com a superfície atual, sem herdar o novo fundo
- a validação também exigiu correção de tipagem no `TrailVideoPlayer` e no `MemoryGameRenderer`, sem alterar o comportamento funcional

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-376`
- contexto sob demanda: `design-system/mobile/Design_System_Evolente_App_Mobile.md`, `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts`
- contexto adicional para validação: `mobile/src/features/trail/components/TrailVideoPlayer.tsx` e `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`
- contexto evitado: demais renderers de jogos e outras stacks, porque a mudança ficou centralizada na tela orquestradora

## Handoff

- `.agents/state/handoffs/TASK-377.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/trail/components/TrailVideoPlayer.tsx`
- `mobile/src/features/games/components/MemoryGameRenderer/index.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- nenhuma

## Status final

done
