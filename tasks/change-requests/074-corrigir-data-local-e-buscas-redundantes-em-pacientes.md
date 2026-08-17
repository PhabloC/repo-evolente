# Task 074 - Corrigir data local e buscas redundantes em pacientes

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

- nao se aplica; sem alteracao de integracao

## Modo de execucao

single-stack

## Slice vertical

- Slice 007 - Gestao de pacientes do profissional
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Objetivo

Corrigir a exibicao de datas puras no fuso local e remover buscas redundantes no menu de acoes da listagem de pacientes.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-051.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | preservar padroes locais do front-end | sim |
| Perfil/listagem | `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`, `front-end/src/pages/Main/Patients/index.tsx` | corrigir data e simplificar o portal de ações | sim |
| Utilitarios | `front-end/src/utils/**` | extrair helper se houver regra reutilizavel | nao |

## Orçamento de contexto

- baixo
- estrategia: restringir a alteracao ao modulo `Patients`, sem tocar contrato nem backend

## Criterios de conclusao

- [ ] datas `YYYY-MM-DD` do perfil do paciente nao sofrem deslocamento de fuso na exibicao
- [ ] menu de acoes da listagem resolve o paciente ativo apenas uma vez por render do portal
- [ ] comportamento visual e acessibilidade do modulo permanecem intactos
- [ ] validacoes focadas do front-end executadas

## Dependencias

- Task 051 - done
- Task 068 - done

## Resultado da execucao

- a formatacao de datas do perfil do paciente passou a tratar strings `YYYY-MM-DD` como data local, evitando o atraso de um dia em fusos negativos
- a regra de parse foi extraida para utilitario compartilhado em `src/utils`
- o portal do menu de ações da listagem passou a resolver o paciente ativo apenas uma vez por render, removendo buscas repetidas no array paginado

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/007-gestao-pacientes-profissional.md`
- `.agents/state/handoffs/TASK-051.md`

### Sob demanda

- `front-end/docs/ai/ARCHITECTURE.md`, `front-end/docs/ai/CODE_STYLE.md`, `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/utils/age.ts`
- `front-end/src/utils/parseDateValue.ts`
- `front-end/src/utils/parseDateValue.test.ts`

## Handoff

- `.agents/state/handoffs/TASK-074.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/utils/parseDateValue.ts`
- `front-end/src/utils/parseDateValue.test.ts`
- `tasks/change-requests/074-corrigir-data-local-e-buscas-redundantes-em-pacientes.md`
- `tasks/slices/007-gestao-pacientes-profissional.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-074.md`

## Validacoes executadas

- `cd front-end && npm run test -- src/utils/parseDateValue.test.ts src/pages/Main/Patients/index.test.tsx` - ok
- `cd front-end && npm run lint` - ok
- `cd front-end && npm run build` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
