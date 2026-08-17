# Task 048 - Refinar tabela de planejamentos por referência visual

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

- nao se aplica; reaproveitar a listagem atual de pacientes ativos

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

imagem fornecida pelo usuario no chat

### Cobertura

- cabeçalho claro da tabela
- primeira coluna com avatar e subtítulo
- pill de status suave
- botão de ação com mais destaque

### Lacunas

- a referência mostra apenas uma linha e estado ativo
- decisão: manter a tabela responsiva existente e aplicar o mesmo padrão visual para todas as linhas

## Objetivo

Deixar a tabela da página de planejamentos mais próxima da referência visual enviada, usando as cores do projeto.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 017 e `.agents/state/handoffs/TASK-047.md`

## Contexto sob demanda

- imagem enviada pelo usuário no chat
- `front-end/docs/ai/{AGENTS.md,ACCESSIBILITY.md}`
- `front-end/src/pages/Main/Plans/{index.tsx,styles.module.css}`
- `front-end/src/ui/Table/**`

## Orçamento de contexto

- baixo; restrito à listagem da página de planejamentos

## Criterios de conclusao

- [x] tabela da página de planejamentos segue a linguagem visual da referência
- [x] primeira coluna mostra avatar e apoio textual
- [x] status aparece em pill visual
- [x] botão `Montar trilha` recebe destaque coerente com a referência
- [x] lint aprovado

## Resultado da execucao

- a listagem de pacientes para planejar ganhou avatar circular, subtítulo e coluna de status
- o cabeçalho da tabela e o botão de ação foram refinados para ficar mais próximos da referência
- a customização ficou isolada no módulo de planejamentos usando classe local da tabela

## Contexto utilizado

- fontes globais, Slice 017, handoff 047, imagem do chat, docs locais de front/acessibilidade, página de planejamentos e `ui/Table`

## Handoff

- `.agents/state/handoffs/TASK-048.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/{index.tsx,styles.module.css}`
- `tasks/change-requests/048-refinar-tabela-planejamentos-por-referencia-visual.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run lint`

## Pendencias pos-task

- nenhuma

## Status final

done
