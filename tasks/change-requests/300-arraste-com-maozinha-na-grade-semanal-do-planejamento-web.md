# Task 300 - Arraste com mãozinha na grade semanal do planejamento web

## Status

in_progress

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- nao se aplica; ajuste de interação no scroll horizontal da grade semanal

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre affordance e gesto de rolagem

### Cobertura

- região de scroll horizontal da grade semanal na tela de trilha do paciente

### Lacunas

- sem novo print; a mudança deve reaproveitar a grade semanal recém-ajustada e acrescentar gesto de arraste com cursor de mão

## Objetivo

Permitir arrastar horizontalmente a grade semanal com cursor de mãozinha, reforçando a descoberta e a usabilidade do scroll lateral.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-299.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | validar interação por mouse e manter escopo mínimo | sim |
| Planejamento | `front-end/src/pages/Main/Plans/PatientTrail/index.tsx` | adicionar gesto de arraste horizontal | sim |
| Estilo | `front-end/src/pages/Main/Plans/styles.module.css` | aplicar cursor `grab/grabbing` e estado visual | sim |
| Teste | `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx` | cobrir o arraste horizontal no contêiner | sim |

## Orçamento de contexto

- baixo
- estrategia: evoluir apenas o contêiner de scroll da Task 299, sem alterar regra de negócio ou outros cards

## Criterios de conclusao

- [x] a região da grade semanal exibe cursor de mão apropriado para arraste
- [x] o usuário consegue arrastar horizontalmente a grade com o mouse
- [x] validações focadas passam

## Dependencias

- Task 299 - done

## Resultado da execucao

- a região de scroll horizontal da grade semanal passou a exibir cursor `grab`, mudando para `grabbing` durante o arraste
- foi adicionado gesto de arraste horizontal com mouse na grade semanal, reaproveitando o contêiner criado na Task 299
- a lógica ignora elementos interativos internos, preservando clique normal em botões e controles dos cards

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-299.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/index.test.tsx`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteração de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito à interação web da grade semanal
- outras rotas internas, porque a mudança foi localizada na tela de trilha do paciente

## Handoff

- `.agents/state/handoffs/TASK-300.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/300-arraste-com-maozinha-na-grade-semanal-do-planejamento-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-300.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx src/pages/Main/Plans/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done

## Status

done
