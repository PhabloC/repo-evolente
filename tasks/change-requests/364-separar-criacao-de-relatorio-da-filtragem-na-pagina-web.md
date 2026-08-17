# Task 364 - Separar criação de relatório da filtragem na página web

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

- não se aplica; refino de UX na composição da página sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- feedback direto do usuário no chat sobre a semântica da página

### Fonte primaria visual

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

### Lacunas

- sem print novo; a separação deve reaproveitar a linguagem visual atual da tela

## Objetivo

Separar a criação de relatório da filtragem do histórico na página `/relatorios`, deixando o filtro com função exclusivamente de filtragem.

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
| UI web | `front-end/docs/ai/ACCESSIBILITY.md` | preservar semântica, labels e ordem de foco na nova composição | sim |
| Página de relatórios | `front-end/src/pages/Main/Reports/index.tsx` | separar os estados e blocos de criação e filtragem | sim |
| Estilos da página | `front-end/src/pages/Main/Reports/styles.module.css` | compor as duas superfícies visuais | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à composição e ao estado local da rota `/relatorios`

## Criterios de conclusao

- [x] a criação de relatório aparece em bloco próprio
- [x] a filtragem do histórico aparece em bloco separado
- [x] o filtro deixa de participar do fluxo de criação
- [x] `npx eslint src/pages/Main/Reports/index.tsx`

## Dependencias

- Task 362 - done

## Resultado da execucao

- a página foi dividida entre um bloco de geração de relatório e outro de filtragem do histórico
- o paciente usado para criar relatório passou a ser independente do paciente usado para filtrar a tabela
- a ação de limpar filtro foi explicitada e a navegação para planejamentos foi movida para a área de histórico

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

- `.agents/state/handoffs/TASK-364.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/364-separar-criacao-de-relatorio-da-filtragem-na-pagina-web.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-364.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done
