# Handoff TASK — retomada de checkout após F5

## Decisão
Após iniciar pagamento, F5 não deve voltar à escolha de meio nem criar nova cobrança. O gate consulta `POST /subscriptions/verify`, e se ainda houver `pending`, mostra aguardando com fatura retomada.

## Alterações
- Backend `createCheckout`: sem `forceNew`, retoma pendente (ou libera se Asaas já confirmou).
- `getStatus` / `verify` passam `pendingCheckout` (invoiceUrl etc.).
- Provider `resumeCheckout` (Asaas sessão de cartão + assinatura PIX/boleto).
- Front: load/poll usam verify; tela awaiting no pending; botão “Escolher outra forma” usa `forceNew`.

## Validação
- tsc backend/front OK
- jest: resumes pending checkout
- vitest: shows awaiting payment after refresh

## Próximo
Testar manualmente no sandbox: pagar cartão → voltar Evolente → F5 → deve ficar em aguardando / liberar se pago.
