# Task 804 - Especialidades do master que atua como profissional

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim (não envolvido)

## Contrato

- `contracts/openapi.yaml#/paths/~1users~1{userId}` (GET e PATCH)
- `contracts/openapi.yaml#/components/schemas/UpdateUserRequest`
- `contracts/openapi.yaml#/components/schemas/User`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 072 — `tasks/slices/072-gestao-operacional-usuarios-master.md`

## Objetivo

Ao marcar o master como "também atua como profissional", abrir um campo para informar as especialidades dele, gravadas no perfil profissional.

## Decisão humana confirmada

- Pedido humano: "quando eu marcar o master para atuar também como profissional abre um campo para ele colocar as suas especialidades"

## Premissas adotadas

- Mesmo formato do cadastro de profissional: texto livre separado por vírgula (`parseSpecialties`)
- Especialidades obrigatórias ao ativar (`PROFESSIONAL_SPECIALTIES_REQUIRED`); podem ser alteradas depois
- `professionalSpecialties` volta em `GET`/`PATCH /users/{userId}` só para master que atua como profissional; a listagem não traz o campo e o modal busca o detalhe para preencher

## Dependências

- Task 802 — done

## Contexto mínimo

- esta task e o Slice 072
- `backend/src/modules/users/`
- `front-end/src/pages/Main/AdminUsers/EditUserModal.tsx`
- `front-end/src/utils/parseSpecialties.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Formato de especialidades | `backend/src/modules/professionals/dto/register-professional.dto.ts`, `front-end/src/pages/Auth/RegisterProfessional/index.tsx` | repetir validação e campo |

## Orçamento de contexto

- baixo

## Critérios de aceite

- [x] Campo "Especialidades" aparece só quando a opção de atuar como profissional está marcada
- [x] Salvar sem especialidade mostra erro e não chama a API
- [x] Especialidades gravadas no perfil profissional e devolvidas no detalhe
- [x] Edição posterior vem com as especialidades preenchidas
- [x] Detalhe do perfil do master mostra as especialidades

## Fora de escopo

- Mobile
- Registro profissional e dados de clínica do master

## Resultado da execucao

- Backend: `professionalSpecialties` no `UpdateUserDto`, `upsertProfessionalProfile` (cria/atualiza perfil com especialidades e acesso liberado), `findProfessionalSpecialties`, resposta enriquecida em `findOne`/`update`
- Front: campo condicional com validação, pré-preenchimento via `getUserById`, linha "Especialidades" no perfil

## Handoff

- `.agents/state/handoffs/TASK-804.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/users/dto/update-user.dto.ts`
- `backend/src/modules/users/entities/user.entity.ts`
- `backend/src/modules/users/users.repository.ts`
- `backend/src/modules/users/users.typeorm.repository.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/users/users.service.spec.ts`
- `front-end/src/types/admin.ts`
- `front-end/src/pages/Main/AdminUsers/EditUserModal.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`

## Validacoes executadas

- Backend: `users.service.spec` 21/21; `npm run build` ok
- Front: tsc/eslint sem erros nos arquivos alterados; testes "marca um master…" e "preenche as especialidades…" passando
- Falhas antigas de AdminUsers seguem iguais; timeouts intermitentes sob carga

## Pendencias pos-task

- Validar no browser com o backend local

## Status final

done
