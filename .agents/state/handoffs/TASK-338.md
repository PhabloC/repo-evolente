# Handoff - Task 338

## Task

- identificador: 338
- titulo: Corrigir quebra dos cards de jogos na biblioteca web
- tipo: front
- modo de execucao: single-stack
- status final: done

## Slice vertical

- identificador: Slice 006 - Catálogo de conteúdos master
- objetivo de negocio: impedir que os cards de jogos quebrem ou clipem no desktop
- entrega verificavel: cards estáveis com título, badge e ações legíveis
- status do slice: done

## Decisoes preservadas

- a correção ficou restrita ao CSS estrutural dos cards de jogo
- a grade voltou a reservar largura suficiente por card
- o header e o rodapé foram reorganizados para evitar disputa de espaço

## Contexto utilizado

### Contexto minimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/338-corrigir-quebra-dos-cards-de-jogos-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-337.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | corrigir quebra | layout do card |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | teste da rota |

## Resultado por stack

- front-end: cards de jogo estabilizados visualmente no desktop

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/338-corrigir-quebra-dos-cards-de-jogos-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`: ok

## Pendencias ou bloqueios

- nenhuma

## Proxima acao sugerida

- seguir só se quiser refinar microdetalhes do card sem mexer mais na estrutura

## Proximo contexto recomendado

- `front-end/src/pages/Main/Library/styles.module.css`
