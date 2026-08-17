# Task 406 - Refinar design do card de jogo na biblioteca web

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

Corrigir o overlap das chips de metadados no card de jogo e refinar hierarquia visual (capa, título, status, ações).

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-405.md`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Card atual | `front-end/src/pages/Main/Library/styles.module.css` | corrigir layout |
| Markup | `front-end/src/pages/Main/Library/index.tsx` | ajustes estruturais se necessário |
| Regressão | `front-end/src/pages/Main/Library/index.test.tsx` | garantir cards intactos |

## Orçamento de contexto

- baixo

## Critérios de conclusão

- [x] chips de metadados não se sobrepõem
- [x] título, status e ações com hierarquia mais clara
- [x] cards master e profissional preservam ações existentes
- [x] teste focado da biblioteca passa

## Resultado da execucao

- Meta chips saíram do grid 3 colunas (causa do overlap) e passaram a `flex-wrap`.
- Card mais limpo: fundo branco, capa full-bleed maior, sombra suave, hover com leve elevação.
- Status alinhado ao topo do título; ações em barra separada com botões retangulares arredondados.

## Contexto utilizado

- estilos/markup da Library, Slice 017, handoff 405

## Handoff

- `.agents/state/handoffs/TASK-406.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/406-refinar-design-card-jogo-biblioteca-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-406.md`

## Validacoes executadas

- `npx vitest run ... -t "shows icon actions for game card"` — OK
- `filters featured games` — OK no run anterior agrupado

## Pendencias pos-task

- nenhuma

## Status final

done
