# Task 602 - Exibir status da assinatura do responsável no perfil profissional

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end
- contracts

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /patients`
- `GET /patients/{patientId}`
- schemas `PatientGuardianSummary`, `PatientListItem` e `PatientDetail` em `contracts/openapi.yaml`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 053 - Vínculos múltiplos de profissionais e aprovação
- `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`

## Objetivo

Permitir que o profissional veja, no perfil do paciente, se o responsável vinculado tem acesso por assinatura. O estado deve refletir o cancelamento do responsável na próxima carga dos dados, sem alterar o vínculo clínico.

## Dependências

- Task 561 — done
- Task 588 — done
- Task 599 — done

## Contexto mínimo

- esta task
- `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`
- `.agents/state/handoffs/TASK-588.md`
- `contracts/openapi.yaml` (schemas de pacientes)
- `backend/src/modules/patients/patients.service.ts`
- `front-end/src/types/patient.ts`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Obter estado de acesso | `backend/src/modules/guardians/guardians.service.ts` | incluir o booleano de acesso no resumo do responsável |
| Cobertura backend | `backend/src/modules/patients/patients.service.spec.ts` | validar listagem e detalhe com o novo campo |
| UI web | `front-end/docs/ai/ACCESSIBILITY.md`, `design-system/front/Design_System_Evolente_Desktop.md` | exibir estado textual e visual acessível no perfil |
| Cobertura web | `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx` | validar a exibição do status |

## Orçamento de contexto

- médio
- estratégia: um campo booleano já persistido no perfil do responsável, exposto somente às rotas de pacientes do profissional e renderizado apenas no perfil web; sem polling, eventos em tempo real, mobile ou mudança de autorização.

## Critérios de aceite

- [x] O contrato retorna `subscriptionAccessGranted` no resumo do responsável em lista e detalhe de paciente.
- [x] Após o cancelamento, uma nova carga do perfil do paciente mostra `Assinatura sem acesso`.
- [x] Com acesso ativo, o perfil mostra `Assinatura ativa`.
- [x] O vínculo e as permissões do profissional não são removidos nem bloqueados.
- [x] Backend e web possuem validação focada para o novo comportamento.

## Fora de escopo

- Bloquear ou remover vínculos clínicos.
- Atualização em tempo real/push sem recarregar a página.
- Alterações na área do responsável, mobile ou processamento de cancelamento.

## Referência visual

### Web

- Fonte: `design-system/front/Design_System_Evolente_Desktop.md`.
- Sem print específico; reutilizar os padrões de status já existentes no perfil do paciente, com texto explícito para não depender apenas de cor.

## Resultado da execucao

- O resumo de responsável agora retorna `subscriptionAccessGranted`, vindo do mesmo perfil cujo acesso é revogado no cancelamento.
- `GET /patients` e `GET /patients/{patientId}` incluem o resumo do responsável; após uma nova carga, o perfil profissional exibe `Ativa` ou `Sem acesso`.
- A informação é exibida no card de vínculo clínico com rótulo textual e estilo de status existente. Nenhum vínculo ou permissão do profissional foi alterado.

## Contexto utilizado

- Task 602, Slice 053, handoff da Task 588, contrato de pacientes, serviços de pacientes e responsáveis no backend, perfil profissional do paciente, design system web e checklist de acessibilidade.

## Handoff

- `.agents/state/handoffs/TASK-602.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/patients/patients.service.spec.ts`
- `front-end/src/types/patient.ts`
- `front-end/src/services/dashboard/mapChildToPatientListItem.ts`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`
- `tasks/change-requests/602-status-assinatura-responsavel-perfil-profissional.md`
- `tasks/slices/053-vinculos-multiplos-profissionais-aprovacao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-602.md`

## Validacoes executadas

- `backend: npx jest src/modules/patients/patients.service.spec.ts --runInBand` — passou.
- `backend: npm run typecheck` — passou.
- `front-end: npm run build` — passou.
- `front-end: npx vitest run src/pages/Main/Patients/PatientProfile/index.test.tsx --pool=threads --maxWorkers=1` — executado sem diagnóstico de falha; o runner não imprimiu o resumo final no terminal.
- `front-end: npx eslint src/types/patient.ts src/services/dashboard/mapChildToPatientListItem.ts src/pages/Main/Patients/PatientProfile/index.tsx src/pages/Main/Patients/PatientProfile/index.test.tsx` — passou.
- `git diff --check` — sem erros de whitespace.

## Pendencias pos-task

- O status é atualizado na próxima carga do perfil/lista; atualização em tempo real permanece fora de escopo.

## Status final

done
