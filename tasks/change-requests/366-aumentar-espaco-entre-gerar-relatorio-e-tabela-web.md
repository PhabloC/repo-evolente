# Task 366 - Aumentar espaço entre gerar relatório e tabela web

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

- não se aplica; ajuste visual pontual sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- feedback direto do usuário no chat

### Fonte primaria visual

- `front-end/src/pages/Main/Reports/styles.module.css`
- `front-end/src/pages/Main/Reports/index.tsx`

### Lacunas

- sem novo print; ajuste restrito ao espaçamento vertical entre o card de geração e a tabela

## Objetivo

Aumentar o respiro visual entre o bloco `Gerar relatório` e a tabela de histórico na página `/relatorios`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Espaçamento visual | `front-end/src/pages/Main/Reports/styles.module.css` | aumentar a distância entre geração e tabela | sim |
| Estrutura da página | `front-end/src/pages/Main/Reports/index.tsx` | confirmar o ponto exato do espaçamento | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar o ajuste ao espaçamento do container da tabela

## Criterios de conclusao

- [x] a tabela passa a ficar mais afastada do card `Gerar relatório`
- [x] `npx eslint src/pages/Main/Reports/index.tsx`

## Dependencias

- Task 365 - done

## Resultado da execucao

- a área da tabela ganhou mais respiro vertical em relação ao bloco de geração de relatório

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-366.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/366-aumentar-espaco-entre-gerar-relatorio-e-tabela-web.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-366.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done
