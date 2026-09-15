# Handoff Task 702

- Slice: `tasks/slices/060-cartao-debito-assinatura.md`
- Status final: done
- Decisão: remover `autoRedirect=true` das URLs e do callback de assinaturas PIX; a página Asaas deve permanecer aberta para o pagamento.
- Contexto usado: provider Asaas, teste do provider, Task 696 e fluxo PIX hospedado.
- Arquivos alterados: `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`, `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts`.
- Validação: suíte do provider aprovada, 15 testes.
- Pendências: nenhuma.
- Próximo contexto: validar manualmente em sandbox com uma cobrança PIX real.
