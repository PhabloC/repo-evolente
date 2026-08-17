# Task 162 - Fotos de perfil web e bucket

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml#/paths/~1users~1me`
- `contracts/openapi.yaml#/paths/~1users~1me~1avatar`
- `contracts/openapi.yaml#/paths/~1patients~1{patientId}`
- `contracts/openapi.yaml#/paths/~1patients~1{patientId}~1avatar`

## Modo de execucao

cross-stack

## Referencia de design system

### Stack de referencia visual

- front-end

### Tipo de referencia visual

artefato documental

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Regra de aderencia visual

- preservar a linguagem já consolidada das páginas de perfil, adicionando upload de imagem sem desmontar a hierarquia visual existente

## Contexto de negocio

### Por que

As páginas de perfil hoje usam apenas iniciais. O produto agora precisa permitir foto real para master, profissional e paciente, com persistência no bucket.

### O que

Adicionar upload de foto no perfil do usuário web (`master` e `profissional`) e no perfil do paciente, com gravação no bucket e retorno da URL pela API.

### Comportamento esperado

- usuário autenticado consegue enviar a própria foto
- profissional consegue enviar foto do paciente que atende
- sem foto, a UI continua mostrando inicial
- com foto, a UI passa a renderizar a imagem persistida

### Fora de escopo

- crop/edição de imagem
- remoção de foto
- upload de foto no mobile
- foto do responsável

## Review da spec

- [x] Permissoes definidas ou `nao se aplica`
- [x] Casos de erro mapeados
- [x] Decisoes de negocio confirmadas como humanas
- [x] Criterios de aceite objetivos e verificaveis
- [x] Casos de borda considerados

### Evidencias da review

- Permissões: `users/me/avatar` fica restrito ao próprio usuário autenticado; `patients/{id}/avatar` fica restrito ao profissional dono do vínculo
- Casos de erro: base64 inválido, MIME inválido, tamanho acima do limite, paciente de outro profissional
- Decisões humanas confirmadas: bucket público e páginas de perfil web como ponto de edição
- Casos de borda: telas sem foto continuam usando inicial

## Especificacao tecnica

### Deve

- estender `users` e `children` com metadados mínimos da foto
- criar endpoints de upload via JSON base64
- gravar fotos no bucket com prefixo por ambiente
- refletir `avatarUrl` nas respostas já consumidas pelo front
- atualizar a UI das páginas `Settings` e `PatientProfile`

### Nao deve

- não introduzir multipart agora
- não alterar listagens ou telas fora do escopo pedido
- não quebrar o fallback de inicial quando não houver imagem

## Entradas

- `STORAGE_BUCKET_MAP.md`
- `.agents/state/handoffs/TASK-051.md`
- `.agents/state/handoffs/TASK-052.md`
- `.agents/state/handoffs/TASK-160.md`

## Dependencias

- Task 051
- Task 052
- Task 159
- Task 160
- Task 161

## Slice vertical

### Identificador do slice

Slice 027 - Fotos de perfil em bucket

### Arquivo do slice

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

### Objetivo de negócio

Habilitar fotos reais de perfil para contas internas e pacientes, com persistência em bucket.

### Entrega verificável do slice

Upload funcional em perfil web de usuário e paciente, com URL retornada pela API.

### Fora do slice

- mobile
- recorte/edição avançada

## Contexto mínimo

