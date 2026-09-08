# Handoff TASK-629

## Slice vertical

Slice 039 — Gateway Asaas e ciclo de assinatura

## Status final

done

## Decisões preservadas

- Novas assinaturas Asaas aceitam apenas cartão de crédito e PIX.
- `SubscriptionPaymentMethod` mantém `boleto` exclusivamente para retomar/exibir checkout histórico; `CheckoutPaymentMethod` restringe a criação.
- Não houve cancelamento ou migração de boletos existentes.

## Contexto efetivamente usado

- Task 629, Slice 039, contrato de subscriptions, provider/serviço backend, gate web e specs focadas.

## Arquivos alterados

- Contrato, backend de subscriptions, gate/tipos web e documentação de pagamento.

## Validações executadas

- Builds backend e front-end; 36 testes Jest e 4 testes Vitest passaram.

## Pendências ou bloqueios

- Nenhuma.

## Próximo contexto recomendado

- Nenhum para esta mudança. Para evolução de pagamentos, começar pela Task 629 e pelo Slice 039.
