# Handoff - Task 318

## Task

- identificador: 318
- titulo: Reduzir ação de excluir para ícone na tabela de relatórios
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao
- objetivo de negocio: compactar a ação de exclusão na tabela mantendo clareza operacional
- entrega verificavel: a rota `/relatorios` exibe a exclusão como botão de ícone de lixeira e ainda abre o modal de confirmação

## Decisoes preservadas

- a exclusão passou a usar botão ícone-only na tabela, sem texto visual
- o botão recebeu nome acessível explícito via `aria-label`
- o modal de confirmação destrutiva da task 317 foi mantido sem alteração de fluxo

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/318-reduzir-acao-de-excluir-para-icone-na-tabela-de-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-317.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md` | botão sem texto | preservar nome acessível e foco |
| `front-end/docs/ai/COMPONENT_REUSE.md` | reuso da primitiva | manter a solução dentro do `Button` compartilhado |
| `front-end/src/pages/Main/Reports/{index.tsx,styles.module.css}` | implementação | transformar a ação em ícone-only |
| `front-end/src/ui/Button/index.tsx` | conferência | validar suporte já existente a botão só com ícone |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `backend/` | sem mudança de API, regra de negócio ou persistência |

## Resultado por stack

- front-end: ação de exclusão compactada para ícone-only com modal preservado
- backend: sem alterações
- mobile: sem alterações

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/318-reduzir-acao-de-excluir-para-icone-na-tabela-de-relatorios.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`: ok
- `cd front-end && npm run build`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- só revisitar esta ação se houver pedido para compactar também `Baixar` ou `Disponibilizar`

## Proximo contexto recomendado

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
