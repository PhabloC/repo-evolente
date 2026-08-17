# Task 206 - Tela de atividade sem padding com ações no topo mobile

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

A tela da atividade ainda mantém espaçamentos estruturais e ações de rodapé que afastam o conteúdo da proposta fullscreen desejada para a execução.

### O que

Remover os paddings da tela de atividade, deixar o conteúdo ocupar toda a área útil e consolidar as ações apenas no topo com seta de voltar à esquerda e check de conclusão à direita.

### Comportamento esperado

- sem padding lateral, superior ou inferior na estrutura principal da tela
- conteúdo da atividade ocupa a tela toda
- não existe mais botão `Voltar à lista`
- não existe mais botão textual de concluir no rodapé
- a conclusão da atividade fica no topo direito em um ícone de check

### Fora de escopo

- mudança de contrato
- alteração da navegação global do app
- mudanças no conteúdo pedagógico dos jogos

## Dependencias

- Task 020
- Task 158
- Task 163
- Task 204
- Task 205

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-205.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | manter a experiência fullscreen minimalista da atividade | sim |
| Mobile | `mobile/docs/ai/AGENTS.md`, `CODE_STYLE.md` | seguir padrões locais de composição e ícones | sim |
| Tela de atividade | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `styles.ts` | mover ações para o topo e remover paddings estruturais | sim |
| Runtime do jogo | `mobile/src/features/games/components/AlphabetGameRenderer/styles.ts`, `mobile/src/features/games/components/AlphabetWritingGameRenderer/styles.ts` | preservar o fullscreen dos cards dentro da nova tela | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar o ajuste ao chrome da tela de atividade e aos cards fullscreen usados dentro dela

## Criterios de conclusao

- tela sem paddings estruturais extras
- ações principais concentradas no topo
- sem botão de voltar no rodapé
- sem botão textual de concluir no rodapé
- lint e typecheck mobile passam

## Resultado da execucao

- A tela de atividade passou a usar a área útil inteira, sem padding estrutural no container principal.
- O botão `Voltar à lista` foi removido do rodapé.
- A conclusão da atividade saiu do rodapé e foi consolidada em um ícone de check no topo direito.
- O fluxo de conclusão continua com confirmação explícita, agora usando `Alert` nativo disparado pelo ícone do topo.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 206, slice 008, `TASK-205`
- contexto sob demanda: `design-system/mobile/Design_System_Evolente_App_Mobile.md`; `mobile/docs/ai/AGENTS.md`, `CODE_STYLE.md`; `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `styles.ts`; `mobile/src/features/games/components/AlphabetGameRenderer/styles.ts`; `mobile/src/features/games/components/AlphabetWritingGameRenderer/styles.ts`
- contexto evitado: `contracts/openapi.yaml`, `front-end/`, `backend/`

## Handoff

- `.agents/state/handoffs/TASK-206.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `tasks/change-requests/206-tela-atividade-sem-padding-com-acoes-no-topo-mobile.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-206.md`

## Validacoes executadas

- `cd mobile && npm run lint` — ok com 2 warnings antigos em `src/features/games/utils/alphabetWritingGame.ts`
- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
