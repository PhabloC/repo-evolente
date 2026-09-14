# Task 652 - Configurar webhook Asaas para produção

## Status

blocked

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `POST /subscriptions/webhooks/asaas`
- URL pública: `https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas`

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura (`tasks/slices/039-gateway-asaas-assinatura.md`)

## Objetivo

Preparar e validar a configuração de produção do backend para que o webhook do Asaas seja cadastrado no ambiente de produção, sem depender do endereço ngrok.

## Escopo

- Registrar as variáveis de produção necessárias sem expor segredos no repositório.
- Confirmar a URL pública final do webhook.
- Validar que o backend publicado responde no path `/api/subscriptions/webhooks/asaas`.
- Documentar a configuração que precisa ser aplicada no provedor de deploy e no painel do Asaas.

## Fora de escopo

- Alterar código do fluxo de assinatura ou do processamento de eventos.
- Publicar valores reais de `PAYMENT_GATEWAY_API_KEY` ou `PAYMENT_GATEWAY_WEBHOOK_SECRET`.

## Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `backend/.env.example`
- `backend/src/modules/subscriptions/subscriptions.controller.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`

## Contexto sob demanda

- `contracts/openapi.yaml#/paths/~1subscriptions~1webhooks~1asaas` para validar o contrato do endpoint.
- `backend/docs/ai/SECURITY.md` para validar que nenhum segredo seja commitado ou logado.
- `ASAAS-CHECKOUT-PAGAMENTO.md` para confirmar o procedimento operacional documentado.

## Orcamento de contexto

baixo; carregar apenas configuração, endpoint, contrato e documentação operacional diretamente relacionados.

## Criterios de aceite

- [ ] URL final documentada como `https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas`.
- [ ] Backend de produção configurado com `PAYMENT_PROVIDER=asaas`, `ASAAS_ENV=production`, `APP_PUBLIC_URL=https://evolente.fasters.app` e segredos fornecidos somente pelo ambiente de deploy.
- [ ] Painel do Asaas de produção usa a mesma URL e o mesmo token de `PAYMENT_GATEWAY_WEBHOOK_SECRET`.
- [ ] Endpoint público validado sem depender do ngrok.

## Dependencias

- Deploy/ops deve permitir editar variáveis do backend e reiniciá-lo.
- A conta/chave do Asaas de produção deve estar disponível.

## Resultado da execucao

- URL final confirmada: `https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas`.
- `POST` público sem token respondeu `401` com `Token de acesso asaas-access-token inválido`, confirmando que o host, prefixo `/api` e rota estão publicados; não houve `404`.
- O repositório não contém credenciais nem acesso ao provedor de deploy/painel Asaas para aplicar `ASAAS_ENV=production` ou trocar o webhook remotamente.

## Contexto utilizado

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `backend/.env.example`
- `backend/docs/ai/SECURITY.md`
- `contracts/openapi.yaml#/paths/~1subscriptions~1webhooks~1asaas`
- `ASAAS-CHECKOUT-PAGAMENTO.md` (variáveis e procedimento de produção)
- `backend/src/modules/subscriptions/subscriptions.controller.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`

## Handoff

- `.agents/state/handoffs/TASK-652.md`

## Arquivos alterados

- `tasks/change-requests/652-configurar-webhook-asaas-producao.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-652.md`

## Validacoes executadas

- `POST https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas` sem token — `401`, rota pública alcançável e autenticação ativa.
- Revisão do contrato OpenAPI e documentação operacional — URL e header confirmados.

## Pendencias pos-task

- No ambiente de deploy do backend, definir `PAYMENT_PROVIDER=asaas`.
- Definir `ASAAS_ENV=production`.
- Definir `APP_PUBLIC_URL=https://evolente.fasters.app`.
- Usar a API Key de produção do Asaas em `PAYMENT_GATEWAY_API_KEY`.
- Definir um valor secreto em `PAYMENT_GATEWAY_WEBHOOK_SECRET` e usar exatamente o mesmo token no webhook de produção do Asaas.
- Reiniciar/redeployar o backend após salvar as variáveis.
- No painel Asaas de produção, cadastrar `https://evolente-api.fasters.app/api/subscriptions/webhooks/asaas`, ativar a fila e enviar um evento de teste.

## Status final

blocked
