# Task 024 - App responsavel: home, perfil e notificacoes

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths` profile/notifications

## Modo de execucao

cross-stack

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`

### Regra de aderencia visual

- Area responsavel calma; notificacoes de trilha.

## Contexto de negocio

### Por que

Completar jornada mobile.

### O que

Home, perfil e notificacoes in-app (push TBD).

### Comportamento esperado

- Home
- Perfil
- Lista notificacoes

### Fora de escopo

- Push definitivo
- Gamificacao

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissoes: responsavel+assinatura
- Casos de erro: sessao; push off
- Decisoes humanas confirmadas: Stack web React/Vite; mobile sim; profissional multi-especialidade; inativar nao excluir; gamificacao fora
- Casos de borda: zero notificacoes

## Especificacao tecnica

### Deve

- API notifications + UI
- Fallback in-app

### Nao deve

- nao adicionar novas dependencias sem autorizacao explicita nesta task
- nao desviar dos padroes estabelecidos sem justificativa registrada
- Hardcode FCM sem decisao

## Entradas

- `requirements/001-escopo-produto.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/docs/ai/`
- `backend/docs/ai/`
- `contracts/openapi.yaml`

## Dependencias

- Tasks 007 e 020

## Slice vertical

### Identificador do slice

Slice 010 - App responsavel

### Arquivo do slice

- `tasks/slices/010-app-responsavel-home-notificacoes.md`

### Objetivo de negócio

Home/perfil/notificacoes.

### Entrega verificável do slice

Experiencia responsavel.

### Fora do slice

- Admin

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI mobile | sim |
| Mobile | `mobile/docs/ai/ARCHITECTURE.md e CODE_STYLE.md` | mobile | sim |
| Backend | `backend/docs/ai/ARCHITECTURE.md e SECURITY.md` | back | sim |
| API | `contracts/openapi.yaml` | API | sim |
| Requisitos | `requirements/001-escopo-produto.md e 002-regras-de-negocio.md` | regras | sim |

## Orçamento de contexto

- Risco medio

## Criterios de conclusao

- Home/perfil
- Notificacoes in-app
- Hook provider

## Instrucoes de implementacao

- Notificar ao atribuir atividade se API permitir

## Validacao esperada

- npm run lint
- npm run typecheck
- npm run test

## Entregaveis esperados

- API+telas

## Riscos ou ambiguidades

- Push TBD

## Resultado da execucao

Cross-stack concluído: API de notificações in-app + perfil do responsável; UI mobile Home/Perfil/Avisos com demo fallback; push via `NoopPushNotificationAdapter` (sem FCM). Evento `trail.items.assigned` gera notificação ao atribuir itens de trilha.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- handoff `TASK-023`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` (guardians/me, notifications, subscriptions/me) | API | contrato |
| `design-system/mobile/Design_System_Evolente_App_Mobile.md` | UI | tom calmo responsável |
| padrões mobile (trail/admin features) | mobile | feature profile/notifications |
| módulo trails/guardians existente | back | emit + perfil |

### Contexto não carregado

- front-end/next-js (não envolvidos)
- design-system/front
- CRUD catálogo / admin

## Handoff

- `.agents/state/handoffs/TASK-024.md`

## Arquivos alterados

### Backend

- `backend/src/modules/notifications/**` (módulo, entity, repos, service, controller, listener, spec)
- `backend/src/patterns/adapters/push-notification.adapter.ts`
- `backend/src/patterns/adapters/noop-push-notification.adapter.ts`
- `backend/src/modules/trails/events/trail.events.ts` + emit em `trails.service.ts`
- `backend/src/modules/guardians/guardians.controller.ts` + `getMyProfile` em service
- `backend/src/modules/users/users.controller.ts` (`GET /users/me`)
- `backend/src/app.module.ts`
- `backend/src/database/migrations/1790000000000-CreateNotificationsTable.ts`
- `contracts/openapi.yaml` (Notifications, `/guardians/me`, `/notifications`)

### Mobile

- `mobile/src/features/profile/**` (types, service, hooks)
- `mobile/src/features/notifications/**` (types, service, hooks)
- `mobile/src/features/shell/screens/ResponsavelHomeScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/ResponsavelNotificationsScreen.tsx`
- `mobile/src/features/shell/screens/styles.ts`
- `mobile/src/features/shell/navigators/ResponsavelShellNavigator.tsx`

### Governança

- esta task, `tasks/000-index.md`, `tasks/slices/010-...`, handoff TASK-024

## Validacoes executadas

- backend: `npm run lint` ok; testes notifications/trails/guardians ok (14)
- mobile: `npm run lint` + `typecheck` + `test` ok (8)

## Aderencia ao design system

- Área responsável calma (bege/tokens existentes); sem medalhas/pontos
- Acessibilidade: labels em avisos, `accessibilityRole`/`Hint` para marcar lida, live region implícita via estados de erro
- Desvio: tipografia Nunito ainda sem pacote de fonte (já documentado no mobile); push nativo TBD

## Pendencias pos-task

- Provedor de push real (FCM/APNs) — decisão humana
- Task 025 conforme prioridade do index

## Status final

done
