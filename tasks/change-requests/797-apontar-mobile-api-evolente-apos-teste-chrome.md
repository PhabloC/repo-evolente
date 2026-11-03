# Task 797 - Apontar o mobile para api.evolente.com.br após teste no Chrome

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

nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 057 — `tasks/slices/057-configuracao-api-publica-mobile.md`

## Referencia de design system

- nao se aplica

## Origem da solicitacao

Humano confirmou que `https://api.evolente.com.br/api` devolve JSON no Chrome. Pedido: o app deve puxar dessa API.

## Objetivo

Atualizar `EXPO_PUBLIC_API_URL` de production para `https://api.evolente.com.br/api` e publicar OTA Android/iOS.

## Fora de escopo

- Alterar Cloudflare/WAF
- Build de loja

## Dependências

- Task 795, Task 796

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 057

## Contexto sob demanda

- EAS production, `mobile/src/config/env.ts`

## Orçamento de contexto

- Fontes obrigatórias: 6
- Estratégia: só EAS/OTA

## Criterios de aceite

- [x] EAS production aponta para `https://api.evolente.com.br/api`
- [x] OTA Android e iOS publicados

## Resultado da execucao

- `EXPO_PUBLIC_API_URL` de production = `https://api.evolente.com.br/api`
- OTA runtime `1.0.3`:
  - Android: `04b5c590-5616-4303-8d2a-d406e92ea461`
  - iOS: `54d94927-07a0-4b40-9e40-8d2d3cc4c5dd`
- Bundle contém `api.evolente.com.br`

## Contexto utilizado

- Slice 057, EAS production

## Handoff

- `.agents/state/handoffs/TASK-797.md`

## Arquivos alterados

- `tasks/change-requests/797-apontar-mobile-api-evolente-apos-teste-chrome.md`
- `tasks/slices/057-configuracao-api-publica-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-797.md`

## Validacoes executadas

- `eas env:set` e `eas update` Android/iOS
- String `api.evolente.com.br` presente no bundle

## Pendencias pos-task

- Fechar o app duas vezes e testar login
- Se o login falhar de novo, o Chrome liberou o host mas o cliente nativo (OkHttp) ainda pode estar bloqueado

## Status final

done
