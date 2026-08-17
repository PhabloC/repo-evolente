# Handoff - Task 342

## Task

- identificador: 342
- titulo: Encostar capa dos jogos nas bordas do card
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catálogo de conteúdos master
- objetivo de negocio: aproximar o card de jogo da referência visual esperada
- entrega verificavel: capa encostada nas laterais e no topo do card
- status do slice: done

## Decisoes preservadas

- a mudança ficou restrita ao CSS do card de jogo
- a imagem passou a ocupar o topo útil inteiro do card
- o espaçamento do conteúdo textual continua no painel inferior

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/342-encostar-capa-dos-jogos-nas-bordas-do-card.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-341.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/styles.module.css` | encaixe da capa | ajuste estrutural do card |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | regressão da rota |

## Resultado por stack

- front-end: cards de jogo com capa colada no topo e nas laterais do card

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/342-encostar-capa-dos-jogos-nas-bordas-do-card.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-342.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- validar visualmente se o painel inferior ainda tem o respiro desejado em cards com capa alta

## Proximo contexto recomendado

- `front-end/src/pages/Main/Library/styles.module.css`
