# Task 036 - Redesign do shell e dashboard web

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

- nao se aplica; preservar integracoes existentes

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Criar a fundacao visual renovada da area autenticada e aplicá-la ao sidebar, header, estrutura responsiva e dashboards por perfil.

## Contexto mínimo

- fontes globais obrigatorias, esta task, Slice 017 e handoff da Task 035

## Contexto sob demanda

- design system desktop
- `front-end/src/layout/{MainLayout,Sidebar,Header,PageContainer}/**`
- `front-end/src/pages/Main/{Dashboard,ShellHome,Admin}/**`
- tokens globais, componentes UI reutilizados e docs locais de acessibilidade/componentes

## Orçamento de contexto

- medio; restringir ao shell, dashboard e dependencias visuais diretas

## Criterios de conclusao

- [x] Sidebar e header renovados e responsivos
- [x] Dashboard profissional/responsavel e master com hierarquia visual real
- [x] Tokens e componentes compartilhados preparados para as proximas paginas
- [x] Testes, lint e build aprovados

## Resultado da execucao

- Shell autenticado renovado com sidebar escura de marca, icones Lucide, navegacao movel horizontal e indicador de ambiente.
- Header ganhou sessao compacta com avatar, melhor hierarquia e acao de logout.
- Dashboard profissional/responsavel deixou de ser provisório e passou a oferecer saudacao, atalhos, resumo diario e progresso.
- Dashboard master recebeu metricas visualmente hierarquizadas; cards e tokens compartilhados foram refinados.

## Contexto utilizado

- fontes globais, Slice 017, handoff 035, design system desktop, shell, dashboards, Card e acessibilidade local

## Handoff

- `.agents/state/handoffs/TASK-036.md`

## Arquivos alterados

- estilos globais, layouts `MainLayout`, `Sidebar`, `Header`, `PageContainer`
- `Card`, `ShellHome`, estilos do dashboard master e teste do `ShellHome`
- governanca da Task 036

## Validacoes executadas

- `npm run lint` - ok
- `npm run build` - ok
- `npm run test -- --run` - 21 arquivos e 34 testes aprovados

## Pendencias pos-task

- Warnings preexistentes de `act(...)` em dois testes de cadastro, sem falhas.

## Status final

done

## Dependencias

- Task 035
