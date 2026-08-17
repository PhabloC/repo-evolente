# Task 207 - Rota real para execução de atividade mobile

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

A execução da atividade ainda estava acoplada ao estado interno da aba da trilha, simulando uma página dedicada sem realmente existir como rota de navegação.

### O que

Criar uma rota real no stack navigator do app mobile para a execução de atividade do responsável.

### Comportamento esperado

- tocar em abrir atividade navega para uma screen real da stack
- a tela da atividade deixa de depender de estado local dentro do shell
- voltar da atividade retorna para a aba da trilha já aberta
- a tab bar continua fora da tela de atividade porque a screen fica acima do shell

### Fora de escopo

- mudança de contrato
- alteração do conteúdo dos jogos
- mudança visual adicional fora da navegação

## Dependencias

- Task 020
- Task 158
- Task 204
- Task 205
- Task 206

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-206.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Navegação mobile | `mobile/src/routes/RootNavigator.tsx`, `mobile/src/routes/params.ts`, `mobile/src/config/linking.ts` | criar a rota dedicada e tipar os parâmetros | sim |
| Shell responsável | `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx` | remover a pseudo-página interna da aba | sim |
| Tela de atividade | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `TrailTodayScreen.tsx` | conectar a screen real à abertura e ao retorno | sim |
| Mobile | `mobile/docs/ai/AGENTS.md` | seguir o padrão arquitetural local | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: limitar a mudança ao eixo de rotas da área do responsável e à screen de atividade

## Criterios de conclusao

- existe uma screen real para `TrailActivity`
- `ResponsavelShellNavigator` não renderiza mais a atividade inline
- a abertura da atividade navega pela stack
- lint e typecheck mobile passam

## Resultado da execucao

- `RootNavigator` passou a registrar a screen `TrailActivity` como rota real da stack do responsável.
- `RootStackParamList` passou a tipar os parâmetros da atividade aberta.
- `ResponsavelShellNavigator` deixou de controlar `selectedActivity` e agora apenas navega para a rota da atividade.
- `TrailActivityScreen` passou a ler `activity` via `route.params` e a voltar com `navigation.goBack()`.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 207, slice 008, `TASK-206`
- contexto sob demanda: `mobile/src/routes/RootNavigator.tsx`, `mobile/src/routes/params.ts`, `mobile/src/config/linking.ts`; `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`; `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `TrailTodayScreen.tsx`; `mobile/docs/ai/AGENTS.md`
- contexto evitado: `contracts/openapi.yaml`, `front-end/`, `backend/`

## Handoff

- `.agents/state/handoffs/TASK-207.md`

## Arquivos alterados

- `mobile/src/routes/params.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `tasks/change-requests/207-rota-real-para-execucao-de-atividade-mobile.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-207.md`

## Validacoes executadas

- `cd mobile && npm run lint` — ok com 2 warnings antigos em `src/features/games/utils/alphabetWritingGame.ts`
- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
