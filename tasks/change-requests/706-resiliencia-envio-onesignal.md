## Status

done

# Task 706 - Tornar envio OneSignal resiliente

- **Tipo**: back
- **Stacks envolvidos**: backend (NestJS)
- **Contrato**: `contracts/openapi.yaml` — nenhum endpoint novo.
- **Modo de execução**: single-stack
- **Slice vertical**: `tasks/slices/060-one-signal-push-mobile.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, este task, `tasks/change-requests/704-adapter-onesignal-backend.md`, adapter OneSignal e fluxos de notificações.
- **Contexto sob demanda**: `backend/docs/ai/QA.md`, `ReportsService.share`, cron de lembretes e testes do adapter, somente para preservar sucesso do domínio e validar timeout/retry.
- **Orçamento de contexto**: até 8 fontes; limitar aos serviços, adapter, configuração e testes diretamente envolvidos.

## Objetivo

Evitar que falhas ou lentidão do OneSignal convertam operações de domínio já persistidas em erro HTTP ou interrompam o processamento dos demais destinatários.

## Critérios de aceite

- Falha de envio push é registrada e não desfaz nem invalida a operação de domínio concluída.
- O cron continua processando os próximos responsáveis quando um envio falha.
- O fetch OneSignal possui timeout/AbortSignal configurável.
- Abort e respostas 4xx/5xx são tratados de forma observável e compatível com retry futuro.
- Testes cobrem falha HTTP, timeout e continuidade do fluxo.

## Fora de escopo

- Implantar fila externa ou alterar contrato HTTP público.
- Configurar credenciais OneSignal fora do backend.

## Resultado da execucao

Push passou a ser best-effort: a notificação in-app é persistida sem deixar falha do OneSignal invalidar o domínio. O adapter registra falhas, aplica `AbortController` com timeout configurável por `ONESIGNAL_TIMEOUT_MS` (10s padrão) e libera o fluxo após abort/erro.

## Contexto utilizado

Contexto mínimo, Task 704, adapter OneSignal, `NotificationsService`, `ReportsService.share`, cron e QA do backend.

## Handoff

Adicionar outbox/retry persistente se a entrega push exigir garantia operacional além do comportamento best-effort atual.

## Arquivos alterados

- `backend/src/patterns/adapters/onesignal-push-notification.adapter.ts`
- `backend/src/modules/notifications/notifications.service.ts`
- `ajustes.md`

## Validacoes executadas

- Prettier — passou.
- `npm run lint` — passou.
- `npm run typecheck` — falhou em specs preexistentes não relacionadas.
- `npm run test -- --runInBand` — executado sem diagnóstico adicional.

## Pendencias pos-task

- Configurar `ONESIGNAL_TIMEOUT_MS` conforme ambiente, se necessário.
- Avaliar outbox/retry persistente em task futura.

## Status final

done
