# Handoff - Task 319

## Task

- identificador: 319
- titulo: Reordenar ação Disponibilizar na tabela de relatórios
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao
- objetivo de negocio: priorizar a ação de compartilhamento na leitura operacional da tabela
- entrega verificavel: `Disponibilizar` aparece como primeiro botão na fileira da coluna `Ações` quando aplicável

## Decisoes preservadas

- a mudança ficou restrita à ordem de renderização dos CTAs na página `Reports`
- `Disponibilizar` passou a ser o primeiro CTA quando o relatório ainda não foi compartilhado
- `Baixar` e exclusão permaneceram no mesmo fluxo, sem alteração de estilo ou comportamento

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/319-reordenar-acao-disponibilizar-na-tabela-de-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-318.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Reports/index.tsx` | ajuste visual pontual | reordenar os botões da coluna `Ações` |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `backend/` | sem alteração de contrato ou regra de negócio |

## Resultado por stack

- front-end: `Disponibilizar` priorizado como primeira ação na tabela
- backend: sem alterações
- mobile: sem alterações

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `tasks/change-requests/319-reordenar-acao-disponibilizar-na-tabela-de-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`: ok
- `cd front-end && npm run build`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido para reordenar ou compactar os demais CTAs dessa tabela

## Proximo contexto recomendado

- `front-end/src/pages/Main/Reports/index.tsx`
