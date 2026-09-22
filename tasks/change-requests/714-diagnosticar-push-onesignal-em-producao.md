# Task 714 - Diagnosticar e corrigir push OneSignal em produção

## Status

done

## Objetivo

Garantir que os builds publicados do app responsável registrem a assinatura push no OneSignal e que o backend envie notificações para o mesmo usuário identificado, sem expor segredos no mobile.

## Tipo

shared

## Stacks envolvidos

mobile (Expo/EAS), backend (NestJS)

## Contrato

Não aplicável; a integração usa o SDK OneSignal e a REST API do provedor, sem endpoint público novo.

## Modo de execução

cross-stack

## Slice vertical

`tasks/slices/060-one-signal-push-mobile.md` (correção incremental do fluxo existente).

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/060-one-signal-push-mobile.md`
- `mobile/src/shared/notifications/oneSignal.ts`
- `mobile/src/config/env.ts`
- `mobile/app.config.js`
- `backend/src/patterns/adapters/onesignal-push-notification.adapter.ts`
- `backend/src/modules/notifications/notifications.module.ts`

## Contexto sob demanda

- `mobile/docs/ai/QA.md`: validar build/configuração Expo.
- `backend/docs/ai/QA.md`: validar adapter e testes backend.
- configuração EAS/OneSignal/APNs/FCM somente para verificar variáveis e credenciais de produção, sem carregar segredos.
- documentação oficial OneSignal: confirmar `login(external_id)` e `include_aliases.external_id`.

## Orçamento de contexto

Até 8 fontes; limitar a configuração nativa, registro da assinatura, seleção do adapter e envio REST, sem carregar telas ou módulos não relacionados.

## Critérios de aceite

- build production recebe App ID público do OneSignal e inicializa o SDK.
- backend production seleciona o adapter OneSignal somente com credenciais presentes.
- usuário autenticado aparece no OneSignal com o mesmo `external_id` usado no backend.
- falhas de configuração/env ficam observáveis sem expor a API key ao cliente.
- testes cobrem a configuração/seleção relevante.

## Dependências

- Tasks 703, 704, 705 e 706, concluídas.

## Status final

done

## Resultado da execucao

O build EAS agora falha explicitamente em `preview`/`production` quando `EXPO_PUBLIC_ONESIGNAL_APP_ID` não foi configurado, evitando publicar um app que nunca inicializa o SDK. Os exemplos de ambiente foram atualizados com o App ID público mobile e as credenciais server-side do backend.

Auditoria local: `ONESIGNAL_APP_ID` do backend e `EXPO_PUBLIC_ONESIGNAL_APP_ID` do mobile estão presentes e coincidem. O `.env` mobile local aponta `EXPO_PUBLIC_API_URL` para `192.168.2.143`, adequado apenas à rede local; o build publicado precisa receber a URL pública da API via ambiente EAS.

## Contexto utilizado

- `mobile/app.config.js`, `mobile/.env.example`, `mobile/src/config/env.ts`
- `backend/src/patterns/adapters/onesignal-push-notification.adapter.ts`
- `backend/src/modules/notifications/notifications.module.ts`
- Tasks/handoffs 703–706
- Documentação OneSignal sobre `login`/`external_id` e `include_aliases`

## Handoff

Antes de gerar novo build, cadastrar `EXPO_PUBLIC_ONESIGNAL_APP_ID` no ambiente EAS usado pelo perfil. No backend publicado, cadastrar `ONESIGNAL_APP_ID` e `ONESIGNAL_REST_API_KEY`. Depois, abrir o app, aceitar permissão de notificações e confirmar no painel OneSignal que o usuário possui subscription push e `external_id` igual ao UUID da sessão.

## Arquivos alterados

- `mobile/app.config.js`
- `mobile/.env.example`
- `backend/.env.example`
- `tasks/change-requests/714-diagnosticar-push-onesignal-em-producao.md`
- `tasks/slices/060-one-signal-push-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/714-diagnosticar-push-onesignal-em-producao.md`

## Validacoes executadas

- `EAS_BUILD_PROFILE=development node -e "require('./app.config.js')"` — passou sem App ID.
- `EAS_BUILD_PROFILE=production node -e "require('./app.config.js')"` sem App ID — falhou explicitamente com mensagem de configuração.
- configuração production com App ID — plugin OneSignal em modo `production` e entitlement iOS `aps-environment=production`.
- auditoria sem exibir segredos — App IDs coincidem; REST API key presente apenas no backend local.
- `git diff --check` — passou.

## Pendencias pos-task

- Configurar as variáveis no EAS/OneSignal/backend, fora do repositório.
- Configurar `EXPO_PUBLIC_API_URL` de produção no ambiente EAS; o `.env` local usa endereço privado `192.168.2.143`.
- Gerar novos builds Android/iOS após configurar o App ID e testar entrega real.
