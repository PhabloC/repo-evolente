# Task 695 - Implementar cartão de débito na assinatura

**Status**: done
**Tipo**: shared
**Stacks envolvidos**: backend, front-end (React/Vite)
**Contrato**: `contracts/openapi.yaml` — checkout e schemas de assinatura, se houver alteração de enum/response
**Modo de execução**: cross-stack
**Slice vertical**: `tasks/slices/060-cartao-debito-assinatura.md`

## Objetivo

Adicionar suporte a cartão de débito no fluxo de contratação mensal, desde que o Asaas permita o processamento recorrente necessário ao produto.

## Escopo

- Validar tecnicamente a disponibilidade de cartão de débito no checkout/assinatura recorrente do Asaas.
- Atualizar provider, tipos, DTOs, contrato OpenAPI, gate web e testes quando suportado.
- Preservar confirmação por webhook, verificação manual, cancelamento e suspensão por inadimplência.
- Se o provedor não suportar débito recorrente, registrar a limitação e propor a alternativa de produto antes de implementar um fluxo incompatível.

## Critérios de aceite

- Cartão de débito não é exibido nem aceito se o Asaas não suportar o fluxo recorrente.
- Quando suportado, o novo meio aparece no front-end, é validado na API e chega corretamente ao provider.
- Eventos de sucesso, recusa, atraso e cancelamento mantêm o comportamento atual da assinatura.
- Testes cobrem aceitação, rejeição e compatibilidade com cartão de crédito/PIX.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/060-cartao-debito-assinatura.md`
- `tasks/change-requests/629-remover-boleto-checkout-asaas.md`

## Contexto sob demanda

- `contracts/openapi.yaml`: endpoints e schemas de subscriptions.
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts` e specs relacionadas.
- `front-end/src/pages/Auth/SubscriptionGate/` e serviços de subscriptions.
- `backend/docs/ai/` e `front-end/docs/ai/`.
- Documentação oficial do Asaas sobre cartão de débito e recorrência.

## Orçamento de contexto

Até 8 fontes obrigatórias; carregar somente os trechos do contrato e os arquivos diretamente envolvidos.

## Dependências

- Slice 039 / Tasks 419–425.
- Task 629.

## Resultado da execucao

O Asaas não possui `debit_card` como novo `billingType` no checkout recorrente. O fluxo existente `CREDIT_CARD` foi mantido e a interface/documentação agora informa que o Asaas pode apresentar crédito ou débito na fatura conforme elegibilidade.

## Contexto utilizado

- Documentação oficial do Asaas sobre checkout recorrente, assinaturas e pagamentos via cartão.
- Provider Asaas, contrato OpenAPI, gate web e Task 629.

## Handoff

Validar em sandbox abrindo o checkout Asaas e confirmando se a fatura oferece débito para um cliente elegível. Débito automático em conta/Pix Automático exige nova task.

## Arquivos alterados

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `contracts/openapi.yaml`
- `ASAAS-CHECKOUT-PAGAMENTO.md`

## Validacoes executadas

- Inspeção do contrato e fluxo Asaas concluída.
- Backend: 2 suites, 38 testes aprovados.
- Front-end: `npm run lint` aprovado.

## Pendencias pos-task

- Confirmar no painel/sandbox do Asaas a disponibilidade efetiva da opção débito para o perfil pagador.

## Status final

done
