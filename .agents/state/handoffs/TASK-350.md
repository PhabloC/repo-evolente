# Handoff - Task 350

## Task

- identificador: 350
- título: Bloquear upload de foto no perfil web do paciente para profissional
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 027 - Fotos de perfil em bucket
- objetivo de negócio: impedir que o profissional altere a foto da criança pelo perfil web do paciente
- entrega verificável: perfil do paciente em modo leitura para avatar, sem CTA de upload

## Decisões preservadas

- decisão: manter a exibição de `avatarUrl`, mas remover o upload da tela do profissional
- motivo: a foto deve ser apenas vinculada ao perfil da criança nesta visão
- impacto: o endpoint de upload de paciente continua existindo, mas não é mais exposto nessa página

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/350-bloquear-upload-de-foto-no-perfil-web-do-paciente-para-profissional.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-162.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | UI web | manter consistência e isolamento da mudança |
| `front-end/src/pages/Main/Patients/PatientProfile/index.tsx` e `index.test.tsx` | perfil do paciente | remover upload e validar leitura |
| `front-end/src/services/patients/patientService.ts` | service atual | confirmar endpoint que estava sendo usado pelo upload |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| `contracts/openapi.yaml` | sem mudança de contrato |
| `backend/` | sem mudança de API nesta etapa |
| `front-end/src/pages/Main/Settings/**` | upload do próprio usuário permanece igual |

## Resultado por stack

- front-end: perfil do paciente virou leitura para avatar e removeu o CTA de upload do profissional
- backend: nao se aplica
- mobile: nao se aplica

## Arquivos alterados

- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`
- `tasks/change-requests/350-bloquear-upload-de-foto-no-perfil-web-do-paciente-para-profissional.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-350.md`

## Validações executadas

- `cd front-end && npx vitest run src/pages/Main/Patients/PatientProfile/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Patients/PatientProfile/index.tsx src/pages/Main/Patients/PatientProfile/index.test.tsx` - ok

## Pendências ou bloqueios

- nenhuma

## Próxima ação sugerida

- validar visualmente o hero do perfil do paciente com e sem `avatarUrl`

## Próximo contexto recomendado

- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`

## Contexto que não deve ser carregado na próxima etapa

- fonte: `backend/`, `contracts/openapi.yaml`, `front-end/src/pages/Main/Settings/**`
- motivo: a mudança foi isolada ao perfil web do paciente
