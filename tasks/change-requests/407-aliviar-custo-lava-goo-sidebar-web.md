# Task 407 - Aliviar custo da lava goo do sidebar web

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

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Objetivo

Manter o efeito goo da lava do sidebar, reduzindo o custo: pausar no scroll e com aba oculta, e processar o filtro em resolução menor.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Lava persistente | `front-end/src/layout/Sidebar/persistentLava.tsx` | pause API + markup low-res |
| Estilos | `front-end/src/layout/Sidebar/styles.module.css` | low-res + play-state |
| Scroll | `front-end/src/layout/MainLayout/index.tsx` | pausar durante scroll |
| Regressão | `persistentLava.test.tsx` | cobrir pause |

## Orçamento de contexto

- baixo

## Critérios de conclusão

- [x] lava pausa durante scroll do conteúdo e retoma ao parar
- [x] lava pausa com `document.hidden`
- [x] filtro goo roda em resolução reduzida (scale)
- [x] efeito visual goo preservado
- [x] testes da lava passam

## Resultado da execucao

- `setSidebarLavaPaused(reason, paused)` com motivos `scroll`/`hidden`
- MainLayout pausa no scroll e retoma ~180ms após parar; visibilitychange pausa com aba oculta
- Goo em buffer 50% + `scale(2)`; blobs em `em` com `font-size: 0.5rem`
- `stdDeviation` do blur reduzido de 10 → 8; `prefers-reduced-motion` desliga o filtro

## Contexto utilizado

- persistentLava, Sidebar CSS, MainLayout

## Handoff

- `.agents/state/handoffs/TASK-407.md`

## Arquivos alterados

- `front-end/src/layout/Sidebar/persistentLava.tsx`
- `front-end/src/layout/Sidebar/persistentLava.test.tsx`
- `front-end/src/layout/Sidebar/styles.module.css`
- `front-end/src/layout/MainLayout/index.tsx`
- `tasks/change-requests/407-aliviar-custo-lava-goo-sidebar-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-407.md`

## Validacoes executadas

- `npx vitest run src/layout/Sidebar/persistentLava.test.tsx` — 3 passed

## Pendencias pos-task

- nenhuma

## Status final

done
