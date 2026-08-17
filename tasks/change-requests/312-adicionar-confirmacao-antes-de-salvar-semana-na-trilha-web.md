# Task 312 - Adicionar confirmacao antes de salvar semana na trilha web

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

- nao se aplica; ajuste de UX local na página da trilha

## Modo de execucao

single-stack

## Slice vertical

- Slice 017 - Redesign da interface interna web
- `tasks/slices/017-redesign-interface-interna-web.md`

## Referencia visual

### Tipo

feedback direto do usuario sobre o fluxo da trilha

### Cobertura

- ação `Salvar semana`
- confirmação antes de persistir a trilha

### Lacunas

- sem mock novo; a tarefa deve reutilizar o padrão de modal já presente na própria página

## Objetivo

Exigir uma confirmação explícita antes de salvar a semana na trilha da criança.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-311.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/{ACCESSIBILITY.md,COMPONENT_REUSE.md}` | preservar semântica, foco e escopo local | sim |
| Trilha web | `front-end/src/pages/Main/Plans/PatientTrail/{index.tsx,index.test.tsx}` | adicionar modal de confirmação no salvamento | sim |

## Orçamento de contexto

- baixo
- estrategia: reaproveitar o componente `Modal` e o padrão de confirmação já existente na página

## Criterios de conclusao

- [x] clicar em `Salvar semana` abre um modal de confirmação
- [x] a persistência só acontece após confirmação explícita
- [x] cancelar fecha o modal sem salvar
- [x] o dirty state do botão continua respeitado
- [x] validações focadas passam

## Dependencias

- Task 309 - done
- Task 311 - done

## Resultado da execucao

- a ação `Salvar semana` passou a abrir um modal de confirmação antes de persistir a trilha
- a gravação da semana foi encapsulada em uma ação confirmada, preservando o mesmo fluxo de sugestão/local draft e trilha manual
- o modal reutilizou o padrão visual já usado para confirmação de inativação na própria página

## Contexto utilizado

### Mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/017-redesign-interface-interna-web.md`
- `.agents/state/handoffs/TASK-311.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/docs/ai/COMPONENT_REUSE.md`
- `front-end/src/pages/Main/Plans/PatientTrail/{index.tsx,index.test.tsx}`

### Contexto evitado

- `contracts/openapi.yaml`, porque nao houve alteração de contrato
- `backend/` e `mobile/`, porque o ajuste ficou restrito ao fluxo web da trilha

## Handoff

- `.agents/state/handoffs/TASK-312.md`

## Arquivos alterados

- `front-end/src/pages/Main/Plans/PatientTrail/index.tsx`
- `front-end/src/pages/Main/Plans/PatientTrail/index.test.tsx`
- `tasks/change-requests/312-adicionar-confirmacao-antes-de-salvar-semana-na-trilha-web.md`
- `tasks/slices/017-redesign-interface-interna-web.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-312.md`

## Validacoes executadas

- `cd front-end && npm run test -- --run src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Plans/PatientTrail/index.tsx src/pages/Main/Plans/PatientTrail/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
