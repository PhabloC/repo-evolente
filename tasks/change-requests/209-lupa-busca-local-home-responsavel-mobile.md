# Task 209 - Lupa da home: busca local de atividades e avisos

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

nao se aplica (busca client-side sobre dados já carregados; sem endpoint de search)

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 010 - App do responsavel: home, perfil e notificacoes

### Arquivo do slice

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system + pedido explícito

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- pedido: ícone de lupa do header precisa funcionar

## Contexto de negocio

### Por que

A lupa do header da home está visualmente presente (Task 208) mas sem fluxo de busca.

### O que

Abrir busca local ao tocar na lupa, filtrando atividades da trilha do dia e avisos.

### Comportamento esperado

- tocar na lupa abre modal/tela de busca
- filtrar localmente atividades (`useTodayTrailQuery`) e avisos (`useNotificationsQuery`)
- tocar em atividade abre a execução (`TrailActivity`)
- tocar em aviso vai para a aba de avisos
- estados: digite para buscar, sem resultados, carregando

### Fora de escopo

- endpoint de search no backend
- busca no catálogo completo de conteúdos
- nova aba na tab bar

## Dependencias

- Task 208

## Contexto minimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-208.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Header / home | `HomeHeader`, `ResponsavelHomeScreen` | wire `onOpenSearch` | sim |
| Shell | `ResponsavelShellNavigator` | navegar para atividade/avisos | sim |
| Dados | hooks trail + notifications | filtrar resultados | sim |

## Orcamento de contexto

- Risco baixo
- Estrategia: modal local + filtro client-side; sem contrato novo

## Criterios de conclusao

- lupa abre busca funcional
- resultados de atividades e avisos com navegação
- typecheck mobile ok

## Resultado da execucao

- Modal `ResponsavelSearchModal` abre ao tocar na lupa.
- Filtro local cobre atividades da trilha do dia e avisos (sem endpoint novo).
- Toque em atividade navega para `TrailActivity`; toque em aviso abre a aba Avisos.

## Contexto utilizado

- contexto mínimo: task 209, slice 010, handoff 208, índice
- contexto sob demanda: home, shell, hooks trail/notifications
- contexto evitado: backend, front-end, OpenAPI search

## Handoff

- `.agents/state/handoffs/TASK-209.md`

## Arquivos alterados

- `mobile/src/features/shell/utils/filterResponsavelSearch.ts`
- `mobile/src/features/shell/utils/filterResponsavelSearch.test.ts`
- `mobile/src/features/shell/components/ResponsavelSearchModal/index.tsx`
- `mobile/src/features/shell/components/ResponsavelSearchModal/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`
- `tasks/change-requests/209-lupa-busca-local-home-responsavel-mobile.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-209.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm test -- --testPathPattern=filterResponsavelSearch` — ok (4 testes)

## Pendencias pos-task

- nenhuma

## Status final

done
