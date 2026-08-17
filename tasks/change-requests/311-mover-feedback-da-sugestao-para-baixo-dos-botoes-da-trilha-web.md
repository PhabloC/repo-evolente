# Task 311 - Mover feedback da sugestao para baixo dos botoes da trilha web

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

- nao se aplica; ajuste visual local na página da trilha

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre a página da trilha

### Cobertura

- posição do feedback visual da sugestão/local draft

### Lacunas

- sem novo mock detalhado; a tarefa deve apenas reposicionar o callout para baixo dos botões

## Objetivo

Reposicionar a mensagem de sugestão da anamnese para aparecer abaixo dos botões operacionais da semana.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-310.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | preservar semântica e escopo local | sim |
| Trilha web | `front-end/src/pages/Main/Plans/{PatientTrail/index.tsx,styles.module.css}` | reposicionar o feedback da sugestão | sim |

## Orçamento de contexto

- baixo
- estrategia: alterar apenas a marcação e o espaçamento local do bloco de feedback

## Criterios de conclusao

- [x] a mensagem de sugestão aparece abaixo dos botões
- [x] o bloco continua legível e coerente com o layout
- [x] a mudança fica restrita à página da trilha
- [x] validações focadas passam

## Dependencias

- Task 309 - done
- Task 310 - done

## Resultado da execucao

- o callout de feedback da sugestão deixou a coluna de status e passou a aparecer logo abaixo dos botões operacionais
- o bloco superior voltou a focar apenas no status e no suporte textual da semana
- a mudança ficou isolada na composição da página da trilha

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-310.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/{PatientTrail/index.tsx,styles.module.css}`

### Contexto evitado

- `contracts/openapi.yaml`, porque não houve alteração de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao visual da trilha web

## Handoff

- `.agents/state/handoffs/TASK-311.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/styles.module.css`
- `tasks/change-requests/311-mover-feedback-da-sugestao-para-baixo-dos-botoes-da-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-311.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
