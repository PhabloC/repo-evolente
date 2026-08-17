# Handoff - Task 422

## Task

- identificador: 422
- status final: done

## Decisões preservadas

- Botão “Pagar com Asaas” abre `invoiceUrl` em nova aba
- Poll a cada 4s em `awaiting-payment` até `accessGranted`
- Fake: create checkout + confirm no mesmo fluxo

## Próxima ação

- Configurar webhook Asaas (token em `.env`)
- Task 423 cancel/reembolso UI
- Testar checkout real no sandbox
