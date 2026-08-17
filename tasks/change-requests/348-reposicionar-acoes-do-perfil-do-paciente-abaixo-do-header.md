# Task 348 - Reposicionar ações do perfil do paciente abaixo do header

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
- print do perfil do paciente enviado no chat em 2026-07-29

### Regra de aderencia visual

- preservar o shell autenticado e mover apenas o conjunto de ações do perfil do paciente para baixo do heading

## Contexto de negocio

### Por que

O perfil do paciente passou a sofrer a mesma quebra visual do header, com os botões `Voltar à lista`, `Inativar` e `Montar trilha` comprimindo o bloco de heading.

### O que

Aplicar no perfil do paciente a variante de layout já usada no dashboard, em pacientes e em planejamentos, posicionando as ações em uma segunda linha abaixo do heading.

### Comportamento esperado

- as ações do perfil do paciente aparecem abaixo do heading
- busca e notificações continuam no topo do shell
- o restante da página permanece inalterado

### Fora de escopo

- mudanças de backend
- mudanças no conteúdo clínico da página
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
- `.agents/state/handoffs/TASK-347.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | preservar semântica e consistência estrutural | sim |
| Header compartilhado | `front-end/src/layout/Header/index.tsx` e `front-end/src/layout/MainLayout/index.tsx` | reutilizar a variante de layout existente | sim |
| Perfil do paciente | `front-end/src/pages/Main/Patients/PatientProfile/index.tsx` e `index.test.tsx` | ativar e validar o layout abaixo do heading | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: reutilizar a variante já introduzida e limitar a mudança ao perfil do paciente

## Criterios de conclusao

- [x] ações do perfil do paciente renderizam abaixo do heading
- [x] busca e notificações permanecem no topo do shell
- [x] teste focado passa
- [x] lint dos arquivos alterados passa

## Dependencias

- Task 346
- Task 347

## Resultado da execucao

- a rota de perfil do paciente passou a usar `actionsLayout="below-heading"`
- foi adicionado um teste focado para garantir a renderização das ações abaixo do heading

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-347.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`
- `front-end/src/layout/Header/index.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver integração
- `backend/` e `mobile/` por estarem fora do escopo
- páginas sem regressão reportada

## Handoff

- `.agents/state/handoffs/TASK-348.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`
- `tasks/change-requests/348-reposicionar-acoes-do-perfil-do-paciente-abaixo-do-header.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-348.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/layout/Header/index.test.tsx src/pages/Main/Patients/PatientProfile/index.test.tsx` - ok
- `cd front-end && npx eslint src/layout/Header/index.tsx src/layout/MainLayout/index.tsx src/pages/Main/Patients/PatientProfile/index.tsx src/pages/Main/Patients/PatientProfile/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
