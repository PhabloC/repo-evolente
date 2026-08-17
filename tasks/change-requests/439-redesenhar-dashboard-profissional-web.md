# Task 439 - Redesenhar dashboard profissional web

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

- nao se aplica; reutilizar APIs ja usadas pelo summary (`patients`, `trails`, `progress`, `reports`, `contents`) sem novos endpoints

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- ajuste funcional/layout solicitado via chat

### Fonte primaria visual

- linguagem visual atual do dashboard profissional (`ShellHome`) e tokens do design system desktop
- graficos com `recharts` no padrao ja usado em planejamentos

### Lacunas

- solicitacao nao inclui print; layout novo segue composicao pedida no chat e padroes existentes

## Objetivo

Substituir o conteudo operacional atual do `/dashboard` do profissional por: metricas sem mini-graficos, grafico de linha de evolucao geral, pizza por area, atividades de hoje, carrossel de maior progresso e card de relatorios semanais; remover o restante.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI dashboard | `front-end/src/pages/Main/ShellHome/` | redesenhar layout | sim |
| Summary/dados | `front-end/src/services/dashboard/`, `front-end/src/types/dashboard.ts` | estender payload | sim |
| Graficos | `recharts` + uso em `PatientTrail` | padrao de chart | sim |
| Acessibilidade | `front-end/docs/ai/ACCESSIBILITY.md` | secoes, status e carrossel | sim |
| Avatar paciente | `PatientAvatar` | fotos nas listas | sim |

## Orçamento de contexto

- medio
- estrategia: limitar ao ShellHome, summary e tipos; nao abrir backend/mobile/openapi

## Criterios de conclusao

- [x] 4 cards iniciais sem mini-graficos de barras
- [x] grafico de linha com atividades concluidas, engajamento e evolucao media
- [x] grafico de pizza de atividades por area
- [x] card de atividades de hoje (foto, nome, atividade, status)
- [x] carrossel de pacientes com maior progresso (foto, nome, %, barra)
- [x] card de relatorios semanais disponiveis
- [x] demais paineis antigos removidos
- [x] testes do ShellHome atualizados; lint/test focados ok

## Dependencias

- Task 056 - done (dados reais do dashboard)
- Task 346 - done (CTA abaixo do header)

## Fora de escopo

- novos endpoints backend
- mudancas no dashboard master
- mobile

## Resultado da execucao

- dashboard profissional redesenhado com metricas limpas, linha de evolucao (6 semanas), pizza por area, atividades de hoje, carrossel de maior progresso e relatorios semanais
- paineis antigos (prioridades, planejamentos, acompanhamento clinico, cadencia, alertas e atalhos) removidos
- summary estendido com builders derivados das APIs existentes + `listContents` para titulo/categoria

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

### Sob demanda

- `front-end/src/pages/Main/ShellHome/`
- `front-end/src/services/dashboard/`
- `front-end/src/types/dashboard.ts`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `PatientAvatar` e padrao recharts de `PatientTrail`

### Contexto evitado

- backend, mobile, openapi, next-js

## Handoff

- `.agents/state/handoffs/TASK-439.md`

## Arquivos alterados

- `front-end/src/types/dashboard.ts`
- `front-end/src/services/dashboard/getDashboardSummary.ts`
- `front-end/src/services/dashboard/buildDashboardPanels.ts`
- `front-end/src/services/dashboard/buildDashboardPanels.test.ts`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/pages/Main/ShellHome/components/*`
- `tasks/change-requests/439-redesenhar-dashboard-profissional-web.md`
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- --run src/pages/Main/ShellHome/index.test.tsx src/services/dashboard/buildDashboardPanels.test.ts` — ok
- `npm run lint -- --quiet src/pages/Main/ShellHome src/services/dashboard src/types/dashboard.ts` — ok
- acessibilidade: headings, `role="img"` nos charts, status em texto, carrossel com botoes nomeados, `progressbar` com aria

## Pendencias pos-task

- nenhuma bloqueante; se quiser fidelidade pixel a um print, enviar referencia visual

## Status final

done
