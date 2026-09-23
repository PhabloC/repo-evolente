# Slice 061 - Deploy das lojas mobile

## Objetivo de negócio

Disponibilizar uma versão de produção do Evolente para distribuição Android e iOS.

## Entrega verificável

Builds de produção Android e iOS concluídas no EAS; Android enviado ao teste interno da Google Play e iOS enviado ao App Store Connect/TestFlight, quando as credenciais das lojas estiverem disponíveis.

## Fora de escopo

- Alterar funcionalidades ou telas do aplicativo.
- Aprovar a publicação pública nas lojas.
- Configurar contas, certificados ou secrets que não estejam acessíveis nesta sessão.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/720-deploy-mobile-lojas.md`

## Contexto sob demanda

- `mobile/app.json`, `mobile/app.config.js` e `mobile/eas.json`: validar identificadores, versão, perfis e ambiente de produção.
- `mobile/docs/ai/QA.md`: executar as validações mínimas antes do build.
- Estado das builds e credenciais no EAS: identificar se é possível gerar e submeter os artefatos.

## Risco de contexto

Baixo: operação de build e distribuição, sem alteração de código ou API.

## Status

blocked
