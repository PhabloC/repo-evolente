# Task 795 - Apontar o mobile de produção para api.evolente.com.br

## Status

done

## Tipo

mobile

## Stacks envolvidos

- mobile

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

nao se aplica (só troca a URL base já contratada; prefixo `/api` permanece)

## Modo de execucao

single-stack

## Slice vertical

- Slice 057 — `tasks/slices/057-configuracao-api-publica-mobile.md`

## Referencia de design system

- nao se aplica (sem UI)

## Origem da solicitacao

Pedido humano: conteúdo criado no frontend de produção (`evolente.com.br`) não aparece no app da loja. Diagnóstico: o site grava em `https://api.evolente.com.br/api` e o EAS production ainda usava `https://evolente-api.fasters.app/api`.

## Objetivo

Atualizar `EXPO_PUBLIC_API_URL` no ambiente EAS `production` para `https://api.evolente.com.br/api` e publicar o bundle no canal `production` para o app da loja passar a ler o mesmo backend da web.

## Entrega verificavel

- Variável EAS `production` `EXPO_PUBLIC_API_URL` = `https://api.evolente.com.br/api`
- Update publicado no canal `production` (ou build de loja, se o update não for suficiente)
- `GET https://api.evolente.com.br/api` responde como Nest (`/api` válido)

## Fora de escopo

- Alterar endpoints, contrato ou backend
- Trocar a API do `.env` local de desenvolvimento
- Publicar binário novo nas lojas, salvo se o OTA não puder carregar a variável

## Dependências

- Task 631 (configuração inicial da API pública no EAS)

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 057

## Contexto sob demanda

| Gatilho | Fonte | Para quê |
|---|---|---|
| Variável de build | ambiente EAS `production`, `mobile/eas.json`, `mobile/src/config/env.ts` | gravar e consumir a URL |
| Prefixo público | `GET https://api.evolente.com.br/api` | confirmar que o host atende a API |

## Orçamento de contexto

- Fontes obrigatórias: 6
- Estratégia de redução: não carregar UI, contrato OpenAPI, design-system nem docs/ai

## Criterios de aceite

- [x] Endpoint `https://api.evolente.com.br/api` confirma prefixo Nest
- [x] `EXPO_PUBLIC_API_URL` de production no EAS aponta para essa URL
- [x] Bundle publicado no canal `production` com a variável carregada

## Resultado da execucao

- Confirmado o host Nest em `https://api.evolente.com.br/api`.
- `eas env:set` atualizou `EXPO_PUBLIC_API_URL` de production de `https://evolente-api.fasters.app/api` para `https://api.evolente.com.br/api`.
- OTA publicado no canal `production`, runtime `1.0.3`:
  - Android: grupo `b920a2fe-8b23-4af8-9753-63830991d7bc`
  - iOS: grupo `dff7e6f9-f6d5-468c-b9d1-91b4c545970a`
- `--platform all` falhou no export web (`image/webp`); publicação feita por plataforma nativa.

## Contexto utilizado

- Governança da raiz, índice, esta task e Slice 057
- `mobile/eas.json`, `mobile/src/config/env.ts`
- Ambiente EAS `production` e endpoint público da nova API

## Handoff

- `.agents/state/handoffs/TASK-795.md`

## Arquivos alterados

- `tasks/change-requests/795-apontar-mobile-producao-api-evolente.md`
- `tasks/slices/057-configuracao-api-publica-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-795.md`

## Validacoes executadas

- `GET https://api.evolente.com.br/api` retorna JSON Nest 404 (`Cannot GET /api`), prefixo válido
- `eas env:list production` mostra `EXPO_PUBLIC_API_URL=https://api.evolente.com.br/api`
- `eas update` Android e iOS concluídos com a variável de production carregada

## Pendencias pos-task

- Fechar e reabrir o app da loja (ou aguardar o fetch do Expo Updates) para baixar o OTA
- Conteúdo novo da biblioteca web ainda precisa ser adicionado à trilha da semana para aparecer em Atividades / Hoje
- `evolente.fasters.app` continua no host antigo; o site oficial é `evolente.com.br`
- Próximo `eas build` de loja já herda a URL nova; se for build de produção, incrementar `expo.version`

## Status final

done
