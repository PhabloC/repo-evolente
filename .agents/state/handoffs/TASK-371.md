# Handoff - Task 371

## Task

- identificador: 371
- título: Corrigir abertura do arquivo baixado nos relatórios mobile Android
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: 011

## Decisões preservadas

- decisão: manter o download autenticado no mesmo `reportsService`
- motivo: a falha estava apenas na abertura do arquivo local no Android
- impacto: a correção ficou concentrada em converter `file://` para `content://` antes de abrir

## Contexto utilizado

- handoff `TASK-370`
- `contracts/openapi.yaml#/paths/~1reports~1{reportId}~1download/get`
- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`

## Arquivos alterados

- `mobile/src/features/reports/services/reportsService.ts`
- `tasks/change-requests/371-corrigir-abertura-do-arquivo-baixado-nos-relatorios-mobile-android.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-371.md`

## Validações executadas

- `cd mobile && npm run typecheck` — falhou por erros preexistentes fora do escopo
- `cd mobile && npm run test` — passou (`27` suítes, `95` testes)

## Pendências ou bloqueios

- erros preexistentes de typecheck no mobile continuam abertos
- a abertura do arquivo depende de um app compatível no dispositivo

## Próxima ação sugerida

- se o erro persistir em algum aparelho específico, inspecionar o MIME e o handler instalado nesse Android

## Próximo contexto recomendado

- `.agents/state/handoffs/TASK-371.md`
- `mobile/src/features/reports/services/reportsService.ts`
