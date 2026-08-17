# Handoff - Task 315

## Task

- identificador: 315
- titulo: Ajustar botão Baixar na tabela de relatórios web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 011 - Relatorios de evolucao
- objetivo de negocio: melhorar a leitura operacional da tabela de relatórios
- entrega verificavel: o botão `Baixar` tem cor própria e a coluna `Ações` fica alinhada ao cabeçalho

## Decisoes preservadas

- o ajuste ficou isolado na página `Reports`, sem alterar a primitiva global `Button`
- a ação `Baixar` recebeu um tratamento visual azul-claro para ganhar identidade própria sem competir com CTAs primários
- o alinhamento foi resolvido no contêiner local da célula de ações com `justify-content: flex-end`

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/315-ajustar-botao-baixar-na-tabela-de-relatorios-web.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `.agents/state/handoffs/TASK-314.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/{AGENTS.md,ARCHITECTURE.md,ACCESSIBILITY.md}` | ajuste visual web | manter coerência estrutural e semântica |
| `front-end/src/pages/Main/Reports/{index.tsx,styles.module.css}` | implementação local | alterar CTA e alinhamento da coluna |
| `front-end/src/ui/Button/**` | composição do CTA | reaproveitar primitiva existente com classe local |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `backend/` | sem mudança funcional ou de API |
| `contracts/openapi.yaml` | sem alteração de contrato |

## Resultado por stack

- front-end: botão `Baixar` diferenciado visualmente e coluna `Ações` alinhada
- backend: sem alterações
- mobile: sem alterações

## Arquivos alterados

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
- `tasks/change-requests/315-ajustar-botao-baixar-na-tabela-de-relatorios-web.md`
- `tasks/slices/011-relatorios-evolucao.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npx eslint src/pages/Main/Reports/index.tsx`: ok
- `cd front-end && npm run build`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir apenas se houver pedido para refinar outros CTAs da tabela de relatórios ou a distribuição visual das colunas

## Proximo contexto recomendado

- `front-end/src/pages/Main/Reports/index.tsx`
- `front-end/src/pages/Main/Reports/styles.module.css`
