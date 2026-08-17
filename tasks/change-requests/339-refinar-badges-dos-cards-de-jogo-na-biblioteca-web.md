# Task 339 - Refinar badges dos cards de jogo na biblioteca web

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

- cards de jogo atuais da biblioteca

### Regra de aderencia visual

- manter o card atual, mas reposicionar a badge de status antes do título e compactar as badges de metadados com ícones

## Objetivo

Refinar o bloco de badges dos cards de jogo na biblioteca para melhorar hierarquia e legibilidade.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-338.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página biblioteca | `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | refinar badges do card | sim |
| Teste da rota | `front-end/src/pages/Main/Library/index.test.tsx` | validar rota | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar a mudança ao header e aos chips de metadados do card de jogo

## Criterios de conclusao

- badge de status aparece antes do título
- badges de metadados ficam menores, lado a lado e com ícones
- teste da biblioteca continua passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: a badge principal dos cards de jogo foi reposicionada antes do título e os chips de metadados ficaram menores, em linha e com ícones.

### Relação com o slice

- refina a leitura visual do catálogo jogável do Slice 006 sem alterar dados, fluxos ou permissões da biblioteca.

### Decisões técnicas

- o cabeçalho do card passou a usar uma linha flexível com badge e título no mesmo bloco visual
- os chips de metadados foram mantidos em linha, com tipografia menor e ícones dedicados por informação
- o refinamento foi aplicado tanto no card editável quanto no card somente leitura

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-338.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | refinar badges do card | estrutura e estilo do card |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | teste da rota |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-339.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `tasks/change-requests/339-refinar-badges-dos-cards-de-jogo-na-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-339.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
