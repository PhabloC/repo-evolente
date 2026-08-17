# Task 363 - Transformar "Gerado em" em badge na tabela de relatórios web

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

- não se aplica; ajuste visual na tabela sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- feedback direto do usuário no chat sobre a tabela atual

### Fonte primaria visual

- screenshot da tabela de relatórios enviado nesta sessão
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

### Lacunas

- sem novo print dedicado do estado final; o badge deve seguir a linguagem visual já consolidada da tabela

## Objetivo

Apresentar a coluna `Gerado em` como badge na tabela da página `/relatorios`.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-362.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | manter legibilidade e contraste do badge na tabela | sim |
| Tabela de relatórios | `front-end/src/pages/Main/Reports/index.tsx` | alterar o render da coluna `Gerado em` | sim |
| Estilos da página | `front-end/src/pages/Main/Reports/styles.module.css` | compor o badge da data | sim |

## Orçamento de contexto

- baixo
- estrategia: restringir a mudança ao render e estilo da coluna `Gerado em`

## Criterios de conclusao

- [x] a coluna `Gerado em` passa a renderizar a data em badge
- [x] o badge mantém contraste e leitura consistente com a tabela
- [x] `npx eslint src/pages/Main/Reports/index.tsx`

## Dependencias

- Task 362 - done

## Resultado da execucao

- a data de geração dos relatórios passou a ser exibida em uma badge arredondada
- o novo tratamento visual aproxima a coluna `Gerado em` da linguagem dos demais estados destacados na tabela

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-362.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-363.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/363-transformar-gerado-em-em-badge-na-tabela-de-relatorios-web.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-363.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done
