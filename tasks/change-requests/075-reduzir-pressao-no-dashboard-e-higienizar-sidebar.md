# Task 075 - Reduzir pressao no dashboard e higienizar sidebar

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao altera contrato; reusa endpoints atuais enquanto nao existir agregado dedicado

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Objetivo

Reduzir o custo operacional do dashboard profissional no cliente e mitigar riscos de isolamento/testes do efeito persistente do sidebar, sem alterar a composicao visual aprovada.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-056.md`
- `.agents/state/handoffs/TASK-070.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Dashboard real | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | manter padroes de hook, service e a11y | sim |
| Implementacao do dashboard | `front-end/src/services/dashboard/getDashboardSummary.ts`, `front-end/src/hooks/useDashboardSummary.ts`, `front-end/src/pages/Main/ShellHome/index.tsx` | limitar concorrencia e corrigir loading inicial | sim |
| Shell compartilhado | `front-end/src/layout/Sidebar/{index.tsx,persistentLava.tsx}` | adicionar limpeza/isolamento seguro do efeito persistente | sim |

## Orçamento de contexto

- medio
- estrategia: manter o escopo no dashboard profissional e no sidebar compartilhado, sem abrir outras telas do shell

## Criterios de conclusao

- [ ] coleta do summary do dashboard deixa de disparar fan-out irrestrito de requisições por paciente
- [ ] hook do dashboard nao pisca estado de loading quando inicializado com `enabled = false`
- [ ] infraestrutura do lava persistente expõe limpeza segura para testes/desmontagem
- [ ] dashboard e sidebar preservam comportamento visual atual
- [ ] validacoes focadas do front-end executadas

## Dependencias

- Task 056 - done
- Task 070 - done

## Resultado da execucao

- o summary do dashboard profissional passou a processar pacientes ativos com limite de concorrencia no cliente, reduzindo o fan-out simultaneo sobre `trails` e `progress`
- o hook `useDashboardSummary` agora inicia `isLoading` de acordo com `enabled`, evitando flash de loading quando o dashboard esta desabilitado para perfis nao profissionais
- a infraestrutura do lava persistente passou a expor `teardownSidebarLava`, permitindo desmontagem e limpeza total em testes ou ciclos de desmontagem controlados
- foram adicionados testes focados para concorrencia, hook de dashboard e limpeza do sidebar persistente

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `.agents/state/handoffs/TASK-056.md`
- `.agents/state/handoffs/TASK-070.md`

### Sob demanda

- `front-end/docs/ai/ARCHITECTURE.md`, `front-end/docs/ai/CODE_STYLE.md`, `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.test.ts`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/layout/Sidebar/index.tsx`
- `front-end/src/layout/Sidebar/persistentLava.tsx`
- `front-end/src/layout/Sidebar/persistentLava.test.tsx`
- `front-end/src/utils/mapWithConcurrency.ts`
- `front-end/src/utils/mapWithConcurrency.test.ts`

## Handoff

- `.agents/state/handoffs/TASK-075.md`

## Arquivos alterados

- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.ts`
- `front-end/src/hooks/useDashboardSummary.test.ts`
- `front-end/src/layout/Sidebar/persistentLava.tsx`
- `front-end/src/layout/Sidebar/persistentLava.test.tsx`
- `front-end/src/utils/mapWithConcurrency.ts`
- `front-end/src/utils/mapWithConcurrency.test.ts`
- `tasks/change-requests/075-reduzir-pressao-no-dashboard-e-higienizar-sidebar.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-075.md`

## Validacoes executadas

- `cd front-end && npm run test -- src/utils/mapWithConcurrency.test.ts src/hooks/useDashboardSummary.test.ts src/layout/Sidebar/persistentLava.test.tsx src/pages/Main/ShellHome/index.test.tsx` - ok
- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
