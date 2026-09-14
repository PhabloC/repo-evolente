# Handoff Task 652

- Slice: 039 - Gateway Asaas e ciclo de assinatura
- Status final: blocked
- Decisão: o webhook de produção deve usar `https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas`; o front público para callbacks é `https://evolente.fasters.app`.
- Validação: POST sem token no endpoint publicado respondeu 401, confirmando rota e autenticação.
- Arquivos alterados: task 652 e índice.
- Pendência: aplicar variáveis de produção no deploy e cadastrar/ativar o webhook na conta Asaas de produção.
- Próximo contexto: painel de deploy do backend e Integrações → Webhooks da conta Asaas de produção.
