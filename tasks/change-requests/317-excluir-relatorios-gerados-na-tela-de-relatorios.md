# Task 317 - Excluir relatórios gerados na tela de relatórios

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1reports~1{reportId}`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- design system + padrão visual atual da rota de relatórios

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- `front-end/src/pages/Main/Reports/**`
- `front-end/src/ui/Modal/**`
- `front-end/src/ui/Button/**`

### Lacunas

- sem print novo; a exclusão deve seguir a linguagem atual de tabela e confirmação destrutiva já usada em outros fluxos

## Objetivo

Permitir que o profissional exclua relatórios já gerados diretamente da tela `/relatorios`, com confirmação explícita, atualização imediata da lista e endpoint dedicado no backend.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-316.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Contrato de API | `contracts/openapi.yaml` | adicionar exclusão em `/reports/{reportId}` | sim |
| Docs backend | `backend/docs/ai/{ARCHITECTURE.md,SECURITY.md}` | manter fluxo controller/service/repository e autorização segura | sim |
| Módulo reports backend | `backend/src/modules/reports/**` | implementar exclusão e cobertura de teste | sim |
| Docs front-end | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | aplicar confirmação acessível e reuso coerente | sim |
| UI relatórios | `front-end/src/pages/Main/Reports/**` | incluir ação de excluir e feedback de sucesso/erro | sim |
| Primitivas UI | `front-end/src/ui/{Button,Modal}/**` | reutilizar componentes existentes | sim |

## Orçamento de contexto

- medio
- estrategia: limitar a mudança ao módulo `reports`, contrato correspondente e à rota web `/relatorios`

## Criterios de conclusao

- [x] existe endpoint autenticado para excluir relatório próprio do profissional
- [x] a tela `/relatorios` permite excluir um relatório com confirmação explícita
- [x] a lista é atualizada após exclusão sem regressão nas ações de baixar e disponibilizar

## Dependencias

- Task 316 - done

## Resultado da execucao

- o contrato passou a expor `DELETE /reports/{reportId}` para exclusão de relatório pelo profissional dono
- o backend ganhou fluxo seguro de exclusão com autorização, remoção em repositório e auditoria `report.deleted`
- a tela `/relatorios` passou a exibir ação `Excluir` com modal de confirmação destrutiva, feedback acessível e refresh imediato da tabela

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-316.md`

### Sob demanda

- `contracts/openapi.yaml`
- `backend/docs/ai/ARCHITECTURE.md`
- `backend/docs/ai/SECURITY.md`
- `backend/src/modules/reports/reports.controller.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.repository.ts`
- `backend/src/modules/reports/reports.typeorm.repository.ts`
- `backend/src/modules/reports/reports.in-memory.repository.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/services/reports/reportService.ts`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `front-end/src/ui/Modal/index.tsx`
- `front-end/src/ui/Button/index.tsx`

### Contexto evitado

- `mobile/`, porque o ajuste não afeta o app nesta fase
- `next-js/`, porque a stack web ativa é `front-end`

## Handoff

- `.agents/state/handoffs/TASK-317.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/reports/reports.controller.ts`
- `backend/src/modules/reports/reports.service.ts`
- `backend/src/modules/reports/reports.repository.ts`
- `backend/src/modules/reports/reports.typeorm.repository.ts`
- `backend/src/modules/reports/reports.in-memory.repository.ts`
- `backend/src/modules/reports/reports.service.spec.ts`
- `front-end/src/services/reports/reportService.ts`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/317-excluir-relatorios-gerados-na-tela-de-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-317.md`

## Validacoes executadas

- `cd backend && npm run test -- --runInBand src/modules/reports/reports.service.spec.ts`
- `cd backend && npm run build`
- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx src/services/reports/reportService.ts`
- `cd front-end && npm run build`

## Pendencias pos-task

- nenhuma

## Status final

done
