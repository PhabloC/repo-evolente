# Handoff - Task 357

## Task

- identificador: 357
- título: Adicionar card de relatórios no perfil mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 010

## Decisões preservadas

- decisão: limitar a entrega a um card-resumo no perfil do responsável
- motivo: o contrato já cobre `GET /reports`, mas o app ainda não tem fluxo de viewer/download autenticado sem ampliar o escopo
- impacto: o responsável vê os relatórios compartilhados pelo profissional sem abrir arquivo nesta task

- decisão: reutilizar o padrão visual de `HomeActionCard`
- motivo: manter consistência com os cards recentes do perfil mobile

## Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/change-requests/357-adicionar-card-de-relatorios-no-perfil-mobile.md`
- `.agents/state/handoffs/TASK-287.md`

## Contexto sob demanda carregado

- `mobile/docs/ai/ARCHITECTURE.md`
- `mobile/docs/ai/CODE_STYLE.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `contracts/openapi.yaml#/paths/~1reports/get`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Arquivos alterados

- `mobile/src/features/reports/types/report.ts`
- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/features/reports/hooks/useGuardianReports.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/357-adicionar-card-de-relatorios-no-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-357.md`

## Validações executadas

- `cd mobile && npm run lint`
- `cd mobile && npm run typecheck`

## Pendências

- viewer/download de relatório no mobile

## Próxima ação sugerida

- se o usuário quiser avançar o fluxo, abrir uma task dedicada para listar/visualizar relatórios em tela própria

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-357.md`
- `mobile/src/features/reports/**`
- `contracts/openapi.yaml#/paths/~1reports`

## Contexto que não deve ser carregado

- `front-end/`
- `backend/` inteiro
- design system web
