# Slice 059 - Estabilidade nativa Expo para iOS

## Objetivo de negócio

Permitir que o aplicativo instalado via TestFlight abra normalmente em iPhone.

## Entrega verificável

Os módulos nativos Expo estão alinhados à versão do SDK, a dependência obrigatória de áudio está instalada e novas builds de loja são iniciadas.

## Fora de escopo

- Alterar fluxos, telas ou regras de negócio.
- Publicar ou distribuir as builds nas lojas.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/633-corrigir-incompatibilidade-nativa-expo-ios.md`

## Contexto sob demanda

- `errors_testflight/crashlog.crash`: confirmar o módulo nativo incompatível.
- `mobile/package.json` e `mobile/package-lock.json`: alinhar dependências do SDK.
- `mobile/app.json`: revisar os avisos de configuração encontrados pelo Expo Doctor.
- `mobile/docs/ai/QA.md`: validar a correção da stack móvel.

## Risco de contexto

Médio: atualiza versões nativas compatíveis dentro do mesmo SDK; requer novas builds Android e iOS.

## Status

in_progress
