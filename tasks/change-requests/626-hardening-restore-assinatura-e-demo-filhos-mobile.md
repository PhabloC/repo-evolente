# Task 626 - Hardening: revalidar assinatura no restore e unificar demo de filhos mobile

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

- `GET /subscriptions/me` (campo `accessGranted`)

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 — Gateway Asaas e ciclo de assinatura (`tasks/slices/039-gateway-asaas-assinatura.md`)
- Slice 055 — Cadastro de filho no perfil mobile (`tasks/slices/055-cadastro-filho-perfil-mobile.md`)

## Objetivo

Corrigir dois gaps de hardening identificados em code review do mobile:

1. Sessão de responsável restaurada no boot/biometria não revalida assinatura; usuário com assinatura expirada/cancelada fora do app permanece autenticado.
2. Em modo demo, cadastro de filho grava em `childrenService.demoChildren` mas invalidação do perfil refaz `profileService.demoProfile`, fazendo o filho recém-criado sumir.

## Comportamento esperado

- `restoreSession` consulta `/subscriptions/me` para responsável com API real; sem `accessGranted`, limpa storage e retorna `null`.
- Master, demo data e ausência de API base continuam sem gate de assinatura no restore (paridade com login).
- Modo demo usa uma única fonte mutável de filhos compartilhada entre perfil e cadastro; após criar filho e invalidar perfil, a criança permanece listada.

## Fora de escopo

- Revalidar assinatura em `refreshSession` ou durante sessão ativa em foreground.
- Alterações de backend, checkout ou telas web.

## Dependências

- Task 603 — gate de assinatura no login (done)
- Task 621 — cadastro de filho no perfil (done)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task e slices 039/055
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/children/hooks/useCreateChildMutation.ts`
- `mobile/src/features/children/services/childrenService.ts`
- `mobile/src/features/profile/services/profileService.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Contrato de acesso | `contracts/openapi.yaml#/paths/~1subscriptions~1me` | campo `accessGranted` |
| Boot mobile | `mobile/src/app/AppGate.tsx` | fluxo de restore/biometria |

## Orçamento de contexto

- baixo — dois pontos localizados em auth e serviços demo; sem UI nova.

## Critérios de aceite

- [x] `restoreSession` revalida assinatura do responsável e limpa sessão quando `accessGranted` for falso.
- [x] Boot com sessão inválida por assinatura cai no login (sem shell autenticado).
- [x] Demo: criar filho persiste após invalidação/refetch do perfil.
- [x] Testes cobrindo restore com assinatura negada.
- [x] Lint e testes do escopo passam.

## Resultado da execucao

- `restoreSession` chama `assertMobileSubscriptionAccess` após validar papel suportado; sem acesso, limpa storage e retorna `null`.
- Criado `demoGuardianChildren` como fonte única mutável; `profileService.getResponsavelProfile` e `childrenService` leem/escrevem a mesma lista no modo demo.

## Contexto utilizado

- Task 626, slices 039/055, serviços de auth/perfil/filhos, contrato `/subscriptions/me`, testes de auth.

## Handoff

`.agents/state/handoffs/TASK-626.md`

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `mobile/src/features/children/services/childrenService.ts`
- `mobile/src/features/profile/services/profileService.ts`
- `mobile/src/features/guardian/demo/demoGuardianChildren.ts`
- `tasks/change-requests/626-hardening-restore-assinatura-e-demo-filhos-mobile.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- --testPathPattern=authService` — passou (5 testes)
- `npm run lint` — passou

## Pendencias pos-task

- Revalidação de assinatura em `refreshSession`/sessão ativa permanece fora de escopo.

## Status final

done
