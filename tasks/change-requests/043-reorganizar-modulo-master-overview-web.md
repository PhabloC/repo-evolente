# Task 043 - Reorganizar modulo master em overview e paginas dedicadas

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

- nao se aplica; preservar integracoes existentes do admin

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Objetivo

Transformar o dashboard master em uma pagina de overview e distribuir usuarios, planos, relatorios e logs em rotas dedicadas, com configuracoes em dropdown.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e `.agents/state/handoffs/TASK-041.md`

## Contexto sob demanda

- `front-end/src/constants/{navigation,routes}.ts`
- `front-end/src/layout/Sidebar/**`
- `front-end/src/pages/Main/Admin/**`
- `front-end/src/routes/index.tsx`

## Resultado da execucao

- dashboard master agora funciona como overview do modulo
- usuarios, planos, relatorios e logs ganharam paginas dedicadas
- configuracoes passou a abrir dropdown com perfil e logs

## Handoff

- `.agents/state/handoffs/TASK-043.md`
