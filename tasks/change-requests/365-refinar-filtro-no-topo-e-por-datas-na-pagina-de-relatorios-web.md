# Task 365 - Refinar filtro no topo e por datas na página de relatórios web

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

- não se aplica; refino de UI e filtragem local sem alterar API

## Modo de execucao

single-stack

## Slice vertical

- Slice 011 - Relatorios de evolucao
- `tasks/slices/011-relatorios-evolucao.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- feedback direto do usuário no chat + screenshot da tabela de relatórios

### Fonte primaria visual

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

### Lacunas

- sem novo print completo da página; o refino segue a linguagem visual já consolidada na rota

## Objetivo

Colocar o filtro acima do bloco de geração, adicionar filtragem por datas ao histórico e refinar os textos de apoio da página de relatórios.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Estrutura da página | `front-end/src/pages/Main/Reports/index.tsx` | reordenar blocos, separar estados e aplicar filtro por datas | sim |
| Composição visual | `front-end/src/pages/Main/Reports/styles.module.css` | aumentar o respiro entre cards e acomodar os novos campos | sim |

## Orçamento de contexto

- baixo
- estrategia: limitar a mudança à rota `/relatorios`, sem alterar services ou contrato

## Criterios de conclusao

- [x] o card de filtro fica acima do card de gerar relatório
- [x] o filtro do histórico passa a aceitar intervalo de datas
- [x] existe respiro visível entre os dois cards
- [x] os textos de apoio da página ficam mais claros
- [x] `npx eslint src/pages/Main/Reports/index.tsx`

## Dependencias

- Task 364 - done

## Resultado da execucao

- o histórico agora aparece primeiro, com filtros por paciente e intervalo de datas
- a geração ficou abaixo, separada visualmente por um espaçamento claro entre os cards
- a tabela passou a aplicar filtro local por data de criação sem depender de mudança na API
- a copy do subtítulo, dos blocos e do aviso inferior foi reescrita para refletir melhor o fluxo da página

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/011-relatorios-evolucao.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`

## Handoff

- `.agents/state/handoffs/TASK-365.md`

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/365-refinar-filtro-no-topo-e-por-datas-na-pagina-de-relatorios-web.md`
- `tasks/000-index.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-365.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done
