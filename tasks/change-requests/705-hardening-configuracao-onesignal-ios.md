## Status

done

# Task 705 - Endurecer runtime e configuração de produção do OneSignal

- **Tipo**: mobile
- **Stacks envolvidos**: mobile (Expo/EAS)
- **Perfil do projeto**: stack web `front-end` (React/Vite); mobile `sim` (Expo)
- **Contrato**: não aplicável; mudança somente de configuração nativa/build.
- **Modo de execução**: single-stack
- **Slice vertical**: `tasks/slices/059-estabilidade-nativa-expo-ios.md` e `tasks/slices/060-one-signal-push-mobile.md` (escopo de configuração nativa compartilhado)
- **Contexto mínimo**: `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`, `mobile/app.json`, `mobile/eas.json`, `mobile/src/app/AppBootstrap.tsx`.
- **Contexto sob demanda**: `mobile/docs/ai/QA.md`; documentação local de configuração Expo/EAS e os arquivos de dependência do mobile, somente para validar a configuração final.
- **Orçamento de contexto**: até 8 fontes; limitar a configuração Expo/EAS e validações mobile, sem carregar front-end ou backend.

## Objetivo

Corrigir os riscos apontados no code review em `ajustes.md`: impedir OTA incompatível após a inclusão de módulo nativo e alinhar OneSignal/APNs ao perfil de build do EAS.

## Critérios de aceite

- A versão/runtime do app é incrementada para que a mudança nativa não seja entregue a instalações antigas via OTA.
- O build `development` usa configuração de desenvolvimento do OneSignal/APNs.
- Os builds `preview` e `production` usam modo de produção do OneSignal e entitlement `aps-environment: production`.
- A configuração permanece determinística durante `expo config`/EAS e não inclui segredos.
- `npm run lint`, `npm run typecheck` e `npm run test` são executados, registrando falhas preexistentes quando houver.

## Fora de escopo

- Publicação de builds ou configuração de credenciais no painel OneSignal/Apple.
- Alteração do bootstrap funcional do SDK ou do backend.

## Resultado da execucao

Incrementada a versão Expo para `1.0.1` e adicionada configuração dinâmica por `EAS_BUILD_PROFILE`. O perfil `development` mantém OneSignal/APNs em desenvolvimento; `preview` e `production` usam OneSignal production e `aps-environment: production`.

## Contexto utilizado

Contexto mínimo da raiz, Slice 059/060, `mobile/app.json`, `mobile/eas.json`, `mobile/src/app/AppBootstrap.tsx` e `mobile/docs/ai/QA.md`.

## Handoff

Antes de publicar TestFlight, configurar/confirmar credenciais APNs de produção no OneSignal e executar um build EAS de distribuição.

## Arquivos alterados

- `ajustes.md`
- `mobile/app.json`
- `mobile/app.config.js`
- `tasks/000-index.md`

## Validacoes executadas

- `npx expo config --json` em development e production — passou; perfis conferidos.
- `npm run lint` — passou.
- `npm run typecheck` — passou.
- `npm run test -- --runInBand` — passou (1 suíte).

## Pendencias pos-task

- Configurar/confirmar credenciais APNs/OneSignal fora do repositório.
- Executar build EAS e validar entrega real no TestFlight.

## Status final

done
