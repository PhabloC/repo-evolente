# Task 350 - Bloquear upload de foto no perfil web do paciente para profissional

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

nao se aplica

## Modo de execucao

single-stack

## Referencia de design system

### Stack de referencia visual

front-end

### Tipo de referencia visual

ajuste funcional orientado por decisão do usuário no chat

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar o hero do perfil do paciente e remover apenas a ação de alteração de foto para o profissional

## Contexto de negocio

### Por que

O profissional não deve conseguir enviar ou trocar a foto da criança a partir do perfil web do paciente.

### O que

Remover do perfil do paciente a ação de upload de foto e tratar a imagem apenas como leitura, exibindo a foto já vinculada em `avatarUrl` quando existir.

### Comportamento esperado

- profissional visualiza a foto da criança quando `avatarUrl` existir
- profissional não vê CTA nem input de upload de foto nessa tela
- a copy deixa claro que a imagem exibida é vinculada ao perfil da criança

### Fora de escopo

- alterações de backend
- nova tela para gerir foto da criança
- mudanças no upload da foto do próprio usuário em `Settings`

## Slice vertical

### Identificador do slice

Slice 027 - Fotos de perfil em bucket

### Arquivo do slice

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-162.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| UI web | `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md` | preservar semântica e isolamento do ajuste | sim |
| Perfil do paciente | `front-end/src/pages/Main/Patients/PatientProfile/index.tsx` e `index.test.tsx` | remover upload e validar comportamento em leitura | sim |
| Service atual | `front-end/src/services/patients/patientService.ts` | confirmar endpoint atualmente usado pelo upload | sim |

## Orçamento de contexto

- baixo
- estrategia de reducao: limitar a mudança ao perfil web do paciente, sem reabrir backend ou outras telas de avatar

## Criterios de conclusao

- [x] botão `Alterar foto` deixa de existir no perfil do paciente
- [x] foto continua sendo exibida quando `avatarUrl` existir
- [x] copy informa que a imagem é apenas vinculada ao perfil da criança
- [x] teste focado e lint dos arquivos alterados passam

## Dependencias

- Task 162
- Task 348

## Resultado da execucao

- o perfil do paciente deixou de importar e usar o fluxo de upload de avatar
- a seção do hero passou a exibir a foto da criança como leitura, com copy explícita de vínculo ao perfil da criança
- o teste da página agora garante que o CTA `Alterar foto` não aparece para o profissional

## Contexto utilizado

### Mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-162.md`

### Sob demanda

- `front-end/docs/ai/ACCESSIBILITY.md`, `ARCHITECTURE.md`, `CODE_STYLE.md`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`
- `front-end/src/services/patients/patientService.ts`

### Contexto evitado

- `contracts/openapi.yaml` por nao haver alteração de contrato
- `backend/` por nao haver alteração de permissão na API nesta etapa
- `front-end/src/pages/Main/Settings/**` por nao afetar o upload do próprio usuário

## Handoff

- `.agents/state/handoffs/TASK-350.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`
- `tasks/change-requests/350-bloquear-upload-de-foto-no-perfil-web-do-paciente-para-profissional.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-350.md`

## Validacoes executadas

- `cd front-end && npx vitest run src/pages/Main/Patients/PatientProfile/index.test.tsx` - ok
- `cd front-end && npx eslint src/pages/Main/Patients/PatientProfile/index.tsx src/pages/Main/Patients/PatientProfile/index.test.tsx` - ok

## Pendencias pos-task

- nenhuma

## Status final

done
