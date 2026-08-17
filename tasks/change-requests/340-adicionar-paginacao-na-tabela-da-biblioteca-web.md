# Task 340 - Adicionar paginação na tabela da biblioteca web

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

- tabela editorial atual da biblioteca

### Regra de aderencia visual

- manter a tabela atual e aplicar o padrão compacto de paginação já usado em pacientes e planejamentos

## Objetivo

Adicionar paginação local na tabela de áudio e vídeo da biblioteca para reduzir a altura do bloco editorial e melhorar a navegação pelo catálogo.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-339.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Página biblioteca | `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | implementar paginação local na tabela | sim |
| Padrão visual existente | `front-end/src/pages/Main/Patients/index.tsx` e `front-end/src/pages/Main/Patients/styles.module.css` | reaproveitar padrão de paginação web | sim |
| Teste da rota | `front-end/src/pages/Main/Library/index.test.tsx` | validar comportamento da biblioteca | sim |

## Orçamento de contexto

- Risco baixo
- Estratégia: limitar a mudança ao bloco da tabela editorial e ao teste da rota

## Criterios de conclusao

- tabela de áudio e vídeo passa a renderizar subconjunto paginado dos itens
- navegação exibe resumo `Mostrando x-y de n conteúdos`
- mudança preserva ações existentes da tabela
- teste da biblioteca continua passando

## Validacao esperada

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx`

## Resultado da execucao

### Resumo por stack

- **front-end**: a tabela editorial da biblioteca ganhou paginação local com resumo de faixa visível e navegação compacta entre páginas.

### Relação com o slice

- refina a navegação do catálogo editorial do Slice 006 sem alterar permissões, contratos ou fluxos de criação/edição.

### Decisões técnicas

- a paginação foi aplicada apenas aos conteúdos não jogáveis, preservando os cards de jogos no topo
- o padrão visual reutiliza a barra compacta já consolidada em outras tabelas web do projeto
- a página atual é reajustada automaticamente quando o catálogo filtrado muda de tamanho

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/006-catalogo-conteudos-master.md`
- `.agents/state/handoffs/TASK-339.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/src/pages/Main/Library/{index.tsx,styles.module.css}` | paginação da tabela editorial | estado, recorte de itens e barra visual |
| `front-end/src/pages/Main/Patients/{index.tsx,styles.module.css}` | padrão visual existente | referência para resumo e navegação |
| `front-end/src/pages/Main/Library/index.test.tsx` | validação | cobertura da rota |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-340.md`

## Arquivos alterados

- `front-end/src/pages/Main/Library/index.tsx`
- `front-end/src/pages/Main/Library/styles.module.css`
- `front-end/src/pages/Main/Library/index.test.tsx`
- `tasks/change-requests/340-adicionar-paginacao-na-tabela-da-biblioteca-web.md`
- `tasks/slices/006-catalogo-conteudos-master.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-340.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Library/index.test.tsx` — ok

## Pendencias pos-task

- nenhuma bloqueante

## Status final

done
