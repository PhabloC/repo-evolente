# Slice 057 - Configuração da API pública no mobile

## Objetivo de negócio

Permitir que a versão Android distribuída pelo Google Play consuma a API pública do Evolente.

## Entrega verificável

O perfil de produção do EAS recebe `EXPO_PUBLIC_API_URL` com a URL pública da API. A URL vigente no app da loja é `https://api.evolente.com.br/api` (Task 797, após o humano confirmar JSON no Chrome).

## Fora de escopo

- Alterar endpoints, contrato OpenAPI ou backend.
- Publicar a build na Google Play.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/change-requests/631-configurar-api-publica-eas-mobile.md`
- `tasks/change-requests/795-apontar-mobile-producao-api-evolente.md` — done; tentativa de `api.evolente.com.br` quebrou o login no aparelho
- `tasks/change-requests/796-restaurar-login-mobile-producao.md` — done; rollback temporário para fasters
- `tasks/change-requests/797-apontar-mobile-api-evolente-apos-teste-chrome.md` — done; URL vigente = `https://api.evolente.com.br/api`

## Contexto sob demanda

- `mobile/eas.json` e `mobile/src/config/env.ts`: assegurar o ambiente de build e o consumo da variável.
- `backend/src/main.ts`: confirmar o prefixo `/api` da API pública.

## Risco de contexto

Baixo: mudança limitada à configuração de build e à URL pública já implantada.

## Status

done
