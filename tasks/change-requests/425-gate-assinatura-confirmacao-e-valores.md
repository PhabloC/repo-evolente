# Task 425 - Gate de assinatura: confirmação profissional e valores oficiais

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- sem mudança de contrato

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Impedir redirecionamento automático do profissional após pagamento (mostrar confirmação com CTA) e atualizar a tela `/assinatura` com os valores oficiais R$ 79 / R$ 49.

## Dependencias

- Task 419 / 424 — done

## Contexto mínimo

- esta task
- `front-end/src/pages/Auth/SubscriptionGate/`
- `front-end/src/constants/adminOptions.ts` (planos oficiais)

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | checklist UI |

## Orçamento de contexto

- baixo

## Criterios de aceite

- [x] Após pagamento fake, profissional permanece na tela de confirmação com “Ir para o dashboard”
- [x] Login no gate com assinatura já ativa mostra confirmação (não some para o dashboard sozinho)
- [x] Valor exibido: R$ 79 profissional / R$ 49 responsável
- [x] Remover copy “a definir”
- [x] Teste do gate atualizado

## Fora de escopo

- Integração Asaas real
- Backend

## Resultado da execucao

- Removido `navigate` automático após pagamento/login no gate para profissional.
- Valores oficiais e copy Asaas na tela `/assinatura`.
- Helper `formatSubscriptionAmount` extraído para `utils/`.

## Contexto utilizado

- SubscriptionGate + adminOptions + ACCESSIBILITY checklist

## Handoff

- `.agents/state/handoffs/TASK-425.md`

## Arquivos alterados

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx`
- `front-end/src/utils/formatSubscriptionAmount.ts`
- `front-end/src/pages/Main/Admin/utils.ts`
- `tasks/change-requests/425-gate-assinatura-confirmacao-e-valores.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-425.md`

## Validacoes executadas

- `vitest run src/pages/Auth/SubscriptionGate/index.test.tsx` — 2 passed

## Pendencias pos-task

- Contas já pagas via login principal (`/login`) ainda vão direto ao dashboard (comportamento esperado)
- Task 420 Asaas

## Status final

done
