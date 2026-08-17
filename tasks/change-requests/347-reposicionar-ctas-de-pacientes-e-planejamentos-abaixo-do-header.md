# Task 347 - Reposicionar CTAs de pacientes e planejamentos abaixo do header

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
- feedback visual do usuario em 2026-07-29

### Regra de aderencia visual

- preservar o shell autenticado e mover apenas os CTAs principais das rotas `/pacientes` e `/planejamentos` para baixo do heading

## Contexto de negocio

### Por que

As páginas de pacientes e planejamentos passaram a sofrer a mesma quebra visual já observada no dashboard profissional, comprimindo o bloco de heading.

### O que

Aplicar a variante de layout do header já criada para posicionar os CTAs dessas duas páginas em uma segunda linha abaixo do heading.

### Comportamento esperado

- a página de pacientes mantém o CTA `Vincular por código` abaixo do heading
- a página de planejamentos mantém o CTA `Ver pacientes` abaixo do heading
- busca e notificações continuam no topo do shell
- outras páginas preservam o comportamento atual

### Fora de escopo

- alteração de regras de negócio
- alteração global de todos os headers do produto
- mudanças em backend ou mobile

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
- `.agents/state/handoffs/TASK-346.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | preservar semântica, reuso e isolamento do ajuste | sim |
| Header compartilhado | `front-end/src/layout/Header/{index.tsx,index.test.tsx}` e `front-end/src/layout/MainLayout/index.tsx` | reutilizar a variante de layout existente | sim |
| Páginas consumidoras | `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx}` e `front-end/src/pages/Main/Plans/{index.tsx,index.test.tsx}` | ativar e validar o layout abaixo do heading | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: reutilizar a variante já introduzida no header e limitar a mudança às duas rotas consumidoras

## Criterios de conclusao

- [x] CTA de pacientes renderiza abaixo do heading
- [x] CTA de planejamentos renderiza abaixo do heading
- [x] busca e notificações permanecem no topo do shell
- [x] testes focados passam
- [x] lint dos arquivos alterados passa

## Dependencias

- Task 308
- Task 346

## Resultado da execucao

- a rota `/pacientes` passou a usar `actionsLayout="below-heading"`
- a rota `/planejamentos` passou a usar `actionsLayout="below-heading"`
- os testes dessas duas páginas agora validam a presença do contêiner de ações abaixo do heading

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-346.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`
- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/Header/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integração
- `backend/` e `mobile/` por estarem fora do escopo
- páginas que não apresentaram a regressão no chat

## Handoff

- `.agents/state/handoffs/TASK-347.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`
- `tasks/change-requests/347-reposicionar-ctas-de-pacientes-e-planejamentos-abaixo-do-header.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-347.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/layout/Header/index.test.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/Header/index.test.tsx src/layout/MainLayout/index.tsx src/pages/Main/Patients/index.tsx src/pages/Main/Patients/index.test.tsx src/pages/Main/Plans/index.tsx src/pages/Main/Plans/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
