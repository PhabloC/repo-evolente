# Task 378 - Usar bg-app nas páginas de vídeo mobile

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

Aplicar o fundo `bg-app.webp` também nas páginas de vídeo do fluxo de atividades mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-377.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `mobile/src/features/trail/screens/styles.ts` | estender o fundo para o fluxo de vídeo | sim |

## Orçamento de contexto

- baixo
- estratégia: alteração localizada na mesma tela orquestradora do fluxo de atividade

## Critérios de conclusão

- [x] vídeo usa `bg-app.webp` como fundo
- [x] jogo preserva o fundo já aplicado
- [x] `npm run typecheck` segue sem diagnósticos

## Resultado da execucao

- o fluxo `isVideo` da `TrailActivityScreen` passou a renderizar o conteúdo sobre `ImageBackground` com o asset local `bg-app.webp`
- o mesmo `contentContainerStyle` usado nos jogos foi estendido ao vídeo para o fundo preencher toda a área útil
- o fluxo de jogo permaneceu inalterado e o de áudio continuou sem esse fundo

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, Slice 008 e handoff `TASK-377`
- contexto sob demanda: `mobile/src/features/trail/screens/TrailActivityScreen.tsx` e `mobile/src/features/trail/screens/styles.ts`
- contexto evitado: outros renderers de jogos, player e outras stacks, porque a mudança ficou restrita à composição da tela

## Handoff

- `.agents/state/handoffs/TASK-378.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- nenhuma

## Status final

done
