# Handoff - Task 617

## Task

- TASK-617 - Corrigir empilhamento da busca sobre dashboard web
- Slice 017 — Redesign da interface interna web
- status final: done

## Decisões preservadas

- `.content > main` usa `z-index: 0`; Header permanece em `z-index: 100` e o balão em `z-index: 1000`.

## Contexto efetivamente usado

- Task 617, Slice 017, handoff Task 616 e CSS do MainLayout.

## Arquivos alterados

- `front-end/src/layout/MainLayout/styles.module.css`

## Validações

- Inspeção da ordem de empilhamento do shell.

## Pendências ou bloqueios

- Smoke visual no dashboard.

## Próximo contexto recomendado

- `front-end/src/layout/MainLayout/styles.module.css`, caso outra página crie um novo contexto de empilhamento.
