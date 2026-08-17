# Handoff - Task 373

## Task

- identificador: 373
- título: Remover criação de relatório CSV e manter apenas PDF
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 011

## Decisões preservadas

- decisão: remover o CSV apenas do fluxo novo de criação
- motivo: atender a regra atual do produto sem quebrar o acesso a relatórios CSV que já possam existir no histórico
- impacto: web e API geram somente PDF; listagem e download continuam aceitando arquivos legados

## Contexto utilizado

- handoff `TASK-372`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/types/report.ts`
- `front-end/src/constants/navigation.ts`
- `backend/src/modules/reports/dto/reports.dto.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `contracts/openapi.yaml`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/reports/services/reportsService.ts`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/types/report.ts`
- `front-end/src/constants/navigation.ts`
- `backend/src/modules/reports/dto/reports.dto.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `contracts/openapi.yaml`
- `tasks/change-requests/373-remover-criacao-de-relatorio-csv-e-manter-apenas-pdf.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-373.md`

## Validações executadas

- `cd backend && npm run test -- reports.service.spec.ts` — passou
- `cd front-end && npm run build` — falhou por erros preexistentes fora do escopo

## Pendências ou bloqueios

- o build do front-end segue quebrado por erros preexistentes em arquivos da biblioteca e do perfil do paciente

## Próxima ação sugerida

- corrigir os erros preexistentes do build web antes de usar `npm run build` como guarda completa para novas mudanças no front-end

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-373.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `backend/src/modules/reports/reports.service.ts`
