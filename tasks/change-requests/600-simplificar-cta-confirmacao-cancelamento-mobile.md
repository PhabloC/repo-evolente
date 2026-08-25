# Task 600 - Simplificar CTA de confirmação de cancelamento no mobile

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

- não se aplica; não altera integração nem regras de assinatura

## Modo de execução

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Alterar o texto do CTA de confirmação de cancelamento de assinatura de `Confirmar cancelamento` para `Confirmar` no modal do perfil do responsável.

## Dependências

- Task 599 — done

## Contexto mínimo

- esta task
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `.agents/state/handoffs/TASK-599.md`
- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Manter composição e reutilização do componente | `mobile/docs/ai/ARCHITECTURE.md`, `mobile/docs/ai/COMPONENT_REUSE.md` | validar que a alteração permanece no componente de domínio correto |

## Orçamento de contexto

- baixo
- estratégia: alterar somente a string condicional do CTA, sem tocar no comportamento de cancelamento, reembolso ou API.

## Critérios de aceite

- [x] Ao confirmar o cancelamento, o CTA exibe `Confirmar` quando não estiver processando.
- [x] O CTA de reembolso e os estados de carregamento permanecem inalterados.

## Fora de escopo

- Alterar a operação de cancelamento, o modal, o reembolso ou o backend.

## Referência visual

### Mobile

- Sem alteração estrutural de UI; preservar `AppConfirmModal` e os componentes mobile existentes.

## Resultado da execucao

- O CTA da confirmação de cancelamento passou de `Confirmar cancelamento` para `Confirmar`.
- O CTA de reembolso (`Confirmar reembolso`) e o estado de processamento (`Processando…`) foram preservados.

## Contexto utilizado

- Task 600, Slice 039, handoff da Task 599, `SubscriptionManagementCard` e os guias mobile de arquitetura e reutilização de componentes.

## Handoff

- `.agents/state/handoffs/TASK-600.md`

## Arquivos alterados

- `mobile/src/features/shell/components/SubscriptionManagementCard/index.tsx`
- `tasks/change-requests/600-simplificar-cta-confirmacao-cancelamento-mobile.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `.agents/state/handoffs/TASK-600.md`

## Validacoes executadas

- `npx eslint src/features/shell/components/SubscriptionManagementCard/index.tsx` — passou

## Pendencias pos-task

- Nenhuma.

## Status final

done
