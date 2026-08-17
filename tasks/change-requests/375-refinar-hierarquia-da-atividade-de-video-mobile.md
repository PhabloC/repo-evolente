# Task 375 - Refinar hierarquia da atividade de vídeo mobile

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

### Stack de referência visual

mobile

### Tipo de referência visual

print de tela fornecido pelo usuário e design system

### Fonte primária visual

- print da atividade de vídeo fornecido na conversa em 2026-07-30
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Objetivo

Reduzir o vazio visual da atividade de vídeo e tornar clara a progressão entre assistir, concluir e receber o feedback.

## Comportamento esperado

- topo e informações do vídeo usam menos espaço vertical
- player recebe acabamento visual discreto e mantém os controles nativos
- ação `Concluir atividade` fica visível abaixo do vídeo enquanto pendente
- após concluir, o mesmo espaço apresenta feedback de sucesso
- check do topo continua como atalho para a confirmação já existente

## Fora de escopo

- alterar a mídia, o player ou a API de progresso
- modificar telas de áudio e jogos

## Dependências

- Task 374 - done

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-374.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | composição e feedback da atividade | sim |
| Implementação | `mobile/docs/ai/CODE_STYLE.md`, `COMPONENT_REUSE.md` | padrões locais | sim |
| Tela alvo | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `styles.ts`, `components/TrailVideoPlayer.tsx` | refino visual e ação explícita | sim |

## Orçamento de contexto

- baixo
- estratégia: limitar a alteração à tela e ao player de vídeo, sem alterar o contrato de progresso

## Critérios de conclusão

- [x] ação de conclusão fica explícita para vídeos pendentes
- [x] feedback substitui a ação após a conclusão
- [x] composição usa o espaço vertical de forma equilibrada
- [x] validação mobile executada

## Resultado da execucao

- reduziu-se a altura visual do topo e o espaçamento anterior ao player
- informações de título, tipo e objetivo foram compactadas acima do vídeo
- o botão primário `Concluir atividade` foi colocado abaixo do player para vídeos pendentes, reutilizando a confirmação existente
- após a conclusão, o botão cede lugar a um estado visual de sucesso; o mesmo estado também é apresentado ao reabrir uma atividade já concluída
- o check no topo foi preservado como atalho de conclusão

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, índice, esta task, Slice 008 e handoff `TASK-374`
- design mobile: `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- implementação: `mobile/docs/ai/CODE_STYLE.md`, `COMPONENT_REUSE.md`, `TrailActivityScreen.tsx`, `styles.ts` e `TrailVideoPlayer.tsx`

## Handoff

- `.agents/state/handoffs/TASK-375.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- esta task, `tasks/slices/008-trilhas-semanais-evolucao.md`, `tasks/000-index.md`
- `.agents/state/handoffs/TASK-375.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — executado sem diagnósticos
- `cd mobile && npm run test` — executado sem falhas reportadas pelo comando

## Pendencias pos-task

- validar visualmente em um dispositivo real com vídeo disponível

## Status final

done
