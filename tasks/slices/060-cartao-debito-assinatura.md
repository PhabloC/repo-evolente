# Slice 060: cartão de débito na assinatura

## Objetivo de negócio

Permitir que o usuário contrate o plano usando cartão de débito, além das opções atuais de cartão de crédito e PIX, respeitando as capacidades reais do Asaas para cobranças recorrentes.

## Status: done

## Entrega verificável

- O checkout informa cartão de crédito ou débito, usando o identificador `credit_card` exigido pelo Asaas.
- A API, o backend e o front-end representam o novo meio sem aceitar valores inconsistentes.
- O pagamento confirmado e os eventos de falha/atraso preservam o mesmo gate de assinatura atual.
- Caso o Asaas não suporte débito recorrente para este produto, a task documenta a limitação e entrega a alternativa aprovada.

## Fora de escopo

- Débito automático em conta ou Pix Automático.
- Alteração de preços, periodicidade ou regras de acesso.
- Aplicativo mobile nesta primeira fatia, salvo necessidade descoberta no contrato.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/629-remover-boleto-checkout-asaas.md`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`

## Contexto sob demanda

- `contracts/openapi.yaml`: paths e schemas de checkout/assinatura, se o meio for exposto na API.
- `backend/docs/ai/`: regras locais do backend.
- `front-end/docs/ai/`: regras locais da interface web.
- Documentação oficial do Asaas sobre cartão de débito e recorrência: validar a capacidade antes da implementação.

## Orçamento de contexto

Até 8 fontes obrigatórias. Priorizar contrato, provider, gate web e documentação oficial; não carregar mobile ou requisitos completos salvo dependência descoberta.

## Risco de contexto

O termo débito pode significar cartão de débito ou débito automático. Esta task foi executada para cartão de débito na fatura; débito automático em conta/Pix Automático permanece fora do escopo.

## Tasks relacionadas

- Slice 039 / Tasks 419–425: gateway Asaas e ciclo de assinatura.
- Task 629: meios aceitos no checkout.
