# Task 205 - Refino fullscreen e confirmação na atividade mobile

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

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 008 - Trilhas semanais e evolucao

### Arquivo do slice

- `tasks/slices/008-trilhas-semanais-evolucao.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

## Contexto de negocio

### Por que

Mesmo após a abertura imersiva da atividade, a experiência ainda precisa de ajustes de usabilidade: parte do conteúdo do jogo pode ficar cortada, a superfície não está suficientemente fullscreen e a conclusão precisa de confirmação explícita.

### O que

Refinar a tela de atividade do app mobile para ter scroll funcional no conteúdo, topo fullscreen sem borda arredondada, seta de voltar no canto superior esquerdo e uma confirmação visual antes de concluir a atividade.

### Comportamento esperado

- a tela da atividade permite scroll vertical quando o conteúdo exceder a altura disponível
- a superfície superior da atividade ocupa a largura inteira, sem borda arredondada no topo
- existe um botão com seta no topo esquerdo para voltar à tela anterior
- concluir atividade exige uma confirmação explícita na própria tela
- a confirmação de conclusão usa ícone de check

### Fora de escopo

- mudança de contrato
- alteração do conteúdo pedagógico dos jogos
- reestruturação da navegação global do app

## Dependencias

- Task 020
- Task 158
- Task 163
- Task 204

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-204.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | preservar a leitura fullscreen da atividade com confirmação clara | sim |
| Mobile | `mobile/docs/ai/AGENTS.md`, `CODE_STYLE.md` | manter padrão local do app | sim |
| Tela de atividade | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `styles.ts` | refino da superfície fullscreen e ações | sim |
| Runtime do jogo | `mobile/src/features/games/renderers/GameActivityRenderer.tsx`, `mobile/src/features/games/components/AlphabetGameRenderer/*`, `mobile/src/features/games/components/AlphabetWritingGameRenderer/*` | garantir scroll e leitura completa dos conteúdos interativos | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a mudança à tela de atividade e aos renderers usados dentro dela

## Criterios de conclusao

- atividade pode ser rolada sem cortar conteúdo inferior
- topo da tela fica fullscreen com ação clara de voltar
- existe confirmação explícita antes de concluir
- lint e typecheck mobile passam

## Resultado da execucao

- `TrailActivityScreen` passou a renderizar uma barra superior dedicada com seta de voltar no canto esquerdo.
- O conteúdo da atividade agora roda em `ScrollView` com container preparado para permitir rolagem vertical sem cortar a parte inferior do jogo.
- A ação de concluir atividade virou um fluxo em dois passos, com card de confirmação na própria tela e ícone de check no CTA de confirmar.
- Os cards do modo de atividade ficaram alinhados ao fullscreen, sem borda arredondada no topo da superfície principal.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 205, slice 008, `TASK-204`
- contexto sob demanda: `design-system/mobile/Design_System_Evolente_App_Mobile.md`; `mobile/docs/ai/AGENTS.md`, `CODE_STYLE.md`; `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `styles.ts`; `mobile/src/features/games/renderers/GameActivityRenderer.tsx`; `mobile/src/features/games/components/AlphabetGameRenderer/*`; `mobile/src/features/games/components/AlphabetWritingGameRenderer/*`; `mobile/src/shared/components/Button/index.tsx`; `mobile/src/shared/components/Screen/index.tsx`
- contexto evitado: `contracts/openapi.yaml`, `front-end/`, `backend/`

## Handoff

- `.agents/state/handoffs/TASK-205.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/games/components/AlphabetGameRenderer/styles.ts`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/styles.ts`
- `tasks/change-requests/205-refino-fullscreen-e-confirmacao-na-atividade-mobile.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-205.md`

## Validacoes executadas

- `cd mobile && npm run lint` — ok com 2 warnings antigos em `src/features/games/utils/alphabetWritingGame.ts`
- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
