# Task 035 - Remover fundo auth web

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

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Remover integralmente o SVG e todas as animacoes de fundo do `AuthLayout`, mantendo o fundo limpo nas telas de login, cadastro e recuperacao.

## Contexto mínimo

- fontes globais obrigatorias, esta task, Slice 017 e `.agents/state/handoffs/TASK-034.md`

## Contexto sob demanda

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Orçamento de contexto

- baixo; limitado ao layout auth compartilhado

## Criterios de conclusao

- [x] SVG e CSS de animacao removidos
- [x] Auth sem conteudo decorativo de fundo
- [x] Lint e build aprovados

## Resultado da execucao

- SVG, formas, filtros e animacoes da Task 034 removidos integralmente do `AuthLayout`.
- Login, cadastro, recuperacao e reset preservam o fundo base limpo do design system.

## Contexto utilizado

- fontes globais, Slice 017, handoff 034, `AuthLayout` e acessibilidade local

## Handoff

- `.agents/state/handoffs/TASK-035.md`

## Arquivos alterados

- `front-end/src/layout/AuthLayout/index.tsx`
- `front-end/src/layout/AuthLayout/styles.module.css`
- esta task, indice e handoff

## Validacoes executadas

- `npm run lint` - ok
- `npm run build` - ok

## Pendencias pos-task

- Nenhuma.

## Status final

done
