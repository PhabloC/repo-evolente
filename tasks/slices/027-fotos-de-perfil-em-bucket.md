# Slice 027 - Fotos de perfil em bucket

## Status

done

## Objetivo de negocio

Permitir que master, profissional e paciente tenham foto de perfil persistida no bucket e refletida nas telas de perfil web, no sidebar e na listagem de usuários.

## Entrega verificavel

- master e profissional conseguem enviar foto no perfil em configuracoes
- profissional consegue enviar foto do paciente no perfil do paciente
- URLs das fotos retornam pela API e persistem no bucket
- sidebar e página de usuários web exibem a foto quando existir

## Fora de escopo

- avatar do responsavel no app mobile
- recorte/crop de imagem
- exclusao de foto
- edição de foto em listagens (somente leitura/exibição)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Stacks envolvidas

- backend
- front-end

## Contrato

- `contracts/openapi.yaml#/paths/~1users~1me`
- `contracts/openapi.yaml#/paths/~1users~1me~1avatar`
- `contracts/openapi.yaml#/paths/~1patients~1{patientId}`
- `contracts/openapi.yaml#/paths/~1patients~1{patientId}~1avatar`

## Referencia visual por stack

### Web

- tipo: artefato de design system
- fonte primaria: `design-system/front/Design_System_Evolente_Desktop.md`

### Mobile

- tipo: nao se aplica
- fonte primaria: `nao se aplica`

## Permissoes e atores

- Master: envia a própria foto
- Profissional: envia a própria foto
- Profissional: visualiza a foto já vinculada ao paciente no perfil web

## Casos de erro e borda

- formato de imagem inválido
- arquivo acima do limite
- upload para paciente de outro profissional
- perfil web do paciente em modo leitura para avatar
- perfil sem foto deve continuar usando inicial

## Decisoes humanas confirmadas

- bucket público já configurado
- persistência de foto no bucket, não no banco como binário

## Premissas adotadas

- upload segue JSON base64 para manter consistência com conteúdos
- fotos ficam em `avatars/users/...` e `avatars/patients/...`

## Tasks relacionadas

- `tasks/change-requests/159-storage-s3-compativel-minio-backend.md`
- `tasks/change-requests/160-prefixo-de-ambiente-no-storage-de-conteudos.md`
- `tasks/change-requests/161-mapa-de-uso-do-bucket-no-projeto.md`
- `tasks/change-requests/162-fotos-de-perfil-web-e-bucket.md`
- `tasks/change-requests/182-avatar-sidebar-e-pagina-usuarios-web.md`
- `tasks/change-requests/295-foto-e-fallback-nativo-nas-tabelas-de-pacientes-e-planejamentos-web.md`
- `tasks/change-requests/295-foto-e-fallback-nativo-nas-tabelas-de-pacientes-e-planejamentos-web.md`
- `tasks/change-requests/331-vincular-foto-paciente-na-aba-usuarios-web.md`
- `tasks/change-requests/332-avatar-redondo-abas-profissionais-admins-usuarios-web.md`
- `tasks/change-requests/397-vincular-foto-profissional-na-aba-usuarios-web.md`
- `tasks/change-requests/398-avatar-redondo-profissional-aba-pacientes-usuarios-web.md`
- `tasks/change-requests/350-bloquear-upload-de-foto-no-perfil-web-do-paciente-para-profissional.md`
- `tasks/change-requests/489-hardening-patch-perfil-proprio-backend.md` — done

## Dependencias do slice

- Slice 006
- Slice 007
- Slice 017

## Contexto minimo recomendado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este slice

## Contexto sob demanda recomendado

| Gatilho | Fonte | Quando carregar | Obrigatorio? |
|---|---|---|---|
| Storage atual | `.agents/state/handoffs/TASK-160.md`, `STORAGE_BUCKET_MAP.md` | reaproveitar convenção do bucket | sim |
| API | `contracts/openapi.yaml` | definir endpoints/DTOs | sim |
| UI perfil usuário | `front-end/src/pages/Main/Settings/**` | implementar foto de master/profissional | sim |
| UI perfil paciente | `front-end/src/pages/Main/Patients/**` | implementar foto de paciente | sim |
| Backend users | `backend/src/modules/users/**` | persistir avatar de usuário | sim |
| Backend patients/guardians | `backend/src/modules/patients/**`, `backend/src/modules/guardians/**` | persistir avatar de paciente | sim |

## Risco de contexto

- medio
- estrategia: limitar a mudança às telas de perfil, aos modelos `users`/`children` e ao storage adapter já existente

## Observacoes de rastreabilidade

- Este slice nasce a partir do inventário da Task 161, que confirmou ausência de avatar no código até `2026-07-24`.
- Task 212: no perfil mobile do responsável, crianças sem `avatarUrl` usam avatar pré-definido por `BiologicalSex` (`masculino`/`feminino`/neutro).

## Progresso das tasks relacionadas

- `tasks/change-requests/159-storage-s3-compativel-minio-backend.md` — done
- `tasks/change-requests/160-prefixo-de-ambiente-no-storage-de-conteudos.md` — done
- `tasks/change-requests/161-mapa-de-uso-do-bucket-no-projeto.md` — done
- `tasks/change-requests/162-fotos-de-perfil-web-e-bucket.md` — done
- `tasks/change-requests/256-hardening-troca-avatar-bucket-backend.md` — done
- `tasks/change-requests/331-vincular-foto-paciente-na-aba-usuarios-web.md` — done
- `tasks/change-requests/332-avatar-redondo-abas-profissionais-admins-usuarios-web.md` — done
- `tasks/change-requests/397-vincular-foto-profissional-na-aba-usuarios-web.md` — done
- `tasks/change-requests/398-avatar-redondo-profissional-aba-pacientes-usuarios-web.md` — done
- `tasks/change-requests/350-bloquear-upload-de-foto-no-perfil-web-do-paciente-para-profissional.md` — done

## Resultado consolidado adicional

- a troca de avatar no backend agora preserva a imagem anterior até a persistência do novo registro e limpa uploads órfãos em falhas
- `tasks/change-requests/182-avatar-sidebar-e-pagina-usuarios-web.md` — done
- `tasks/change-requests/295-foto-e-fallback-nativo-nas-tabelas-de-pacientes-e-planejamentos-web.md` — done
- `tasks/change-requests/331-vincular-foto-paciente-na-aba-usuarios-web.md` — done
- `tasks/change-requests/332-avatar-redondo-abas-profissionais-admins-usuarios-web.md` — done
- Task 397 liga também a foto do profissional na coluna `Profissional` da aba `Pacientes` da página `/usuarios`.
- Task 398 torna circular o avatar do profissional nessa mesma coluna.
- Task 350 removeu do perfil web do paciente o CTA de upload para o profissional, deixando a foto apenas em modo leitura vinculada ao perfil da criança.

## Status final

done
