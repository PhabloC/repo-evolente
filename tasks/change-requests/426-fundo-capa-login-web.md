# Task 426 - Fundo capa na tela de login web

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

- sem alteração

## Modo de execução

single-stack

## Slice vertical

- Slice 012 - Login visual e acesso livre (web)
- `tasks/slices/012-login-visual-acesso-livre.md`

## Objetivo

Usar `front-end/src/assets/capa-tela-login.webp` como fundo da tela de login web.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/012-login-visual-acesso-livre.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Layout auth | `front-end/src/layout/AuthLayout/` | aplicar fundo só quando solicitado |
| Login | `front-end/src/pages/Auth/Login/` | ativar capa |
| Asset | `front-end/src/assets/capa-tela-login.webp` | imagem de fundo |

## Orçamento de contexto

- baixo

## Critérios de conclusão

- [x] `/login` usa `capa-tela-login.webp` como fundo (cover)
- [x] outras telas AuthLayout não herdam o fundo sem prop
- [x] formulário permanece usável
- [x] teste de login passa

## Resultado da execucao

- Prop `coverBackground` no `AuthLayout` aplica `capa-tela-login.webp` via CSS variable `--auth-cover-image` (`background-size: cover`).
- Ativado apenas em `LoginPage`.

## Contexto utilizado

- AuthLayout, Login, asset `capa-tela-login.webp`, Slice 012

## Handoff

- `.agents/state/handoffs/TASK-426.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `front-end/src/pages/Auth/Login/index.tsx`
- `tasks/change-requests/426-fundo-capa-login-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-426.md`

## Validacoes executadas

- `npx vitest run src/pages/Auth/Login/index.test.tsx` — 1 passed

## Pendencias pos-task

- nenhuma

## Status final

done
