# Task 243 - Redesign das telas de edição de perfil + avatar

## Status

done

## Tipo

shared

## Stacks envolvidos

backend, contracts, mobile

## Modo de execucao

cross-stack

## Slice vertical

`tasks/slices/010-app-responsavel-home-notificacoes.md`

## Perfil do projeto

- stack web: front-end
- mobile: sim

## Contrato

`contracts/openapi.yaml` — `POST /users/me/avatar`; `POST /guardians/me/children/{childId}/avatar`; `PATCH /guardians/me` (`phone`)

## Dependencias

- Task 238, Task 239

## Objetivo

Melhorar as telas de edição do responsável e da criança: espaçamento superior alinhado ao perfil, edição de foto de perfil, design mais preenchido com campos editáveis e bloco de dados protegidos (somente leitura).

## Entrega verificavel

- `paddingVertical: spacing.lg` nas telas de edição
- Upload de avatar do responsável via `POST /users/me/avatar`
- Upload de avatar da criança via `POST /guardians/me/children/{childId}/avatar`
- UI com seções (foto, dados editáveis, dados protegidos) nas duas telas
- Dados sensíveis permanecem somente leitura

## Fora de escopo

- Alterar e-mail, CPF, patientCode ou data de nascimento
- Edição de avatar no web

## Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- Esta task
- Slice 010
- Handoffs TASK-238 / TASK-239

## Contexto sob demanda

- `contracts/openapi.yaml` (paths guardians/users avatar)
- `backend/src/modules/guardians/**`
- `mobile/src/features/profile/**`
- tokens mobile

## Orcamento de contexto

medio

## Referencia visual

`design-system/mobile/Design_System_Evolente_App_Mobile.md` + tokens mobile existentes

## Resultado da execucao

Implementado redesign das telas `EditGuardianProfile` e `EditChildProfile` com avatar editável, seções de dados editáveis/protegidos, telefone editável no responsável e endpoint de avatar da criança para o guardian.

## Contexto utilizado

- OpenAPI guardians/users
- GuardiansService/Controller
- profileService + hooks mobile
- expo-image-picker

## Handoff

`.agents/state/handoffs/TASK-243.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/**`
- specs que instanciam `GuardiansService`
- `mobile/src/features/profile/**`
- `mobile/app.json`, `mobile/package.json`

## Validacoes executadas

- `npx jest guardians.service.spec.ts` — pass
- `patients.service.spec` + `subscriptions.service.spec` — pass
- `npm run typecheck` (mobile) — pass

## Pendencias pos-task

- Em build nativo, rebuild necessário por causa do plugin `expo-image-picker`
- Validar upload real de avatar com storage configurado no ambiente

## Status final

done
