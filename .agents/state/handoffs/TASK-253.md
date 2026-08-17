# Handoff - Task 253

## Task

- identificador: 253
- título: Corrigir sincronização do avatar e remoção de telefone no perfil mobile
- tipo: shared
- modo de execução: cross-stack
- status final: done

## Slice vertical

- identificador: 010
- objetivo de negócio: preservar a edição de perfil do responsável sem regressões em avatar e telefone

## Decisões preservadas

- `PATCH /guardians/me` agora aceita `phone: null` para limpar o telefone do responsável
- Upload de avatar não deve invalidar/refetchar o perfil inteiro enquanto a tela de edição estiver aberta
- A tela de edição do responsável inicializa o formulário apenas uma vez por montagem

## Contexto efetivamente usado

- task 253, índice, slice 010
- handoffs `TASK-243` e `TASK-247`
- `contracts/openapi.yaml` no path `PATCH /guardians/me`
- módulo `guardians` e `users` no backend
- feature mobile de perfil

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/guardians/dto/update-my-guardian-profile.dto.ts`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `backend/src/modules/users/dto/update-user.dto.ts`
- `backend/src/modules/users/users.in-memory.repository.ts`
- `backend/src/modules/users/users.repository.ts`
- `mobile/src/features/profile/hooks/useResponsavelProfile.ts`
- `mobile/src/features/profile/hooks/useResponsavelProfile.test.ts`
- `mobile/src/features/profile/screens/EditGuardianProfileScreen.tsx`
- `mobile/src/features/profile/services/profileService.ts`

## Validacoes executadas

- `cd backend && npm run test -- guardians.service.spec.ts` — ok
- `cd mobile && npm run test -- useResponsavelProfile` — ok
- `cd mobile && npm run typecheck` — ok

## Pendencias ou bloqueios

- Falta smoke test manual em dispositivo para confirmar remoção de telefone e edição simultânea com troca de avatar

## Próximo contexto recomendado

- `tasks/change-requests/254-corrigir-fala-e-fluxo-assincrono-escrita-guiada-mobile.md`
- `mobile/src/features/games/services/gameSpeechService.ts`
- `mobile/src/features/games/components/AlphabetWritingGameRenderer/index.tsx`
