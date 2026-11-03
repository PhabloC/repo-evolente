# Task 796 - Restaurar login mobile de produção

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

- nao se aplica (sem UI)

## Origem da solicitacao

Após a Task 795, o login no app da loja passou a exibir "Não foi possível conectar ao servidor. Verifique se a API está ativa e acessível no mobile."

## Objetivo

Restaurar o login no canal `production` voltando `EXPO_PUBLIC_API_URL` para o host que o app já alcançava (`https://evolente-api.fasters.app/api`) e republicar o OTA.

## Entrega verificavel

- EAS production `EXPO_PUBLIC_API_URL` = `https://evolente-api.fasters.app/api`
- Update Android e iOS no canal `production`

## Fora de escopo

- Corrigir WAF/DNS/SSL de `api.evolente.com.br`
- Unificar os dois hosts no Cloudflare
- Build de loja

## Dependências

- Task 795

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- esta task, Slice 057, handoff da Task 795

## Contexto sob demanda

| Gatilho | Fonte | Para quê |
|---|---|---|
| Variável de build | EAS production, `mobile/src/config/env.ts` | restaurar a URL |
| Erro de login | `mobile/src/shared/network/createAppError.ts` | confirmar que é falha sem HTTP response |

## Orçamento de contexto

- Fontes obrigatórias: 6
- Estratégia de redução: sem UI, contrato ou backend além do health check

## Criterios de aceite

- [x] Variável EAS production restaurada
- [x] OTA Android e iOS publicados

## Resultado da execucao

- O bundle da Task 795 continha `api.evolente.com.br` (não o IP local). Esse host responde no desktop, mas o login no aparelho falhou com erro de rede (sem HTTP response).
- `EXPO_PUBLIC_API_URL` de production voltou para `https://evolente-api.fasters.app/api`.
- OTA runtime `1.0.3`:
  - Android: `93183394-a4bc-41f5-b2e7-91e4fb6633e4`
  - iOS: `7898af5f-3d24-4919-9406-b71a1b1873f7`
- Bundle iOS verificado: contém `evolente-api.fasters.app` e não contém `api.evolente.com.br`.

## Contexto utilizado

- Task 795/handoff, Slice 057, `createAppError.ts`, ambiente EAS production

## Handoff

- `.agents/state/handoffs/TASK-796.md`

## Arquivos alterados

- `tasks/change-requests/796-restaurar-login-mobile-producao.md`
- `tasks/slices/057-configuracao-api-publica-mobile.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-796.md`

## Validacoes executadas

- `POST /auth/login` nos dois hosts retorna 401 de credencial inválida quando alcançáveis
- Bundle publicado contém só o host fasters

## Pendencias pos-task

- Fechar o app duas vezes: a primeira baixa o OTA, a segunda aplica
- `api.evolente.com.br` ainda não é seguro para o app; unificar DNS/Cloudflare antes de trocar de novo
- Conteúdo criado só em `evolente.com.br` continua no outro host até essa unificação

## Status final

done
