# Task 336 - Reduzir cards dos jogos na biblioteca web

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

artefato documental

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- manter a linguagem editorial recente da biblioteca, apenas reduzindo a escala visual dos cards dos jogos

## Objetivo

Diminuir os cards dos jogos na página da biblioteca para reduzir peso visual e aumentar a sensação de catálogo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-335.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página biblioteca | `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | reduzir a escala dos cards | sim |
| Teste da rota | `front-end/src/pages/Main/Library/index.test.tsx` | revalidar comportamento | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: alterar apenas grid, preview e espaçamentos dos cards de jogo

## Criterios de conclusao

- cards dos jogos ficam menores
- leitura e ações continuam legíveis
- teste da página da biblioteca continua passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: os cards dos jogos na biblioteca ficaram menores e mais leves visualmente, reforçando a sensação de catálogo.

### Relação com o slice

- refina a composição editorial recente da biblioteca, reduzindo apenas a escala dos cards de jogo.

### Decisões técnicas

- a redução ficou concentrada em `grid`, `preview`, `padding`, tipografia e chips dos cards
- nenhuma semântica, ação ou agrupamento do catálogo foi alterado

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-335.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | redução da escala | ajuste dos cards |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | reexecução da rota |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-336.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/336-reduzir-cards-dos-jogos-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-336.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
