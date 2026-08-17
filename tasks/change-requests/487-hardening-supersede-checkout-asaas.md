# Task 487 - Hardening do supersede de checkout Asaas

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem mudança de contrato; ajuste no fluxo interno de checkout/Asaas

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Impedir que um checkout pendente local seja marcado como cancelado quando o cancelamento remoto no Asaas falhar durante a criação de um novo checkout.

## Criterios de aceite

- [x] falha ao cancelar checkout pendente no provider interrompe a criação do novo checkout
- [x] assinatura pendente anterior permanece íntegra no repositório local
- [x] teste de regressão cobre o cenário
- [x] handoff gerado

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/change-requests/487-hardening-supersede-checkout-asaas.md`
- `.agents/state/handoffs/TASK-425.md`

## Contexto sob demanda

- `backend/AGENTS.md` e `backend/docs/ai/AGENTS.md`
- `backend/docs/ai/SECURITY.md` e `backend/docs/ai/QA.md`
- `backend/src/modules/subscriptions/`

## Orçamento de contexto

- 8 fontes
- estratégia: limitar ao serviço/repositório de assinaturas e specs focadas

## Resultado da execucao

O backend agora falha de forma explícita quando não consegue cancelar remotamente o checkout pendente anterior, evitando abrir uma nova cobrança com estado local inconsistente.

## Contexto utilizado

- slice 039
- handoff 425
- `subscriptions.service` e `subscriptions.service.spec`

## Handoff

- `.agents/state/handoffs/TASK-487.md`

## Arquivos alterados

- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `backend/src/modules/subscriptions/subscriptions.service.spec.ts`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`

## Validacoes executadas

- `npm run test -- --runInBand src/modules/subscriptions/subscriptions.service.spec.ts src/modules/admin/admin.service.spec.ts src/modules/contents/catalog-config-merge.spec.ts src/modules/users/dto/update-own-profile.dto.spec.ts` — PASS
- `npx eslint src/modules/subscriptions/subscriptions.service.ts src/modules/subscriptions/subscriptions.service.spec.ts src/modules/users/dto/update-own-profile.dto.ts src/modules/users/dto/update-own-profile.dto.spec.ts src/modules/admin/admin.service.ts src/modules/admin/admin.service.spec.ts src/modules/contents/fluency-game-assets.ts src/modules/contents/dialogue-game-assets.ts src/modules/contents/emotions-game-assets.ts src/modules/contents/jigsaw-game-assets.ts src/modules/contents/catalog-config-merge.spec.ts` — PASS

## Pendencias pos-task

- o fluxo ainda não tem retry assíncrono/persistido para cancelamento remoto; a mitigação atual é bloquear o supersede inconsistente

## Status final

done
