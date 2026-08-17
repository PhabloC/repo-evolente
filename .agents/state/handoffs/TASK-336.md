# Handoff - Task 336

## Task

- identificador: 336
- titulo: Reduzir cards dos jogos na biblioteca web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catálogo de conteúdos master
- objetivo de negocio: deixar a grade de jogos da biblioteca mais compacta e com leitura melhor de catálogo
- entrega verificavel: cards menores, preview menor e metadados mais compactos
- status do slice: done

## Decisoes preservadas

- a redução ficou restrita ao CSS local dos cards de jogo
- a grade passou a usar largura menor por card e espaçamentos internos mais compactos
- nenhum fluxo, texto ou ação da biblioteca foi alterado

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/336-reduzir-cards-dos-jogos-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-335.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | ajuste de escala | redução dos cards |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | teste da rota |

## Resultado por stack

- front-end: cards dos jogos menores e mais leves visualmente na biblioteca

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/336-reduzir-cards-dos-jogos-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir só se quiser compactar também o hero ou a tabela editorial da biblioteca

## Proximo contexto recomendado

- `front-end/src/pages/Main/Library/styles.module.css`
