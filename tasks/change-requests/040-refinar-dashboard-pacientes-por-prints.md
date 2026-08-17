# Task 040 - Refinar dashboard e pacientes por prints

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

- nao se aplica; preservar dados e integracoes existentes

## Modo de execucao

single-stack

## Slice vertical

- Slice 018 - Fidelidade visual dashboard e pacientes web
- `tasks/slices/018-fidelidade-visual-dashboard-pacientes-web.md`

## Referencia visual

### Tipo

prints de telas fornecidos pelo usuario

### Fontes primarias

- `design-system/front/prints/dashboard-overview-reference.png`: dashboard profissional desktop
- `design-system/front/prints/dashboard-pacientes-reference.png`: listagem de pacientes desktop

### Cobertura

- sidebar, topo, busca, perfil, metricas, paineis e densidade do dashboard
- cabecalho, filtros, metricas, tabela e paineis auxiliares de pacientes

### Lacunas

- prints mostram dados, fotos, agenda, notificacoes e metricas nao garantidos pelo produto atual
- decisao: reproduzir estrutura e linguagem visual usando somente dados existentes ou estados vazios honestos

## Objetivo

Refinar o redesign interno para se inspirar diretamente nos dois prints, com foco no shell, dashboard e pacientes e propagacao da fundacao visual às demais paginas.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 018 e `.agents/state/handoffs/TASK-039.md`

## Contexto sob demanda

- os dois prints declarados
- `front-end/src/layout/{MainLayout,Sidebar,Header,PageContainer}/**`
- `front-end/src/pages/Main/{ShellHome,Patients}/**`
- UI compartilhada diretamente afetada e acessibilidade local

## Orçamento de contexto

- medio; nao carregar backend, mobile, auth ou paginas sem impacto direto

## Criterios de conclusao

- [x] Shell claro e estrutura superior alinhados aos prints
- [x] Dashboard mais denso e modular sem inventar dados reais
- [x] Pacientes com cabecalho, filtros e conteudo alinhados à referência
- [x] Responsividade, acessibilidade, lint, build e testes aprovados

## Resultado da execucao

- Sidebar mudou para base clara com logo colorido, navegacao azul ativa e superficie auxiliar quente.
- Header recebeu busca superior, notificacao acessivel e perfil compacto, seguindo a composicao dos prints.
- Dashboard ganhou quatro atalhos modulares e hero claro, preservando estados honestos para agenda e evolucao.
- Pacientes recebeu quatro indicadores calculados da resposta real e busca funcional por nome/codigo.
- A fundacao clara e quente se propaga para todas as paginas do shell compartilhado.

## Contexto utilizado

- fontes globais, Slice 018, handoff 039, dois prints fornecidos, Header, Sidebar, MainLayout, ShellHome, Patients e acessibilidade local

## Handoff

- `.agents/state/handoffs/TASK-040.md`

## Arquivos alterados

- `design-system/front/prints/dashboard-overview-reference.png`
- `design-system/front/prints/dashboard-pacientes-reference.png`
- `front-end/src/layout/Header/**`
- `front-end/src/layout/Sidebar/styles.module.css`
- `front-end/src/layout/MainLayout/styles.module.css`
- `front-end/src/pages/Main/ShellHome/**`
- `front-end/src/pages/Main/Patients/**`
- task, slice, indice e handoff

## Validacoes executadas

- `npm run lint` - ok
- `npm run build` - ok
- testes focados ShellHome/Patients - 2 aprovados
- suite completa - 21 arquivos e 34 testes aprovados

## Pendencias pos-task

- Busca global e sino são elementos de interface sem integracao de backend nesta task.
- Agenda, fotos, graficos e metricas inexistentes nao foram simulados.
- Permanecem dois warnings preexistentes de `act(...)` nos testes de cadastro.

## Status final

done

## Dependencias

- Task 039 - done
