# Task 376 - Adicionar orientação abaixo do vídeo mobile

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

- mobile; print da atividade de vídeo fornecido na conversa e `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Objetivo

Adicionar uma orientação curta para a prática abaixo do vídeo e acima da conclusão.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-375.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `styles.ts` | inserir orientação na sequência de vídeo | sim |

## Orçamento de contexto

- baixo
- estratégia: alteração localizada na composição da atividade de vídeo

## Critérios de conclusão

- [x] orientação aparece abaixo do vídeo e antes da conclusão
- [x] não altera os fluxos de áudio e jogo

## Resultado da execucao

- adicionada a orientação `Pratique junto` abaixo do player de vídeo e antes do botão de conclusão
- o bloco usa fundo discreto para orientar sem competir com o vídeo e a ação principal

## Contexto utilizado

- contexto mínimo: índice, esta task, Slice 008 e handoff `TASK-375`
- implementação: `mobile/src/features/trail/screens/TrailActivityScreen.tsx` e `styles.ts`

## Handoff

- `.agents/state/handoffs/TASK-376.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- esta task, slice, índice e handoff

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos

## Pendencias pos-task

- validar o texto de orientação com o conteúdo terapêutico final de cada atividade, caso seja necessária personalização por vídeo

## Status final

done
