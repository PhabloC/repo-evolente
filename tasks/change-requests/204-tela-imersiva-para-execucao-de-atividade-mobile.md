# Task 204 - Tela imersiva para execução de atividade no mobile

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

Ao abrir uma atividade no app do responsável, a tela atual ainda mostra título, cabeçalho e chrome adicional acima da atividade, atrapalhando a execução.

### O que

Abrir a atividade em uma tela mobile imersiva, removendo o header superior da atividade e ocultando a tab bar enquanto a atividade estiver aberta.

### Comportamento esperado

- tocar em `Abrir atividade` leva para uma superfície dedicada
- a atividade aparece sem `ScreenHeader` e sem hero superior
- a tab bar do shell do responsável some enquanto a atividade está aberta
- a navegação de volta continua funcionando

### Fora de escopo

- mudança de contrato
- refino visual dos renderers internos de cada jogo
- alteração do fluxo web

## Dependencias

- Task 020
- Task 163

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `.agents/state/handoffs/TASK-020.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | preservar a leitura da atividade sem chrome extra | sim |
| Mobile | `mobile/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | organização local da mudança | sim |
| Execução da trilha | `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `TrailTodayScreen.tsx`, `styles.ts` | refino da superfície da atividade | sim |
| Shell responsável | `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`, `styles.ts` | ocultar tab bar durante atividade | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: restringir a mudança à abertura e renderização da atividade no mobile

## Criterios de conclusao

- atividade abre sem cabeçalho/título extras
- tab bar não aparece com a atividade aberta
- fluxo de voltar para a lista continua funcionando
- lint e typecheck mobile passam

## Resultado da execucao

- `TrailActivityScreen` virou uma superfície mais imersiva, sem `ScreenHeader`, sem hero e sem cards informativos redundantes no topo.
- `ResponsavelShellNavigator` passou a esconder a tab bar enquanto existe uma atividade selecionada.
- A tela preserva renderer da atividade, feedback e ações finais de concluir/voltar.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 204, slice 008, `TASK-020`
- contexto sob demanda: `design-system/mobile/Design_System_Evolente_App_Mobile.md`; `mobile/docs/ai/AGENTS.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`; `mobile/src/features/trail/screens/TrailActivityScreen.tsx`, `TrailTodayScreen.tsx`, `styles.ts`; `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`, `styles.ts`
- contexto evitado: `contracts/openapi.yaml`, `front-end/`, `backend/`

## Handoff

- `.agents/state/handoffs/TASK-204.md`

## Arquivos alterados

- `mobile/src/features/trail/screens/TrailActivityScreen.tsx`
- `mobile/src/features/trail/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `mobile/src/features/shell/navigators/styles.ts`
- `tasks/change-requests/204-tela-imersiva-para-execucao-de-atividade-mobile.md`
- `tasks/slices/008-trilhas-semanais-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-204.md`

## Validacoes executadas

- `cd mobile && npm run lint` — ok
- `cd mobile && npm run typecheck` — ok

## Pendencias pos-task

- nenhuma

## Status final

done
