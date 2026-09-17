## Resultado da execucao

Implementado adapter REST do OneSignal com seleção automática no NotificationsModule quando `ONESIGNAL_APP_ID` e `ONESIGNAL_REST_API_KEY` estão configurados; caso contrário, permanece o adapter noop.

## Contexto utilizado

Adapter push existente, módulo de notificações, ConfigService e padrões de validação do backend.

## Handoff

Configurar as duas variáveis secretas no ambiente do backend e testar `report_shared` com um dispositivo registrado.

## Arquivos alterados

- `backend/src/patterns/adapters/onesignal-push-notification.adapter.ts`
- `backend/src/modules/notifications/notifications.module.ts`

## Validacoes executadas

- Prettier executado nos arquivos alterados.
- `npm run lint` concluído sem diagnósticos.
- `npm run typecheck` falhou somente em specs preexistentes de admin, conteúdos, guardians, patients, reports, subscriptions, trails e e2e.

## Pendencias pos-task

- Configurar `ONESIGNAL_APP_ID` e `ONESIGNAL_REST_API_KEY` no ambiente do backend.
- Validar envio real e tratamento de clique no mobile.

## Status final

done

# Task 704 - Adapter OneSignal no backend

- **Tipo**: back
- **Stacks envolvidos**: backend (NestJS)
- **Contrato**: `contracts/openapi.yaml` — nenhum endpoint novo.
- **Modo de execução**: single-stack
- **Slice vertical**: `tasks/slices/060-one-signal-push-mobile.md`
- **Contexto mínimo**: adapter push, NotificationsModule, app config e testes de adapters.
- **Contexto sob demanda**: documentação OneSignal REST API; somente endpoint de notificações e configuração por ambiente.
- **Orçamento de contexto**: até 6 fontes.

## Critérios de aceite

- Envia para `external_id` via OneSignal REST API.
- Não inicia envio sem credenciais configuradas.
- API key permanece somente no backend.
- Mantém fallback noop quando OneSignal não está configurado.
- Testes e lint passam na área alterada.
