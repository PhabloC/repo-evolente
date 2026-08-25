# Handoff TASK-602

## Status

done

## Objetivo

Exibir, no perfil do paciente para o profissional, o acesso de assinatura do responsável associado.

## Decisões

- O estado é informativo: não inativa vínculo nem bloqueia o profissional.
- O backend expõe o booleano persistido `subscriptionAccessGranted` no resumo de responsável, em listagem e detalhe.
- A tela mostra `Ativa` ou `Sem acesso` com rótulo textual; a atualização ocorre na próxima carga de dados.

## Contexto utilizado

- Task 602, Slice 053, handoff da Task 588, contrato de pacientes, serviços de pacientes/responsáveis e perfil web do paciente.

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/patients/patients.service.spec.ts`
- `front-end/src/types/patient.ts`
- `front-end/src/services/dashboard/mapChildToPatientListItem.ts`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`

## Validações

- Jest focado de patients, typecheck backend, build e lint web passaram.
- Vitest focado do perfil foi executado sem diagnóstico de falha; o resumo não foi emitido pelo runner.

## Pendências

- Sem atualização em tempo real; recarregar o perfil/lista consulta o estado atual.

## Próximo contexto recomendado

- Nenhum; task concluída.
