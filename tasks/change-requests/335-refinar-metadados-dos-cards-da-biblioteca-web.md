# Task 335 - Refinar metadados dos cards da biblioteca web

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

- manter a linguagem editorial recente da biblioteca e refinar apenas a leitura dos metadados dos cards

## Objetivo

Melhorar a apresentação da linha de informações dos cards da biblioteca, substituindo o texto corrido por metadados visualmente mais bem resolvidos.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-334.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página biblioteca | `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | refinar os metadados dos cards | sim |
| Teste da rota | `front-end/src/pages/Main/Library/index.test.tsx` | revalidar comportamento | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: alterar apenas o bloco visual dos metadados dos cards de jogo

## Criterios de conclusao

- metadados dos cards deixam de parecer uma frase corrida
- categoria, dificuldade e idade ficam mais legíveis
- teste da página da biblioteca continua passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: os metadados dos cards da biblioteca passaram de texto corrido para chips compactos e mais legíveis.

### Relação com o slice

- refina o redesign editorial recente da biblioteca, concentrando o ajuste apenas na leitura visual dos cards de jogo.

### Decisões técnicas

- categoria, dificuldade e faixa etária passaram a ser renderizadas como pills independentes
- a mudança ficou restrita à rota `Library` e ao CSS local, sem alterar lógica ou dados do catálogo

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-334.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | refino visual dos cards | chips de metadados |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | reexecução da rota |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-335.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/335-refinar-metadados-dos-cards-da-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-335.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
