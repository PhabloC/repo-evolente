# Handoff Task 695

- Slice: `tasks/slices/060-cartao-debito-assinatura.md`
- Status final: done
- Decisão: débito é disponibilizado pelo Asaas dentro do fluxo/fatura de cartão; não existe enum `debit_card` separado para o checkout recorrente.
- Contexto usado: provider Asaas, contrato OpenAPI, gate web, docs oficiais do Asaas e Task 629.
- Arquivos alterados: gate web, provider Asaas, contrato OpenAPI e documentação de pagamento.
- Validações: 38 testes backend aprovados; lint front-end aprovado.
- Pendência: confirmar a opção de débito em uma cobrança sandbox com cliente elegível.
- Próximo contexto: painel Asaas sandbox, checkout gerado e webhook já configurado.
