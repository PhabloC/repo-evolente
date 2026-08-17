# Task 342 - Encostar capa dos jogos nas bordas do card

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

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 006 - Catálogo de conteúdos master
- `tasks/slices/006-catalogo-conteudos-master.md`

## Referencia visual

### Stack de referencia visual

- front-end

### Tipo de referencia visual

- refinamento incremental solicitado via chat

### Fonte primaria visual

- cards atuais de jogo da biblioteca

### Regra de aderencia visual

- manter o card atual, mas fazer a imagem encostar nas laterais e no topo interno do card

## Objetivo

Ajustar o card dos jogos da biblioteca para que a capa ocupe toda a largura útil no topo, sem respiro lateral nem superior.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-341.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Card de jogo | `front-end/src/pages/Main/Library/styles.module.css` | ajustar encaixe da capa | sim |
| Rota biblioteca | `front-end/src/pages/Main/Library/index.test.tsx` | revalidar regressão | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar a mudança ao CSS estrutural do card de jogo

## Criterios de conclusao

- a capa do jogo encosta nas laterais e no topo do card
- o restante do conteúdo do card permanece íntegro
- teste da biblioteca continua passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: os cards de jogo da biblioteca passaram a renderizar a capa encostada nas laterais e no topo, sem a moldura interna anterior.

### Relação com o slice

- refina a composição visual do catálogo jogável no Slice 006 sem alterar fluxos, dados ou permissões.

### Decisões técnicas

- o padding estrutural externo do card foi removido
- o espaçamento visual passou a ficar concentrado apenas no painel de conteúdo inferior
- a capa preserva o recorte arredondado superior por meio do próprio container com `overflow: hidden`

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-341.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/styles.module.css` | encaixe da capa | ajuste estrutural do card |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | regressão da rota |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-342.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/342-encostar-capa-dos-jogos-nas-bordas-do-card.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-342.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
