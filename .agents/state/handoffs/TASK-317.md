# Handoff - Task 317

## Task

- identificador: 317
- titulo: Excluir relatórios gerados na tela de relatórios
- tipo: shared
- modo de execucao: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao
- objetivo de negocio: permitir que o profissional remova relatórios gerados sem sair da tela de histórico
- entrega verificavel: a rota `/relatorios` exibe ação de exclusão com confirmação e o backend remove o relatório do profissional com auditoria

## Decisoes preservadas

- a exclusão foi implementada no mesmo recurso `DELETE /reports/{reportId}`, sem criar rota paralela
- apenas o profissional dono do relatório pode excluir; o fluxo reutiliza a mesma linha de autorização já aplicada a baixar e disponibilizar
- a confirmação no front usa `Modal` compartilhado, evitando `window.confirm` e mantendo foco/teclado consistentes

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/317-excluir-relatorios-gerados-na-tela-de-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-316.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | integração cliente-servidor | adicionar `DELETE /reports/{reportId}` |
| `backend/docs/ai/{ARCHITECTURE.md,SECURITY.md}` | ajuste de API protegida | manter fluxo controller/service/repository e autorização segura |
| `backend/src/modules/reports/**` | implementação backend | incluir remoção, persistência e teste |
| `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | impacto em UI | manter confirmação acessível e reuso coerente |
| `front-end/src/services/reports/reportService.ts` | integração web | expor chamada de exclusão |
| `front-end/src/pages/Main/Reports/{index.tsx,styles.module.css}` | implementação web | adicionar ação, modal e feedback |
| `front-end/src/ui/Modal/index.tsx` | confirmação destrutiva | validar reuso do componente compartilhado |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `mobile/` | sem impacto no app nesta fase |
| `next-js/` | stack web ativa é `front-end` |

## Resultado por stack

- backend: endpoint de exclusão, remoção em repositório e auditoria `report.deleted`
- front-end: ação `Excluir` na tabela com modal de confirmação e recarga da lista
- mobile: sem alterações

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

## Validacoes executadas

- `cd backend && npm run test -- --runInBand src/modules/reports/reports.service.spec.ts`: ok
- `cd backend && npm run build`: ok
- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx src/services/reports/reportService.ts`: ok
- `cd front-end && npm run build`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- só evoluir este fluxo se surgir necessidade de exclusão em lote ou trilha de auditoria visível na interface

## Proximo contexto recomendado

- `backend/src/modules/reports/reports.service.ts`
- `front-end/src/pages/Main/Reports/index.tsx`
- `contracts/openapi.yaml`
