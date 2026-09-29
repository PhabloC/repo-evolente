# Handoff - Task 747

## Task

- TASK-747 - Responsividade do dashboard e da sidebar web
- Slice 019 — shell dashboard web
- status final: done

## Decisões preservadas

- Abaixo de 960px a sidebar vira gaveta (`position: fixed`), aberta pelo botão Menu do header.
- Fechar: botão, overlay, Escape ou clique num link. Foco volta ao Menu ou ao `main`.
- A animação da lava pausa com o motivo `drawer` enquanto a gaveta está fechada.
- A transição da gaveta só liga depois do primeiro frame, para não aparecer no carregamento.
- Dashboards profissional, responsável e master empilham métricas e gráficos até 640px.

## Contexto efetivamente usado

- Layout Sidebar, MainLayout, Header e estilos de ShellHome, Admin e Guardian.

## Arquivos alterados

- `front-end/src/layout/Sidebar/`
- `front-end/src/layout/MainLayout/`
- `front-end/src/layout/Header/`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/pages/Main/Guardian/styles.module.css`

## Validações

- Vitest do Sidebar e do Header.
- ESLint dos arquivos de layout alterados.
- Viewport 390px: botão Menu, gaveta aberta e fechamento ao escolher Dashboard.

## Pendências ou bloqueios

- Gráficos com dados reais não foram vistos: a sessão local de teste não autenticou na API.

## Próximo contexto recomendado

- `front-end/src/layout/Sidebar/styles.module.css` se o breakpoint de 960px mudar.

## Contexto que não deve ser carregado

- requirements, contrato OpenAPI e design-system mobile.
