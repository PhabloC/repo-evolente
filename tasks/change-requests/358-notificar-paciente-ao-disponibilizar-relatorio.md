# Task 358 - Notificar paciente ao disponibilizar relatório

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1reports~1{reportId}~1share/patch`
- `contracts/openapi.yaml#/paths/~1notifications/get`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Backend

- não se aplica

### Mobile

- reutilizar a central de avisos já entregue em `Slice 010`

## Objetivo

Quando o profissional disponibilizar um relatório ao responsável, o paciente/responsável deve receber uma notificação na central de avisos do app mobile.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-357.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Share de relatório | `backend/src/modules/reports/reports.service.ts` e `reports.module.ts` | ligar emissão da notificação no fluxo de disponibilização | sim |
| Domínio de notificações | `backend/src/modules/notifications/**` | criar novo tipo de aviso | sim |
| Contrato | `contracts/openapi.yaml#/paths/~1reports`, `#/paths/~1notifications`, `#/components/schemas/PublicNotification` | refletir o novo tipo `report_shared` | sim |
| Tipos mobile | `mobile/src/features/notifications/types/notification.ts` | aceitar o novo tipo sem quebra | sim |
| Qualidade backend/mobile | `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/SECURITY.md`, `mobile/docs/ai/ARCHITECTURE.md` | manter fronteiras e baixo acoplamento | sim |

## Orçamento de contexto

- baixo
- estratégia: limitar a mudança ao evento de share e ao contrato/tipos de notificações, sem reabrir viewer/download de relatório nem redesign da tela de avisos

## Criterios de conclusao

- [x] disponibilizar relatório gera notificação ao responsável
- [x] notificação usa a central existente de `/notifications`
- [x] contrato OpenAPI expõe o novo tipo de notificação
- [x] mobile aceita o novo tipo sem regressão
- [x] share repetido do mesmo relatório não duplica notificação

## Dependencias

- Task 323 - done
- Task 357 - done

## Resultado da execucao

- o backend passou a emitir uma notificação `report_shared` quando um relatório é disponibilizado pela primeira vez ao responsável
- o fluxo de share continua auditado e agora alimenta a central já existente de avisos do app
- o contrato e os tipos mobile foram atualizados para reconhecer o novo tipo de notificação

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/011-relatorios-evolucao.md`
- handoff `TASK-357`
- `backend/docs/ai/ARCHITECTURE.md`, `backend/docs/ai/SECURITY.md`
- `mobile/docs/ai/ARCHITECTURE.md`
- `contracts/openapi.yaml`
- `backend/src/modules/reports/**`
- `backend/src/modules/notifications/**`
- `mobile/src/features/notifications/types/notification.ts`

## Handoff

- `.agents/state/handoffs/TASK-358.md`

## Arquivos alterados

- `tasks/change-requests/358-notificar-paciente-ao-disponibilizar-relatorio.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-358.md`
- `contracts/openapi.yaml`
- `backend/src/modules/notifications/entities/notification.entity.ts`
- `backend/src/modules/notifications/notifications.service.ts`
- `backend/src/modules/notifications/notifications.service.spec.ts`
- `backend/src/modules/reports/reports.module.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `mobile/src/features/notifications/types/notification.ts`

## Validacoes executadas

- `cd backend && npm run test -- --runInBand src/modules/notifications/notifications.service.spec.ts src/modules/reports/reports.service.spec.ts`

## Pendencias pos-task

- push nativo real continua fora de escopo; a entrega cobre a notificação in-app via central de avisos

## Status final

done
