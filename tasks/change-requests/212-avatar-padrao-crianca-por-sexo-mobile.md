# Task 212 - Avatar padrão da criança por sexo no mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- reuso: `Child.sex` (`BiologicalSex`) e `Child.avatarUrl` em `GET /guardians/me/children`
- sem endpoint novo

## Modo de execucao

single-stack

## Slice vertical

### Identificador do slice

Slice 027 - Fotos de perfil em bucket (extensão de exibição no mobile do responsável)

### Arquivo do slice

- `tasks/slices/027-fotos-de-perfil-em-bucket.md`

Também relacionado a Slice 010 (lista de crianças no perfil).

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

pedido explícito + tokens Evolente

### Fonte primaria visual

- pedido: se a criança não tiver foto, usar avatar pré-definido conforme o sexo até upload próprio

## Contexto de negocio

### Por que

A lista de crianças no perfil mobile usa ícone genérico e ignora `sex`/`avatarUrl` já disponíveis na API.

### O que

Mapear `sex` e `avatarUrl` no profile mobile e exibir foto custom ou default por sexo.

### Comportamento esperado

- se `avatarUrl` existir → usar a foto
- senão → avatar local por `masculino` / `feminino`
- `outro` / `nao_informado` → avatar neutro
- demo data inclui sexo para validar fallback

### Fora de escopo

- upload de foto da criança no mobile
- alteração web
- mudança de contrato

## Dependencias

- Slice 027
- Task 210/211 (perfil)

## Contexto minimo

- esta task, slice 027, `profile` types/service, `ResponsavelProfileScreen`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Sex enum | openapi BiologicalSex | valores oficiais | sim |
| UI perfil | ResponsavelProfileScreen | trocar Baby por Image | sim |

## Orcamento de contexto

- Risco baixo

## Criterios de conclusao

- crianças sem foto mostram avatar por sexo
- foto própria prevalece
- typecheck/testes do helper ok

## Resultado da execucao

- Profile mobile mapeia `sex` e `avatarUrl` das crianças.
- Sem foto: avatar local por `masculino` / `feminino` / neutro.
- Com foto: usa `avatarUrl`.
- Lista de crianças no perfil usa `ChildAvatar`.

## Contexto utilizado

- task 212, profile, BiologicalSex, tela de perfil

## Handoff

- `.agents/state/handoffs/TASK-212.md`

## Arquivos alterados

- `mobile/assets/avatars/child-masculino.png`
- `mobile/assets/avatars/child-feminino.png`
- `mobile/assets/avatars/child-neutro.png`
- `mobile/src/features/profile/types/profile.ts`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/profile/utils/resolveChildAvatarSource.ts`
- `mobile/src/features/profile/utils/resolveChildAvatarSource.test.ts`
- `mobile/src/features/shell/components/ChildAvatar/index.tsx`
- `mobile/src/features/shell/components/ChildAvatar/styles.ts`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/212-avatar-padrao-crianca-por-sexo-mobile.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-212.md`

## Validacoes executadas

- `cd mobile && npm run typecheck` — ok
- `cd mobile && npm test -- --testPathPattern=resolveChildAvatarSource` — ok

## Pendencias pos-task

- upload de foto da criança no mobile fora de escopo

## Status final

done
