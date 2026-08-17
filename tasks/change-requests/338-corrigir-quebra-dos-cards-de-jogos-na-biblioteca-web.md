# Task 338 - Corrigir quebra dos cards de jogos na biblioteca web

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

- print de tela

### Fonte primaria visual

- print enviado no chat em `2026-07-29` mostrando os cards quebrados

### Regra de aderencia visual

- preservar a linguagem recente dos cards de jogo, mas corrigir largura, badge e rodapé para evitar clipping e quebras ruins

## Objetivo

Corrigir os cards de jogos da biblioteca para que não estourem ou quebrem o layout no desktop.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-337.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página biblioteca | `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | corrigir o card | sim |
| Teste da rota | `front-end/src/pages/Main/Library/index.test.tsx` | validar que a rota segue íntegra | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: restringir a mudança à responsividade e à composição do card de jogo

## Criterios de conclusao

- cards deixam de quebrar visualmente
- título, badge e ações permanecem legíveis
- teste da página da biblioteca continua passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: os cards de jogos da biblioteca deixaram de quebrar no desktop após ajuste de largura mínima, header e rodapé de ações.

### Relação com o slice

- corrige a apresentação dos cards dentro do Slice 006 sem reabrir comportamento, dados ou interações do catálogo.

### Decisões técnicas

- a grade passou a reservar mais largura por card
- o badge saiu da disputa horizontal com o título
- o rodapé virou uma grade estável de três ações, evitando clipping

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-337.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | corrigir quebra | CSS estrutural do card |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | teste da rota |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-338.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/338-corrigir-quebra-dos-cards-de-jogos-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-338.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
