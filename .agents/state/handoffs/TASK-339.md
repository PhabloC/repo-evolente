# Handoff - Task 339

## Task

- identificador: 339
- titulo: Refinar badges dos cards de jogo na biblioteca web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catálogo de conteúdos master
- objetivo de negocio: melhorar a leitura do cabeçalho e dos metadados dos cards de jogo
- entrega verificavel: badge principal antes do título e chips menores com ícones
- status do slice: done

## Decisoes preservadas

- a badge principal ficou no mesmo bloco visual do título, antes do nome da atividade
- os metadados foram mantidos em linha com tipografia menor para reduzir peso visual
- o refinamento foi espelhado nos cards editáveis e somente leitura

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/339-refinar-badges-dos-cards-de-jogo-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-338.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | refinar badges | componente e CSS do card |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | teste da rota |

## Resultado por stack

- front-end: cards de jogo com status/trilha antes do título e chips mais compactos com ícones

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/339-refinar-badges-dos-cards-de-jogo-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-339.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- validar visualmente no navegador se a ordem e o respiro das badges atendem ao estilo final desejado

## Proximo contexto recomendado

- `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}`
