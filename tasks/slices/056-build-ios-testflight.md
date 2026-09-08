# Slice 056 - Build iOS para TestFlight

## Objetivo de negócio

Permitir a distribuição do aplicativo Evolente para testes no TestFlight.

## Entrega verificável

Os assets nativos iOS são aceitos pelo prebuild do Expo e uma build de produção pode ser iniciada no EAS.

## Fora de escopo

- Alterar telas ou comportamento do app.
- Publicar versão na App Store.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/630-corrigir-assets-ios-testflight.md`

## Contexto sob demanda

- `mobile/app.json` e `mobile/assets/logo-seal.webp`: converter asset incompatível e atualizar as referências nativas.
- `mobile/docs/ai/AGENTS.md`: regras locais de configuração mobile.

## Risco de contexto

Baixo: a correção se limita aos assets de build e à configuração Expo.

## Status

blocked
