# Task 593 - Exibir falha de consultas no perfil do paciente web

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

- Sem alteracao de contrato; consumo existente de `GET /patients/{patientId}/in-person-consultations`.

## Modo de execucao

single-stack

## Slice vertical

- Slice 053 - `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Contexto mínimo

- Indice, Slice 053, Task 588 e perfil web do paciente.

## Contexto sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`, para estados de carregamento e erro do painel.

## Orçamento de contexto

- baixo; limitar a timeline de consultas e seu teste.

## Estratégia de redução

- Sem tocar em CRUD ou contrato: apenas separar vazio, carregamento e erro com retry.

## Resultado da execucao

- Falhas da API de consultas deixam de ser mascaradas como historico vazio e passam a oferecer nova tentativa.

## Contexto utilizado

- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`

## Handoff

- `.agents/state/handoffs/TASK-593.md`

## Arquivos alterados

- Perfil do paciente web.

## Validacoes executadas

- Vitest direcionado e build do front-end.

## Pendencias pos-task

- Nenhuma.

## Status final

done
