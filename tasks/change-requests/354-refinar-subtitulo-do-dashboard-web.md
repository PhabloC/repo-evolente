# Task 354 - Refinar subtítulo do dashboard web

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

nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste visual orientado por referência enviada no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar o hero do dashboard e melhorar apenas a hierarquia do texto contextual abaixo do título

## Contexto de negocio

### Por que

O subtítulo do dashboard profissional estava funcional, mas visualmente simples demais para a importância do contexto e da data de atualização.

### O que

Transformar o subtítulo do dashboard em um bloco com texto principal e metadados visuais mais claros para o painel do dia e a última atualização.

### Comportamento esperado

- o dashboard mostra uma frase principal mais limpa sobre a rotina do profissional
- a última atualização fica destacada separadamente
- o header continua sem regressão estrutural ao aceitar subtítulos ricos

### Fora de escopo

- mudanças no restante dos cards do dashboard
- alteração das métricas ou da fonte de `lastUpdatedAt`
- redesign global do header

## Slice vertical

### Identificador do slice

Slice 017 - Redesign interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-353.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Header compartilhado | `front-end/src/layout/Header/index.tsx` e `styles.module.css` | permitir subtítulo rico sem quebra semântica | sim |
| Shell autenticado | `front-end/src/layout/MainLayout/index.tsx` | abrir a prop `subtitle` para `ReactNode` | sim |
| Dashboard | `front-end/src/pages/Main/ShellHome/index.tsx` e `styles.module.css` | compor o novo bloco visual do subtítulo | sim |
| Testes focados | `front-end/src/layout/Header/index.test.tsx`, `front-end/src/pages/Main/ShellHome/index.test.tsx` | validar estabilidade do header e do dashboard | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a mudança ao contrato de `subtitle` e ao dashboard profissional

## Criterios de conclusao

- [x] `MainLayout` e `Header` aceitam subtítulo rico
- [x] dashboard profissional exibe contexto principal e última atualização com melhor hierarquia
- [x] o header não mantém markup inválido para esse conteúdo
- [x] testes focados de header e dashboard passam

## Dependencias

- Task 347
- Task 353

## Resultado da execucao

- `subtitle` passou de `string` para `ReactNode` no shell compartilhado
- o subtítulo do dashboard foi reorganizado em frase principal, badge de contexto e badge de atualização
- o `Header` deixou de envolver o subtítulo em `<p>`, evitando nesting inválido quando o conteúdo é composto

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-353.md`

### Sob demanda

- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/styles.module.css`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`

### Contexto evitado

- outras páginas internas, por não precisarem de subtítulo rico nesta etapa
- `backend/` e `mobile/`, por não participarem do ajuste

## Handoff

- `.agents/state/handoffs/TASK-354.md`

## Arquivos alterados

- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/layout/Header/index.tsx`
- `front-end/src/pages/Main/ShellHome/index.tsx`
- `front-end/src/pages/Main/ShellHome/styles.module.css`
- `tasks/change-requests/354-refinar-subtitulo-do-dashboard-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-354.md`

## Validacoes executadas

- `cd front-end && npm test -- --run src/layout/Header/index.test.tsx src/pages/Main/ShellHome/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
