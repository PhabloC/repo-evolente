# Handoff - Task 358

## Task

- identificador: 358
- título: Notificar paciente ao disponibilizar relatório
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 011

## Decisões preservadas

- decisão: gerar notificação apenas na primeira disponibilização do relatório
- motivo: evitar duplicidade se o profissional repetir a ação de share em um relatório já liberado
- impacto: `sharedAt` continua atualizando pelo fluxo atual, mas o aviso in-app não se repete

- decisão: reutilizar a central existente de `/notifications`
- motivo: o app já renderiza título/corpo genericamente, então bastou incluir o novo tipo no contrato/tipos

## Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/change-requests/358-notificar-paciente-ao-disponibilizar-relatorio.md`
- `.agents/state/handoffs/TASK-357.md`

## Contexto sob demanda carregado

- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/SECURITY.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `contracts/openapi.yaml`
- `backend/src/modules/reports/**`
- `backend/src/modules/notifications/**`
- `mobile/src/features/notifications/types/notification.ts`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/notifications/entities/notification.entity.ts`
- `backend/src/modules/notifications/notifications.service.ts`
- `backend/src/modules/notifications/notifications.service.spec.ts`
- `backend/src/modules/reports/reports.module.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `mobile/src/features/notifications/types/notification.ts`
- `tasks/change-requests/358-notificar-paciente-ao-disponibilizar-relatorio.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-358.md`

## Validações executadas

- `cd backend && npm run test -- --runInBand src/modules/notifications/notifications.service.spec.ts src/modules/reports/reports.service.spec.ts`

## Pendências

- push nativo real fora de escopo

## Próxima ação sugerida

- se o usuário quiser aprofundar o fluxo, abrir task dedicada para CTA/contexto específico de relatório dentro da tela de avisos

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-358.md`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/notifications/notifications.service.ts`

## Contexto que não deve ser carregado

- `front-end/`
- viewer/download mobile de relatórios
- design system web
