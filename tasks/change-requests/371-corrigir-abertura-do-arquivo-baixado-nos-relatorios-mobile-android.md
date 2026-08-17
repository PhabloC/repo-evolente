# Task 371 - Corrigir abertura do arquivo baixado nos relatórios mobile Android

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

- `contracts/openapi.yaml#/paths/~1reports~1{reportId}~1download/get`

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

correção funcional incremental sobre a tela de relatórios do responsável

### Fonte primaria visual

- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/reports/services/reportsService.ts`

## Objetivo

Corrigir a abertura do PDF/CSV baixado na tela de relatórios do responsável quando o Android rejeita a URL local `file:///...`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-370.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Fluxo atual de download | `mobile/src/features/reports/services/reportsService.ts` | ajustar a abertura do arquivo após download | sim |
| Tela consumidora | `mobile/src/features/shell/screens/GuardianReportsScreen.tsx` | confirmar o ponto de uso do download | sim |
| Contrato de download | `contracts/openapi.yaml#/paths/~1reports~1{reportId}~1download/get` | preservar o mesmo endpoint autenticado | sim |

## Orçamento de contexto

- baixo
- estratégia: limitar a mudança ao serviço de relatórios, convertendo o `file://` local em `content://` no Android antes de abrir

## Criterios de conclusao

- [x] arquivos baixados na tela de relatórios usam abertura compatível com Android
- [x] a correção não altera o contrato nem a tela de listagem
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 369 - done
- Task 370 - done

## Resultado da execucao

- o `reportsService` passou a converter o caminho local baixado em `content://...` no Android usando `getContentUriAsync`
- a abertura do arquivo continua usando a mesma chamada de download autenticado e não muda o fluxo da tela

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-370.md`
- `contracts/openapi.yaml#/paths/~1reports~1{reportId}~1download/get`
- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-371.md`

## Arquivos alterados

- `tasks/change-requests/371-corrigir-abertura-do-arquivo-baixado-nos-relatorios-mobile-android.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-371.md`
- `mobile/src/features/reports/services/reportsService.ts`

## Validacoes executadas

- `cd mobile && npm run typecheck` — falhou por erros preexistentes em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` — passou (`27` suítes, `95` testes)

## Pendencias pos-task

- erros preexistentes de typecheck no app mobile seguem fora do escopo desta task
- a abertura final do arquivo ainda depende de existir um app compatível no dispositivo

## Status final

done
