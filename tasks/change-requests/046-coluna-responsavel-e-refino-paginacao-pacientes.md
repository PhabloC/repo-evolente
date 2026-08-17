# Task 046 - Coluna de responsável e refino da paginação em pacientes

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1patients/get`
- `contracts/openapi.yaml#/components/schemas/PatientListItem`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 007 - Gestao de pacientes do profissional
- `tasks/slices/007-gestao-pacientes-profissional.md`

## Referencia visual

### Tipo

ajuste incremental solicitado no chat

### Cobertura

- paginação com navegação mais compacta
- tabela de pacientes com coluna adicional de responsável

### Lacunas

- sem print dedicado da tabela com responsável
- decisao: manter a coluna nova em formato textual simples, coerente com a densidade atual da tabela

## Objetivo

Refinar a paginação da listagem de pacientes e acrescentar a coluna de responsável usando dado real do backend.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 007 e `.agents/state/handoffs/TASK-045.md`

## Contexto sob demanda

- `front-end/docs/ai/{AGENTS.md,ACCESSIBILITY.md}`
- `backend/docs/ai/AGENTS.md`
- `contracts/openapi.yaml`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/patients/patients.service.spec.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/types/patient.ts`

## Orçamento de contexto

- medio; limitado ao slice de pacientes, contrato do endpoint de listagem e renderização da tabela

## Criterios de conclusao

- [x] paginação usa setas em vez de rótulos longos e números com visual menor
- [x] `/patients` retorna responsável em cada item da listagem
- [x] tabela de pacientes exibe a nova coluna com dado real
- [x] contrato OpenAPI e tipos do front refletem o campo novo
- [x] lint/testes das stacks afetadas aprovados

## Resultado da execucao

- a paginação ficou mais compacta com setas e números menores
- o backend passou a incluir um resumo do responsável em cada item de `/patients`
- a tabela de pacientes ganhou a coluna `Responsável`
- contrato, tipos e testes foram atualizados para cobrir o novo campo

## Contexto utilizado

- fontes globais, Slice 007, handoff 045, docs locais de front/backend, contrato OpenAPI, service de pacientes e página de pacientes

## Handoff

- `.agents/state/handoffs/TASK-046.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/{guardians/guardians.service.ts,patients/patients.service.ts,patients/patients.service.spec.ts}`
- `front-end/src/pages/Main/Patients/{index.tsx,index.test.tsx,styles.module.css}`
- `front-end/src/types/patient.ts`
- task, slice, índice e handoff

## Validacoes executadas

- `cd backend && npm run test -- patients.service.spec.ts`
- `cd front-end && npm run lint`
- `cd front-end && npm run test -- --run src/pages/Main/Patients/index.test.tsx`

## Pendencias pos-task

- nenhuma

## Status final

done
