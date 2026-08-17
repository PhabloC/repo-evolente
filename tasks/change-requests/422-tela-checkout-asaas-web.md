# Task 422 - Tela de checkout Asaas na web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Slice vertical

- `tasks/slices/039-gateway-asaas-assinatura.md`

## Criterios de aceite

- [x] Remove CTA “pagamento simulado” (botão “Pagar com Asaas”)
- [x] Valores R$ 79 / R$ 49
- [x] Abre checkout Asaas (invoiceUrl) com cartão/PIX/boleto
- [x] Poll de status após retorno/checkout
- [x] Responsável mantém CTA app após pagamento
- [x] Pending/awaiting com feedback
- [x] Master isento (sem mudança)

## Resultado da execucao

- Gate cria checkout, abre URL Asaas, aguarda confirmação por poll/webhook
- Fallback fake: confirma via `/confirm` se provider=fake

## Handoff

- `.agents/state/handoffs/TASK-422.md`

## Status final

done
