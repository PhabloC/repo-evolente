# Handoff - Task 243

## Task

- identificador: 243
- título: Redesign das telas de edição de perfil + avatar
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 010
- objetivo de negócio: home/perfil do responsável
- entrega verificável: edição de perfil com foto e dados protegidos visíveis

## Decisões preservadas

- Avatar do responsável: `POST /users/me/avatar`
- Avatar da criança: `POST /guardians/me/children/{childId}/avatar` (somente guardian dono)
- Telefone passou a ser editável em `PATCH /guardians/me`
- E-mail, CPF, nascimento e patientCode permanecem somente leitura na UI
- Upload usa galeria via `expo-image-picker` + Base64

## Contexto utilizado

### Contexto mínimo lido

- Task 243, índice, handoffs 238/239

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| openapi guardians/users | contrato avatar | documentar endpoint |
| guardians module | API child avatar | implementação |
| profile mobile | UI | redesign |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| front-end web | fora de escopo |
| design-system/front | task mobile |

## Resultado por stack

- backend: endpoint avatar criança + phone no PATCH me
- contracts: OpenAPI atualizado
- mobile: telas redesenhadas + picker + upload

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/guardians.controller.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/dto/update-my-guardian-profile.dto.ts`
- `backend/src/modules/guardians/guardians.module.ts`
- specs de GuardiansService
- `mobile/src/features/profile/**`
- `mobile/app.json`

## Validações executadas

- testes guardians/patients/subscriptions: pass
- typecheck mobile: pass

## Pendências ou bloqueios

- Rebuild nativo se usar Expo Dev Client / builds com plugins novos
- Smoke test de upload com bucket real

## Próxima ação sugerida

- Validar visualmente no app (responsável e criança) e upload de foto

## Próximo contexto recomendado

- Telas `EditGuardianProfileScreen` / `EditChildProfileScreen`
- `profileService.ts`

## Contexto que não deve ser carregado na próxima etapa

- Spec completa de onboarding / anamnese
- Design system web
