# Handoff - Task 162

## Task

- identificador: 162
- título: Fotos de perfil web e bucket
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: Slice 027 - Fotos de perfil em bucket
- objetivo de negócio: habilitar fotos reais para contas internas e pacientes
- entrega verificável: upload funcionando em `Settings` e `PatientProfile`, com persistência no bucket
- status do slice: done

## Decisões preservadas

- upload ficou em JSON base64 para manter consistência com conteúdos
- fotos de `master` e `profissional` ficam em `avatars/users/...`
- fotos de `paciente` ficam em `avatars/patients/...`
- `avatarStorageKey` ficou interno; a API expõe só metadados públicos e `avatarUrl`
- `authStore` recebeu atualização de usuário sem exigir relogin

## Contexto utilizado

### Contexto mínimo lido

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, `tasks/change-requests/162-fotos-de-perfil-web-e-bucket.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-051.md`, `.agents/state/handoffs/TASK-052.md`, `.agents/state/handoffs/TASK-160.md`

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | contrato | novos endpoints/schemas |
| `backend/src/modules/users/**` | avatar user | persistência e retorno |
| `backend/src/modules/patients/**`, `guardians/**` | avatar patient | persistência e RBAC |
| `front-end/src/pages/Main/Settings/**` | perfil user | upload e fallback |
| `front-end/src/pages/Main/Patients/**` | perfil patient | upload e fallback |
| `STORAGE_BUCKET_MAP.md` | bucket | alinhar paths |

## Resultado por stack

- backend: done
- front-end: done

## Arquivos alterados

- `backend/src/common/dto/upload-image-base64.dto.ts`
- `backend/src/modules/storage/storage.module.ts`
- `backend/src/modules/storage/profile-avatar-storage.service.ts`
- `backend/src/modules/users/**`
- `backend/src/modules/patients/**`
- `backend/src/modules/guardians/**`
- `backend/src/database/migrations/1810000000000-AddAvatarFieldsToUsersAndChildren.ts`
- `contracts/openapi.yaml`
- `front-end/src/types/{auth.ts,guardian.ts,profileImage.ts}`
- `front-end/src/utils/buildProfileImageUploadPayload.ts`
- `front-end/src/services/{users/userService.ts,patients/patientService.ts,adapters/adaptAuthResponse.ts}`
- `front-end/src/stores/authStore.ts`
- `front-end/src/hooks/useAuth.ts`
- `front-end/src/pages/Main/Settings/**`
- `front-end/src/pages/Main/Patients/**`
- `STORAGE_BUCKET_MAP.md`

## Validações executadas

- backend lint: ok
- backend test: ok (17 suites / 66 tests)
- front-end lint: ok
- front-end build: ok

## Pendências ou bloqueios

- nenhuma bloqueante
- mobile/responsável ainda não tem upload de foto

## Próxima ação sugerida

- abrir nova CR apenas se quiser foto de perfil também no app do responsável ou remoção/crop de avatar

## Próximo contexto recomendado

- `front-end/src/pages/Main/Settings/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `backend/src/modules/storage/profile-avatar-storage.service.ts`

## Contexto que não deve ser carregado na próxima etapa

- telas administrativas/listagens sem relação com perfil
- motivo: esta entrega ficou contida às páginas de perfil
