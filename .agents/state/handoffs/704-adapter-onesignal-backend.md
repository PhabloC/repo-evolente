# Handoff Task 704

- Slice: 060 — Push OneSignal no mobile
- Status final: done
- Decisões: adapter usa REST API `https://api.onesignal.com/notifications`, direciona por `external_id` e só é selecionado com as duas variáveis configuradas.
- Arquivos: `onesignal-push-notification.adapter.ts` e `notifications.module.ts`.
- Validação: lint ok; typecheck bloqueado por falhas preexistentes em specs não relacionadas.
- Pendências: secrets no ambiente e teste real do evento `report_shared`.
