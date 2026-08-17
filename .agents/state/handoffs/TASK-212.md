# Handoff - Task 212

## Task

- identificador: 212
- título: Avatar padrão da criança por sexo no mobile
- tipo: mobile
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 027 (+ perfil Slice 010)
- entrega verificável: criança sem foto mostra avatar default por sexo

## Decisões preservadas

- decisão: prioridade `avatarUrl` > default por sexo
- motivo: pedido do produto
- impacto: assets locais `masculino` / `feminino` / `neutro` (`outro` e `nao_informado`)

- decisão: mapear `sex` e `avatarUrl` no profile mobile a partir de `/guardians/me/children`
- motivo: API já devolvia; cliente descartava

## Contexto utilizado

- task 212, BiologicalSex no openapi, profile types/service, ResponsavelProfileScreen

## Arquivos alterados

- `mobile/assets/avatars/child-masculino.png`
- `mobile/assets/avatars/child-feminino.png`
- `mobile/assets/avatars/child-neutro.png`
- `mobile/src/features/profile/types/profile.ts`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/profile/utils/resolveChildAvatarSource.ts`
- `mobile/src/features/profile/utils/resolveChildAvatarSource.test.ts`
- `mobile/src/features/shell/components/ChildAvatar/`
- `mobile/src/features/shell/screens/ResponsavelProfileScreen.tsx`
- `tasks/change-requests/212-avatar-padrao-crianca-por-sexo-mobile.md`
- `tasks/slices/027-fotos-de-perfil-em-bucket.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-212.md`

## Validações executadas

- `npm run typecheck` — ok
- `npm test -- --testPathPattern=resolveChildAvatarSource` — ok

## Pendências ou bloqueios

- upload de foto da criança no mobile continua fora de escopo
- assets PNG ~1MB cada; comprimir depois se necessário

## Próxima ação sugerida

- opcional: usar o mesmo `ChildAvatar` na home/trilha quando houver foto da criança em destaque
