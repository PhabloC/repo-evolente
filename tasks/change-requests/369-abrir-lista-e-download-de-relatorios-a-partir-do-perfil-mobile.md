# Task 369 - Abrir lista e download de relatórios a partir do perfil mobile

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

- `contracts/openapi.yaml#/paths/~1reports/get`
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

refino incremental sobre a área do responsável e o card de relatórios já existente

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/components/HomeActionCard`

## Objetivo

Fazer o card de relatórios do perfil abrir uma página com os relatórios disponíveis ao responsável e permitir o download autenticado desses arquivos.

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
| Fluxo anterior do card | `tasks/change-requests/357-adicionar-card-de-relatorios-no-perfil-mobile.md` | estender a entrega do card sem reabrir escopo desnecessário | sim |
| Arquitetura mobile | `mobile/docs/ai/ARCHITECTURE.md` e `mobile/docs/ai/CODE_STYLE.md` | manter separação entre screen, hook e service | sim |
| Contrato de relatórios | `contracts/openapi.yaml#/paths/~1reports/get`, `#/paths/~1reports~1{reportId}~1download/get` e `#/components/schemas/EvolutionReport` | listar relatórios e baixar arquivo autenticado | sim |
| Perfil e navegação atuais | `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`, `mobile/src/routes/RootNavigator.tsx` e `mobile/src/routes/params.ts` | ligar o card à nova tela do stack | sim |
| Domínio de relatórios | `mobile/src/features/reports/hooks/useGuardianReports.ts`, `mobile/src/features/reports/services/reportsService.ts`, `mobile/src/features/reports/types/report.ts` | reaproveitar a listagem e adicionar download | sim |

## Orçamento de contexto

- baixo
- estratégia: limitar a mudança ao fluxo mobile do responsável, reaproveitando a query já existente de `/reports` e adicionando apenas a rota/tela e o download autenticado

## Criterios de conclusao

- [x] tocar no card de relatórios do perfil abre a tela de relatórios
- [x] a nova tela lista apenas relatórios disponíveis ao responsável
- [x] cada relatório permite baixar o arquivo pelo endpoint autenticado
- [x] `npm run lint` executado
- [x] `npm run typecheck` executado
- [x] `npm run test` executado

## Dependencias

- Task 357 - done
- Task 358 - done

## Resultado da execucao

- o card de relatórios no perfil do responsável passou a navegar para uma tela dedicada de relatórios
- a nova tela lista os relatórios compartilhados e expõe um botão explícito de download por item
- o download passou a usar o endpoint autenticado `/reports/{reportId}/download`, salvando o arquivo no dispositivo e tentando abri-lo logo em seguida

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-357.md`
- `tasks/change-requests/357-adicionar-card-de-relatorios-no-perfil-mobile.md`
- `mobile/docs/ai/ARCHITECTURE.md`, `mobile/docs/ai/CODE_STYLE.md`
- `contracts/openapi.yaml#/paths/~1reports/get`
- `contracts/openapi.yaml#/paths/~1reports~1{reportId}~1download/get`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/reports/hooks/useGuardianReports.ts`
- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/features/reports/types/report.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/routes/params.ts`

## Handoff

- `.agents/state/handoffs/TASK-369.md`

## Arquivos alterados

- `tasks/change-requests/369-abrir-lista-e-download-de-relatorios-a-partir-do-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-369.md`
- `mobile/src/features/reports/types/report.ts`
- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/features/reports/hooks/useGuardianReports.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `mobile/src/features/shell/screens/GuardianReportsScreen.tsx`
- `mobile/src/features/shell/screens/guardianReportsStyles.ts`
- `mobile/src/routes/RootNavigator.tsx`
- `mobile/src/routes/params.ts`

## Validacoes executadas

- `cd mobile && npm run lint` — falhou por erros preexistentes em `WordSearchGameRenderer`, `EditChildProfileScreen`, `EditGuardianProfileScreen`, `HomeHeader`, `AppBackgroundBubbles` e `Screen`
- `cd mobile && npm run typecheck` — falhou por erros preexistentes em `MemoryGameRenderer` e `TrailActivityScreen`
- `cd mobile && npm run test` — passou (`27` suítes, `95` testes)

## Pendencias pos-task

- erros preexistentes de lint e typecheck no app mobile seguem fora do escopo desta task
- a abertura do arquivo baixado depende do app/suporte do dispositivo ao tipo de arquivo retornado

## Status final

done
