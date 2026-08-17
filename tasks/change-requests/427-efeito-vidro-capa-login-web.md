# Task 427 - Efeito de vidro sobre a capa do login web

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

Aplicar efeito de vidro (blur + translucidez) sobre a imagem de fundo da tela de login.

## Contexto mínimo

- `AGENTS.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- handoff Task 426

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Capa login | `front-end/src/layout/AuthLayout/styles.module.css` | camadas imagem + vidro |
| Prop existente | `AuthLayout` `coverBackground` | só quando capa ativa |

## Orçamento de contexto

- baixo

## Critérios de conclusão

- [x] overlay de vidro sobre `capa-tela-login.webp` no login
- [x] conteúdo (branding + card) permanece legível e clicável
- [x] sem impacto nas telas auth sem `coverBackground`

## Resultado da execucao

- `::before` renderiza a capa com blur; `::after` aplica verniz branco translúcido (efeito vidro).
- Conteúdo permanece em `z-index: 1` com `pointer-events` intactos.

## Contexto utilizado

- AuthLayout CSS, Task 426

## Handoff

- `.agents/state/handoffs/TASK-427.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/styles.module.css`
- `tasks/change-requests/427-efeito-vidro-capa-login-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-427.md`

## Validacoes executadas

- revisão visual via CSS; sem mudança de markup além do já existente em 426

## Pendencias pos-task

- nenhuma

## Status final

done

## Dependências

- Task 426