Sempre ler:

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Handoff bucket | `.agents/state/handoffs/TASK-160.md` | reaproveitar convenção de key | sim |
| Handoff perfis web | `.agents/state/handoffs/TASK-051.md`, `.agents/state/handoffs/TASK-052.md` | encaixar a UI nas páginas existentes | sim |
| API | `contracts/openapi.yaml` | atualizar contrato | sim |
| Front docs | `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | implementar UI web | sim |
| Backend docs | `backend/docs/ai/ARCHITECTURE.md` | alinhar módulos e storage | sim |
| Web perfil usuário | `front-end/src/pages/Main/Settings/**` | upload da própria foto | sim |
| Web perfil paciente | `front-end/src/pages/Main/Patients/**` | upload da foto do paciente | sim |
| Backend users | `backend/src/modules/users/**` | persistir foto de master/profissional | sim |
| Backend patients/guardians | `backend/src/modules/patients/**`, `backend/src/modules/guardians/**` | persistir foto de paciente | sim |

## Orçamento de contexto

- Risco medio
- Estrategia de reducao: limitar a mudança a modelos `users`/`children`, aos dois fluxos de perfil e ao storage adapter já implantado

## Criterios de conclusao

- contrato atualizado
- backend persiste e retorna `avatarUrl`
- páginas de perfil web permitem upload com preview/fallback
- lint e testes relevantes passam

## Instrucoes de implementacao

- seguir convenção `dev/avatars/users/{userId}/original/{uuid}.{ext}` e `dev/avatars/patients/{patientId}/original/{uuid}.{ext}`
- permitir `image/jpeg`, `image/png` e `image/webp`
- manter inicial como fallback visual quando `avatarUrl` for nulo

## Validacao esperada

- `cd backend && npm run lint`
- `cd backend && npm run test`
- `cd front-end && npm run lint`
- `cd front-end && npm run build`

## Entregaveis esperados

- contrato atualizado
- suporte backend a foto de perfil
- ajustes nas páginas `Settings` e `PatientProfile`

## Riscos ou ambiguidades

- o `authStore` persiste o payload do usuário; a sessão local precisa refletir `avatarUrl` novo sem exigir logout/login

## Resultado da execucao

### Resumo por stack

- **backend**: `users` e `children` passaram a persistir metadados de avatar, com upload em bucket por `POST /users/me/avatar` e `POST /patients/{id}/avatar`.
- **front-end**: as páginas de perfil em `Settings` e `PatientProfile` agora permitem enviar foto JPG/PNG/WEBP, mantêm fallback por inicial e atualizam a imagem após o upload.

### Relação com o slice

- O slice 027 foi entregue de ponta a ponta sem reabrir mobile, recorte de imagem ou exclusão de avatar.

### Decisões técnicas

- O upload segue o padrão JSON base64 já usado em conteúdos.
- As keys novas seguem `dev/avatars/users/{userId}/original/{uuid}.{ext}` e `dev/avatars/patients/{patientId}/original/{uuid}.{ext}`.
- A API expõe `avatarUrl`, `avatarMimeType`, `avatarOriginalName` e `avatarSizeBytes`; `avatarStorageKey` permanece interno ao backend.
- O `authStore` ganhou atualização pontual do usuário para refletir a nova foto sem exigir novo login.

### Trade-offs

- Não há crop, remoção ou edição avançada da imagem nesta etapa.
- O responsável no mobile continua com avatar por inicial.

## Contexto utilizado

### Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`, esta task, `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `.agents/state/handoffs/TASK-051.md`, `.agents/state/handoffs/TASK-052.md`, `.agents/state/handoffs/TASK-160.md`

### Contexto sob demanda

| Fonte | Gatilho | Uso |
|---|---|---|
| `contracts/openapi.yaml` | API | endpoints e schemas |
| `backend/docs/ai/ARCHITECTURE.md` | backend | organização de módulo/storage |
| `front-end/docs/ai/ARCHITECTURE.md`, `CODE_STYLE.md`, `ACCESSIBILITY.md` | web | integração de UI |
| `backend/src/modules/users/**` | avatar de master/profissional | persistência e retorno |
| `backend/src/modules/patients/**`, `backend/src/modules/guardians/**` | avatar de paciente | persistência e RBAC |
| `front-end/src/pages/Main/Settings/**` | perfil do usuário | upload e fallback |
| `front-end/src/pages/Main/Patients/**` | perfil do paciente | upload e fallback |
| `STORAGE_BUCKET_MAP.md` | storage | alinhar paths do bucket |

## Handoff

- Caminho: `.agents/state/handoffs/TASK-162.md`
- Próximo contexto recomendado: mobile/responsável se você quiser levar avatar também para o app

## Arquivos alterados

### Backend

- `backend/src/common/dto/upload-image-base64.dto.ts`
- `backend/src/modules/storage/storage.module.ts`
- `backend/src/modules/storage/profile-avatar-storage.service.ts`
- `backend/src/modules/users/**`
- `backend/src/modules/patients/**`
- `backend/src/modules/guardians/**`
- `backend/src/modules/contents/contents.module.ts`
- `backend/src/database/migrations/1810000000000-AddAvatarFieldsToUsersAndChildren.ts`
- `backend/.env.example`
- `backend/.env.local`

### Front-end

- `front-end/src/types/auth.ts`
- `front-end/src/types/guardian.ts`
- `front-end/src/types/profileImage.ts`
- `front-end/src/utils/buildProfileImageUploadPayload.ts`
- `front-end/src/services/adapters/adaptAuthResponse.ts`
- `front-end/src/services/users/userService.ts`
- `front-end/src/services/patients/patientService.ts`
- `front-end/src/stores/authStore.ts`
- `front-end/src/hooks/useAuth.ts`
- `front-end/src/pages/Main/Settings/**`
- `front-end/src/pages/Main/Patients/**`
- testes de `authStore`, `adaptAuthResponse`, `Patients` e `Plans`

### Contrato e governança

- `contracts/openapi.yaml`
- `STORAGE_BUCKET_MAP.md`
- `tasks/change-requests/162-fotos-de-perfil-web-e-bucket.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-162.md`

## Validacoes executadas

- `cd backend && npm run lint` — ok
- `cd backend && npm run test` — ok (17 suites / 66 tests)
- `cd front-end && npm run lint` — ok
- `cd front-end && npm run build` — ok

## Aderencia ao design system

- Mantida a linguagem visual já consolidada dos perfis web, com fallback por inicial e CTA discreto de troca de foto.

## Pendencias pos-task

- adicionar remoção de foto, crop ou upload no mobile somente se virar nova demanda

## Status final

done
