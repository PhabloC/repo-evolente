# Task 202 - Corrigir layout do card diário da trilha

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

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 026 - Jogos terapeuticos e alfabeto falado

### Arquivo do slice

- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`

## Contexto de negocio

### O que

Corrigir o card do item diário da trilha para remover o aspecto torto gerado pela lixeira isolada.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-201.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Front-end | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`, `front-end/src/pages/Main/Plans/styles.module.css` | reorganizar o card diário | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: mudança localizada ao layout do item diário

## Criterios de conclusao

- card deixa de ficar torto
- botão de remover fica bem posicionado visualmente
- título e meta preservam boa leitura

## Resultado da execucao

- O card diário foi reorganizado em header e corpo, com a lixeira no canto superior direito.
- O item ganhou alinhamento e espaçamento consistentes, sem distorcer a caixa.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 202, slice 026, `TASK-201`
- contexto sob demanda: `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`, `front-end/src/pages/Main/Plans/styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-202.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/202-corrigir-layout-do-card-diario-da-trilha.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-202.md`

## Validacoes executadas

- revisão estática

## Pendencias pos-task

- nenhuma

## Status final

done
