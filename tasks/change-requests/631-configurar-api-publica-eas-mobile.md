# Task 631 - Configurar API pública no EAS para mobile

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile (Expo / React Native)

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim

## Contrato

Aplicável sem alteração: a base da API deve manter o prefixo `/api` do backend existente.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/057-configuracao-api-publica-mobile.md`

## Objetivo

Configurar a URL pública da API no ambiente `production` do EAS e gerar uma build Android que a incorpore.

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/057-configuracao-api-publica-mobile.md`

## Contexto sob demanda

- `mobile/eas.json` e `mobile/src/config/env.ts`: configurar e validar o consumo da variável de build.
- `backend/src/main.ts`: confirmar o prefixo público `/api`.
- endpoint público `https://evolente-api.fasters.app/api`: confirmar que responde pela API antes da configuração.

## Orçamento de contexto

Baixo (até 8 fontes). Estratégia: limitar a mudança ao ambiente EAS, à configuração Expo e à validação do endpoint público.

## Critérios de aceite

- [ ] `EXPO_PUBLIC_API_URL` está definida para `production` no EAS.
- [ ] O perfil `production` seleciona explicitamente o ambiente `production`.
- [ ] Uma build Android de loja é iniciada com a variável disponível.

## Dependências

- Slice 010 — concluído; usa integração mobile existente.

## Resultado da execucao

- Confirmada a API Nest pública em `https://evolente-api.fasters.app/api`; a resposta JSON em `GET /api` confirma o prefixo, mesmo sem rota raiz.
- Criada no EAS a variável `EXPO_PUBLIC_API_URL` no ambiente `production`, com a URL pública da API.
- O perfil EAS `production` passou a selecionar explicitamente o ambiente `production`.
- Iniciada a build Android de loja `1.0.0 (4)` com a variável carregada.

## Contexto utilizado

- Contexto mínimo da raiz, esta task e o Slice 057.
- `mobile/eas.json` e `mobile/src/config/env.ts` para configuração e consumo da variável.
- `backend/src/main.ts` e o endpoint público para confirmar o prefixo `/api`.
- Documentação oficial do EAS para o comando e visibilidade da variável.

## Handoff

- `.agents/state/handoffs/TASK-631.md`

## Arquivos alterados

- `mobile/eas.json`
- `tasks/slices/057-configuracao-api-publica-mobile.md`
- `tasks/change-requests/631-configurar-api-publica-eas-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-631.md`

## Validacoes executadas

- `curl https://evolente-api.fasters.app/api` retornou JSON 404 do Nest, confirmando que o host atende a API e que o prefixo `/api` é válido.
- `eas env:set` criou `EXPO_PUBLIC_API_URL` em `production`.
- A saída da build EAS confirmou o carregamento de `EXPO_PUBLIC_API_URL` e iniciou a build Android `749c5b96-ced8-4da2-8931-5c8f043dc276` (versionCode 4).

## Pendencias pos-task

- Aguardar a conclusão da build EAS, baixar o AAB e publicar a versão 4 na faixa de teste interno da Google Play.

## Status final

done
