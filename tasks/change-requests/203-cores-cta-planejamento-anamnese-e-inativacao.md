# Task 203 - Cores dos CTAs de anamnese e inativação da trilha

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

Ajustar a cor de fundo dos CTAs `Sugerir pela anamnese` e `Inativar trilha` no header do planejamento.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `.agents/state/handoffs/TASK-202.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Front-end | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`, `front-end/src/pages/Main/Plans/styles.module.css` | ajuste visual dos CTAs | sim |

## Orçamento de contexto

- Risco baixo
- Estrategia de reducao: mudança localizada aos botões do header da semana

## Criterios de conclusao

- `Sugerir pela anamnese` usa fundo amarelo
- `Inativar trilha` usa fundo vermelho quando a trilha estiver ativa

## Resultado da execucao

- O CTA de sugestão ganhou variação amarela.
- O CTA de inativação ganhou variação vermelha para o estado de trilha ativa.

## Contexto utilizado

- contexto mínimo: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, task 203, slice 026, `TASK-202`
- contexto sob demanda: `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`, `front-end/src/pages/Main/Plans/styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-203.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/203-cores-cta-planejamento-anamnese-e-inativacao.md`
- `tasks/slices/026-jogos-terapeuticos-alfabeto.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-203.md`

## Validacoes executadas

- revisão estática

## Pendencias pos-task

- nenhuma

## Status final

done
