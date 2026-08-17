# Task 319 - Reordenar ação Disponibilizar na tabela de relatórios

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

- nao se aplica; ajuste de ordem visual sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- feedback direto do usuario

### Fonte primaria visual

- `front-end/src/pages/Main/Reports/**`

### Lacunas

- sem print novo; a mudanca se limita a ordem dos CTAs na coluna `Ações`

## Objetivo

Colocar a ação `Disponibilizar` como o primeiro botão na fileira da coluna `Ações` da tabela de relatórios.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-318.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página de relatórios | `front-end/src/pages/Main/Reports/**` | reordenar os CTAs da coluna | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança ao componente da página `Reports`

## Criterios de conclusao

- [x] `Disponibilizar` aparece como primeira ação quando disponível
- [x] `Baixar` e exclusão continuam funcionando na mesma linha
- [x] a rota `/relatorios` continua sem regressão visual ou funcional

## Dependencias

- Task 318 - done

## Resultado da execucao

- a ordem dos CTAs na coluna `Ações` foi reordenada para renderizar `Disponibilizar` primeiro quando o relatório ainda não foi compartilhado
- `Baixar` e o botão ícone-only de exclusão foram mantidos na mesma fileira, sem alterar comportamento
- a rota `/relatorios` permaneceu funcional após o ajuste

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-318.md`

### Sob demanda

- `front-end/src/pages/Main/Reports/index.tsx`

### Contexto evitado

- `backend/`, porque não há alteração de contrato ou regra de negócio

## Handoff

- `.agents/state/handoffs/TASK-319.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `tasks/change-requests/319-reordenar-acao-disponibilizar-na-tabela-de-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-319.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`
- `cd front-end && npm run build`

## Pendencias pos-task

- nenhuma

## Status final

done
