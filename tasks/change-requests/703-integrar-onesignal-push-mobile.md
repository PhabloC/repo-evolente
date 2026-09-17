## Resultado da execucao

Configurado o SDK OneSignal no Expo/EAS, com App ID por ambiente, inicialização única no bootstrap e associação automática ao usuário autenticado. O backend permanece com adapter noop até a configuração da REST API key e definição do envio server-side.

## Contexto utilizado

Contexto mínimo da raiz, configuração Expo/EAS, bootstrap/sessão mobile, adapter de push backend e documentação oficial do OneSignal para Expo.

## Handoff

O próximo incremento deve implementar `OneSignalPushNotificationAdapter` no backend e configurar a API key por ambiente. Validar também `aps-environment` de produção antes do TestFlight.

## Arquivos alterados

- `mobile/package.json`
- `mobile/package-lock.json`
- `mobile/app.json`
- `mobile/src/config/env.ts`
- `mobile/src/shared/notifications/oneSignal.ts`
- `mobile/src/app/AppBootstrap.tsx`
- `mobile/src/app/AppGate.tsx`

## Validacoes executadas

- `npm run typecheck` — falhou por erros preexistentes em arquivos de jogos/admin/trilha; nenhum erro nos arquivos OneSignal.
- `npm run lint` — executado sem diagnóstico adicional.

## Pendencias pos-task

- Criar App IDs e credenciais APNs/FCM no OneSignal.
- Implementar adapter server-side com REST API key em secret de ambiente.
- Testar em development build EAS; Expo Go não suporta push OneSignal.

## Status final

done

# Task 703 - Integrar OneSignal para push mobile

- **Tipo**: shared
- **Stacks envolvidos**: mobile (Expo), backend (NestJS)
- **Contrato**: `contracts/openapi.yaml` — sem endpoint novo neste primeiro incremento; o adapter usa o identificador externo do usuário.
- **Modo de execução**: cross-stack
- **Slice vertical**: `tasks/slices/060-one-signal-push-mobile.md`
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, slice 060, `mobile/src/app/AppBootstrap.tsx`, `mobile/src/app/providers/AppProviders.tsx`, adapter de push do backend.
- **Contexto sob demanda**: docs locais de mobile e backend para padrões de configuração/serviço; `mobile/app.json`, `mobile/src/config/env.ts`, autenticação e módulo de notificações; documentação oficial OneSignal Expo para requisitos do plugin.
- **Orçamento de contexto**: até 8 fontes; carregar somente arquivos diretamente envolvidos e paths relevantes.

## Critérios de aceite

- OneSignal instalado e configurado via Expo plugin.
- App ID lido de variável pública de ambiente, sem segredo no código.
- SDK inicializado uma única vez no bootstrap nativo.
- Usuário autenticado identificado e logout desvincula a sessão do SDK.
- Clique/recebimento não quebra o fallback in-app.
- Backend mantém adapter abstrato e possui implementação OneSignal configurável por ambiente.
- `npm run lint`, `npm run typecheck` e testes relevantes executados nas stacks alteradas.
