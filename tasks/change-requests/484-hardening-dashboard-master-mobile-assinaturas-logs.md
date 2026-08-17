# Task 484 - Hardening do dashboard master mobile para assinaturas e logs

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

- sem mudança de contrato; consumo dos endpoints admin existentes

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/009-administracao-master.md`

## Objetivo

Evitar que o dashboard master mobile mostre métricas enganosas quando `/admin/subscriptions` falhar e limitar a concorrência de `GET /users/:id` na hidratação dos logs administrativos.

## Criterios de aceite

- [x] dashboard explicita indisponibilidade de métricas derivadas de assinaturas quando a query falha
- [x] métricas confiáveis do dashboard continuam visíveis
- [x] enriquecimento de logs limita concorrência de busca de usuários
- [x] testes de regressão cobrem tela e service
- [x] handoff gerado

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/009-administracao-master.md`
- `tasks/change-requests/484-hardening-dashboard-master-mobile-assinaturas-logs.md`
- `.agents/state/handoffs/TASK-023.md`

## Contexto sob demanda

- `mobile/AGENTS.md` e `mobile/docs/ai/AGENTS.md` — governança local
- `mobile/docs/ai/REPO_MAP.md` e `mobile/docs/ai/QA.md` — mapa da stack e validações
- `design-system/mobile/Design_System_Evolente_App_Mobile.md` — manter linguagem operacional calma do módulo master

## Orçamento de contexto

- 8 fontes
- estratégia: focar em `admin/screens`, `admin/services` e hooks já existentes

## Resultado da execucao

O dashboard master mobile agora distingue falha de assinaturas de valor zero real, marca indicadores dependentes como indisponíveis e reduz o pico de requisições simultâneas ao enriquecer logs com usuários.

## Contexto utilizado

- slice 009
- handoff da task 023
- screen/service/hooks do módulo admin mobile

## Handoff

- `.agents/state/handoffs/TASK-484.md`

## Arquivos alterados

- `mobile/src/features/admin/screens/AdminHomeScreen.tsx`
- `mobile/src/features/admin/services/adminService.ts`
- `mobile/src/features/admin/screens/AdminHomeScreen.test.tsx`
- `mobile/src/features/admin/services/adminService.test.ts`
- `tasks/slices/009-administracao-master.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- --runInBand src/features/admin/services/adminService.test.ts src/features/admin/screens/AdminHomeScreen.test.tsx` — PASS

## Pendencias pos-task

- nenhuma

## Status final

done
