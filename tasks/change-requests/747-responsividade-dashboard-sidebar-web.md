# Task 747 - Responsividade do dashboard e da sidebar web

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

Não se aplica.

## Modo de execução

single-stack

## Slice vertical

- Slice 019 — `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Objetivo

Deixar o dashboard web e o menu lateral utilizáveis em viewport de celular.

## Dependências

- Slice 019 — done
- Slice 052 — done

## Contexto mínimo

- esta task
- `front-end/src/layout/Sidebar/`
- `front-end/src/layout/MainLayout/`
- `front-end/src/layout/Header/`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/pages/Main/Guardian/styles.module.css`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Lavas da sidebar | `persistentLava.tsx` | pausar a animação com a gaveta fechada |
| Dashboard do responsável e master | estilos já citados | empilhar cards e gráficos |

## Orçamento de contexto

- baixo
- estratégia: alterar só o shell autenticado e os estilos dos três dashboards que compartilham a rota `/dashboard`.

## Critérios de aceite

- [x] Abaixo de 960px a sidebar vira gaveta, com botão Menu, fechar, overlay e atalhos de conta.
- [x] Os dashboards de profissional, responsável e master empilham métricas e gráficos no celular.
- [x] A animação da sidebar pausa enquanto a gaveta está fechada.

## Fora de escopo

- telas que não são o dashboard, além do shell compartilhado (sidebar e cabeçalho)
- app mobile
