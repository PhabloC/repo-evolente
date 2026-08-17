# Task 201 - Ícone vermelho para remover item da trilha

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

Reduzir a ação de remover item da trilha para um botão só com ícone de lixeira, em vermelho.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-200.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Front-end | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`, `front-end/src/pages/Main/Plans/styles.module.css` | ajuste visual do botão | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: mudança localizada ao CTA de remoção no card do dia

## Criterios de conclusao

- botão de remover exibe apenas o ícone
- ícone/botão fica em vermelho

## Resultado da execucao

- A ação `Remover` do card do dia foi reduzida para um botão só com ícone de lixeira.
- O controle passou a usar estilo vermelho, preservando nome acessível via `aria-label`.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 201, slice 026, `TASK-200`
- contexto sob demanda: `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`, `front-end/src/pages/Main/Plans/styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-201.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/201-icone-vermelho-remover-item-da-trilha.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-201.md`

## Validacoes executadas

- revisão estática

## Pendencias pos-task

- nenhuma

## Status final

done
