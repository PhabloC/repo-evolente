# Task 337 - Aproximar cards de jogos da biblioteca da referência web

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

- referência enviada no chat em `2026-07-29` para o card de jogo "Caça-palavras"

### Regra de aderencia visual

- aproximar os cards de jogo da biblioteca ao card de referência, com destaque maior da capa, bloco branco inferior, badge de status no topo do conteúdo e ações distribuídas no rodapé

## Objetivo

Deixar os cards dos jogos da biblioteca com visual mais próximo da referência enviada, mantendo o comportamento atual da página.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-336.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página biblioteca | `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | refinar o card de jogo | sim |
| Teste da rota | `front-end/src/pages/Main/Library/index.test.tsx` | revalidar comportamento | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: restringir a mudança ao markup e CSS dos cards de jogo

## Criterios de conclusao

- cards de jogo ficam visualmente mais próximos da referência
- ações continuam legíveis e clicáveis
- teste da página da biblioteca continua passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: os cards de jogos da biblioteca foram aproximados do card de referência, com capa dominante, painel inferior branco, badge de status no topo do conteúdo e ações visuais no rodapé.

### Relação com o slice

- refina a biblioteca dentro do Slice 006 sem alterar os fluxos do catálogo, apenas a composição visual dos cards de jogo.

### Decisões técnicas

- o card passou a ser dividido entre área de arte/capa e painel inferior de conteúdo
- as ações ganharam rótulos visuais para ficar mais próximas do print de referência
- a mudança ficou contida em `Library/index.tsx` e `Library/styles.module.css`

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-336.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | aproximação visual do card | markup e CSS |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | teste da rota |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-337.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/337-aproximar-cards-de-jogos-da-biblioteca-da-referencia-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-337.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
