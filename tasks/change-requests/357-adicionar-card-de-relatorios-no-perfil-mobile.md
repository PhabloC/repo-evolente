# Task 357 - Adicionar card de relatórios no perfil mobile

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

## Modo de execucao

single-stack

## Slice vertical

- Slice 010 - App do responsavel: home, perfil e notificacoes
- `tasks/slices/010-app-responsavel-home-notificacoes.md`

## Referencia visual

### Stack de referencia visual

mobile

### Tipo de referencia visual

refino incremental sobre os cards existentes do perfil

### Fonte primaria visual

- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `mobile/src/features/shell/components/HomeActionCard`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Objetivo

Adicionar na página de perfil do responsável um card de relatórios que represente os relatórios que o profissional gera e disponibiliza ao paciente/responsável.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-287.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI perfil mobile | `mobile/docs/ai/ARCHITECTURE.md` e `mobile/docs/ai/CODE_STYLE.md` | implementar a tela | sim |
| Referência visual mobile | `design-system/mobile/Design_System_Evolente_App_Mobile.md` | manter área do responsável calma e previsível | sim |
| Contrato de relatórios | `contracts/openapi.yaml#/paths/~1reports/get` e `#/components/schemas/EvolutionReport` | consumir listagem já compartilhada ao responsável | sim |
| Perfil atual | `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx` e `mobile/src/features/profile/services/profileService.ts` | encaixar o card no fluxo existente | sim |

## Orçamento de contexto

- baixo
- estratégia: limitar a mudança ao perfil mobile e a um reader de relatórios já previstos no contrato, sem abrir viewer/download

## Criterios de conclusao

- [x] perfil mobile exibe card de relatórios
- [x] card deixa claro que os relatórios vêm do profissional
- [x] card usa dados reais de `/reports` quando disponíveis
- [x] card mantém fallback seguro em demo e sem viewer/download nesta entrega

## Dependencias

- Task 287 - done
- Task 314 - done

## Resultado da execucao

- o perfil mobile passou a exibir um card de relatórios compartilhados pelo profissional ao responsável
- a leitura usa `GET /reports`, respeitando o contrato já existente para o papel de responsável
- o card resume quantidade, último envio e período mais recente sem abrir escopo para viewer ou download autenticado

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/010-app-responsavel-home-notificacoes.md`
- handoff `TASK-287`
- `mobile/docs/ai/ARCHITECTURE.md`, `mobile/docs/ai/CODE_STYLE.md`
- `design-system/mobile/Design_System_Evolente_App_Mobile.md`
- `contracts/openapi.yaml#/paths/~1reports/get`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Handoff

- `.agents/state/handoffs/TASK-357.md`

## Arquivos alterados

- `tasks/change-requests/357-adicionar-card-de-relatorios-no-perfil-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/010-app-responsavel-home-notificacoes.md`
- `.agents/state/handoffs/TASK-357.md`
- `mobile/src/features/reports/types/report.ts`
- `mobile/src/features/reports/services/reportsService.ts`
- `mobile/src/features/reports/hooks/useGuardianReports.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`

## Validacoes executadas

- `cd mobile && npm run lint`
- `cd mobile && npm run typecheck`

## Pendencias pos-task

- viewer/download autenticado de relatório no mobile continua fora de escopo

## Status final

done
