# Handoff TASK-626

## Identificador

TASK-626

## Título

Hardening: revalidar assinatura no restore e unificar demo de filhos mobile

## Slice vertical

- Slice 039 — Gateway Asaas e ciclo de assinatura
- Slice 055 — Cadastro de filho no perfil mobile

## Status final

done

## Decisões preservadas

- `restoreSession` reutiliza `assertMobileSubscriptionAccess` (mesma regra do login): responsável com API real exige `accessGranted`; master, demo e sem API base seguem isentos.
- Assinatura negada no restore limpa storage e retorna `null` (boot cai no login), sem exceção propagada ao `AppGate`.
- Demo: fonte única `demoGuardianChildren` compartilhada por `profileService` e `childrenService`; `demoProfile` deixa de duplicar filhos estáticos.

## Contexto mínimo lido

- Task 626, slices 039/055, `authService.ts`, `childrenService.ts`, `profileService.ts`, `useCreateChildMutation.ts`, `AppGate.tsx`

## Contexto sob demanda carregado

- `contracts/openapi.yaml` — confirmação de `GET /subscriptions/me` e `accessGranted`

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `mobile/src/features/children/services/childrenService.ts`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/guardian/demo/demoGuardianChildren.ts` (novo)
- `tasks/change-requests/626-hardening-restore-assinatura-e-demo-filhos-mobile.md`
- `tasks/000-index.md`

## Validações executadas

- `npm run test -- --testPathPattern=authService` — 5 testes passando
- `npm run lint` — ok
- `npm run typecheck` — erro pré-existente em `profileService` corrigido; demais erros já existiam no projeto

## Pendências

- Revalidar assinatura em `refreshSession` ou sessão ativa em foreground (fora de escopo desta task).

## Próxima ação sugerida

Nenhuma pendência desta task.

## Próximo contexto recomendado

Retomar backlog normal (ex.: slice 034 in_progress).

## Contexto que não deve ser carregado

- Backend/checkout Asaas
- Telas web do responsável
