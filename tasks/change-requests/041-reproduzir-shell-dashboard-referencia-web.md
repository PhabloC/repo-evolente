# Task 041 - Reproduzir shell e dashboard por nova referencia

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

- nao se aplica; preservar dados e integracoes existentes

## Modo de execucao

single-stack

## Slice vertical

- Slice 019 - Reproducao de shell dashboard por referencia externa
- `tasks/slices/019-referencia-shell-dashboard-ambiental-web.md`

## Referencia visual

### Tipo

imagem fornecida pelo usuario no chat

### Cobertura

- shell externo escuro com sidebar integrada ao frame
- miolo branco com cantos arredondados dentro do shell
- dashboard com faixa superior de metricas, paineis principais e CTA visual

### Lacunas

- a imagem referencia um produto ambiental e contem metricas/mapas que nao pertencem ao dominio Evolente
- decisao: reproduzir composicao, proporcao, hierarquia e linguagem visual sem apresentar dados falsos como reais

## Objetivo

Reproduzir na area autenticada web o layout observado na imagem enviada pelo usuario, com shell em moldura escura integrada ao sidebar e dashboard inicial com composicao equivalente.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 019 e `.agents/state/handoffs/TASK-040.md`

## Contexto sob demanda

- imagem enviada pelo usuario no chat
- `front-end/src/layout/{MainLayout,Sidebar,Header,PageContainer}/**`
- `front-end/src/pages/Main/ShellHome/**`
- `front-end/src/ui/{Button,Card}/**` se necessario

## Orçamento de contexto

- medio; limitar ao shell autenticado e dashboard inicial

## Criterios de conclusao

- [x] shell autenticado passa a ter frame externo escuro com sidebar integrada
- [x] conteudo principal fica encapsulado em painel branco com bordas arredondadas
- [x] dashboard inicial replica a hierarquia visual da referencia sem inventar dados clinicos
- [x] lint, build e teste focado aprovados

## Resultado da execucao

- shell autenticado agora usa moldura escura esverdeada, sidebar integrada e painel interno branco com padding e bordas generosas
- header foi simplificado para atuar como topo do painel interno, coerente com a referencia
- dashboard inicial foi refeito com metricas superiores, paineis grandes, indice circular e CTA visual na mesma composicao do print

## Contexto utilizado

- fontes globais, Slice 019, handoff 040, imagem do chat e arquivos do shell/dashboard web

## Handoff

- `.agents/state/handoffs/TASK-041.md`

## Arquivos alterados

- `front-end/src/layout/MainLayout/**`
- `front-end/src/layout/Sidebar/**`
- `front-end/src/layout/Header/**`
- `front-end/src/layout/PageContainer/**`
- `front-end/src/pages/Main/ShellHome/**`
- task, slice, indice e handoff

## Validacoes executadas

- `npm run lint` - ok
- `npm run build` - ok
- `npm run test -- ShellHome` - ok

## Pendencias pos-task

- a CTA lateral e alguns micrograficos permanecem estaticos porque esta task e puramente visual

## Status final

done

## Dependencias

- Task 040 - done
