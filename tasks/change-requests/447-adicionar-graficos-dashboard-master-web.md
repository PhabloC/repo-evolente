# Task 447 - Adicionar gráficos ao dashboard master web

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

- reutilizar `GET /admin/metrics`, `GET /admin/subscriptions`, `GET /admin/professionals-tree`, `GET /contents` — sem novos endpoints

## Modo de execucao

single-stack

## Slice vertical

- Slice 009 - Administracao master
- `tasks/slices/009-administracao-master.md`

## Referencia visual

- padrao recharts do dashboard profissional (`ShellHome`)
- linguagem visual atual do Admin

## Objetivo

Incluir no dashboard master graficos operacionais alinhados ao perfil: metricas da plataforma, assinaturas por status e por publico, carteira de pacientes por profissional e biblioteca por area.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, esta task, slice 009

## Contexto sob demanda

| Gatilho | Fonte | Obrigatório? |
|---|---|---|
| UI Admin | `front-end/src/pages/Main/Admin/` | sim |
| APIs | `adminService`, `contentService` | sim |
| Charts | recharts + ShellHome components | sim |
| A11y | `ACCESSIBILITY.md` | sim |

## Orçamento de contexto

- medio
- estrategia: agregar no cliente; nao abrir backend

## Criterios de conclusao

- [x] graficos relevantes ao master no `/dashboard`
- [x] dados reais das APIs existentes
- [x] empty states e a11y basica
- [x] teste do AdminDashboard atualizado

## Dependencias

- Slice 009 done

## Resultado da execucao

- secao "Graficos operacionais" com:
  - barras das metricas da plataforma
  - pizza de assinaturas por status
  - pizza de assinaturas por publico
  - pizza de conteudos por area
  - barras horizontais de pacientes ativos por profissional
- agregacao no cliente via builders dedicados

## Handoff

- `.agents/state/handoffs/TASK-447.md`

## Arquivos alterados

- `front-end/src/pages/Main/Admin/index.tsx`
- `front-end/src/pages/Main/Admin/AdminChartsSection.tsx`
- `front-end/src/pages/Main/Admin/components/AdminDashboardCharts.tsx`
- `front-end/src/pages/Main/Admin/buildAdminDashboardCharts.ts`
- `front-end/src/pages/Main/Admin/buildAdminDashboardCharts.test.ts`
- `front-end/src/pages/Main/Admin/index.test.tsx`
- `front-end/src/pages/Main/Admin/styles.module.css`

## Validacoes executadas

- testes Admin dashboard + builders ok

## Pendencias pos-task

- nenhuma; series temporais exigiria API nova

## Status final

done
