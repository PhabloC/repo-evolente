# Task 588 - Consultas presenciais e timeline no perfil do paciente

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET/POST/PATCH /patients/{patientId}/in-person-consultations`.

## Modo de execucao

cross-stack

## Slice vertical

- Slice 053 — `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Contexto mínimo

- Índice, task, perfil profissional do paciente e autorização de patients.

## Contexto sob demanda

- Entidades/repositórios/migrations de backend, OpenAPI, serviço de pacientes e componentes do perfil web.

## Orçamento de contexto

- médio.

## Estratégia de redução

- Entrega somente web profissional; responsável e mobile ficam fora de escopo.

## Resultado da execucao

- Backend passou a expor e validar o histórico de consultas presenciais por profissional no perfil do paciente, com criação, edição, listagem e remoção.
- O perfil web do profissional ganhou timeline filtrável por status e intervalo de datas, com utilitário dedicado para manter a regra fora da page.
- O contrato OpenAPI foi completado para os endpoints de consultas presenciais, incluindo parâmetros, payloads e responses.
- A suíte de testes foi ampliada para cobrir o fluxo de consultas no backend e a regra de timeline no front-end.
- A validação expôs e corrigiu um bug real: vínculos `inactive` voltavam a falhar no retorno do `updateStatus` por causa da guarda de acesso.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`
- `backend/AGENTS.md`
- `backend/docs/ai/AGENTS.md`
- `front-end/AGENTS.md`
- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `contracts/openapi.yaml` (paths e schemas de pacientes/consultas)
- `backend/src/modules/patients/*`
- `front-end/src/pages/Main/Patients/PatientProfile/*`
- `front-end/src/pages/Main/Patients/utils/*`

## Handoff

- Handoff atualizado em `.agents/state/handoffs/TASK-588.md`.

## Arquivos alterados

- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/patients/patients.service.spec.ts`
- `contracts/openapi.yaml`
- `front-end/src/types/patient.ts`
- `front-end/src/services/patients/patientService.ts`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/utils/inPersonConsultations.ts`
- `front-end/src/pages/Main/Patients/utils/inPersonConsultations.test.ts`
- `front-end/src/pages/Main/Admin/buildAdminDashboardCharts.ts`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Guardian/ChildProfile/index.test.tsx`
- `front-end/src/pages/Main/Guardian/ChildRegister/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`
- `front-end/src/pages/Main/ShellHome/index.test.tsx`
- `front-end/src/services/dashboard/buildDashboardPanels.ts`

## Validacoes executadas

- `backend`: `npx jest src/modules/patients/patients.service.spec.ts --runInBand`
- `backend`: `npm run lint`
- `backend`: `npm run build`
- `front-end`: `npx vitest run src/pages/Main/Patients/utils/inPersonConsultations.test.ts --pool=threads --maxWorkers=1`
- `front-end`: `npm run lint`
- `front-end`: `npm run build`

## Pendencias pos-task

- Nenhuma dentro do escopo desta task.

## Status final

done
