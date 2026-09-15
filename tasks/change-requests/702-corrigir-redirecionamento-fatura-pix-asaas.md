# Task 702 - Corrigir redirecionamento da fatura PIX Asaas

## Status

done

## Tipo

back

## Stacks envolvidos

backend

## Contrato

Nenhum — a URL continua no mesmo campo `invoiceUrl`.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/060-cartao-debito-assinatura.md`

## Objetivo

Permitir que o usuário permaneça na página hospedada do Asaas para concluir o pagamento PIX, sem redirecionamento automático prematuro ao Evolente.

## Escopo

- Remover `autoRedirect=true` das URLs de fatura PIX retornadas pelo backend.
- Atualizar testes do provider.

## Critérios de aceite

- Reabrir fatura abre a página do Asaas e não retorna imediatamente ao Evolente.
- A URL retornada não contém `autoRedirect=true`.
- Confirmação por webhook, polling e verificação manual permanecem inalterados.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/060-cartao-debito-assinatura.md`
- `tasks/change-requests/696-remover-pix-copia-cola-local.md`

## Contexto sob demanda

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts`

## Orçamento de contexto

Até 6 fontes; limitar a alteração ao provider, testes e rastreabilidade da task.

## Dependências

- Task 696.

## Resultado da execucao

Removido o redirecionamento automático da fatura PIX Asaas. A URL permanece hospedada no Asaas até a conclusão ou saída manual do pagador.

## Contexto utilizado

- Provider Asaas e teste unitário relacionado.

## Handoff

O fluxo de confirmação continua dependente de webhook/polling após o pagamento.

## Arquivos alterados

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts`
- `tasks/change-requests/702-corrigir-redirecionamento-fatura-pix-asaas.md`

## Validacoes executadas

- `npm test -- --runInBand src/modules/subscriptions/providers/asaas-payment.provider.spec.ts` — 15 testes aprovados.

## Pendencias pos-task

Nenhuma.

## Status final

done
