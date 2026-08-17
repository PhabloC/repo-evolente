# Task 349 - Reposicionar ações da trilha do paciente abaixo do header

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

ajuste orientado por feedback do usuario no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`
- print da página da trilha enviado no chat em 2026-07-29

### Regra de aderencia visual

- preservar o shell autenticado e mover apenas as ações da trilha do paciente para baixo do heading

## Contexto de negocio

### Por que

Na página da trilha do paciente, os botões `Voltar` e `Perfil do paciente` passaram a quebrar o header e comprimir o bloco de título.

### O que

Aplicar também nessa rota a variante de layout que posiciona as ações em uma segunda linha abaixo do heading.

### Comportamento esperado

- as ações da trilha aparecem abaixo do heading
- busca e notificações continuam no topo do shell
- o conteúdo da semana permanece inalterado

### Fora de escopo

- mudanças de backend
- mudanças na grade semanal, progresso ou persistência da trilha
- alteração global de todos os headers

## Slice vertical

### Identificador do slice

Slice 017 - Redesign da interface interna web

### Arquivo do slice

- `tasks/slices/017-redesign-interface-interna-web.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-348.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | preservar semântica e consistência estrutural | sim |
| Header compartilhado | `front-end/src/layout/Header/index.tsx` e `front-end/src/layout/MainLayout/index.tsx` | reutilizar a variante de layout existente | sim |
| Página da trilha | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` e `index.test.tsx` | ativar e validar o layout abaixo do heading | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: reutilizar a variante já introduzida e limitar a mudança à página da trilha

## Criterios de conclusao

- [x] ações da trilha renderizam abaixo do heading
- [x] busca e notificações permanecem no topo do shell
- [x] teste focado passa
- [x] lint dos arquivos alterados passa

## Dependencias

- Task 346
- Task 348

## Resultado da execucao

- a rota da trilha do paciente passou a usar `actionsLayout="below-heading"`
- o teste da página agora valida a presença do contêiner de ações abaixo do heading

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-348.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`
- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integração
- `backend/` e `mobile/` por estarem fora do escopo
- outras páginas sem regressão reportada

## Handoff

- `.agents/state/handoffs/TASK-349.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `tasks/change-requests/349-reposicionar-acoes-da-trilha-do-paciente-abaixo-do-header.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-349.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/layout/Header/index.test.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/MainLayout/index.tsx src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
