# Task 812 - Botão falar com o suporte no login mobile

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

- nao se aplica

## Modo de execucao

single-stack

## Slice vertical

- Slice 002 - Autenticacao e recuperacao de senha
- `tasks/slices/002-autenticacao.md`

## Objetivo

Na tela de login do app mobile (incluindo iOS/Apple), oferecer o botão "Falar com o suporte" que abre o cliente de e-mail com destino `evolenteapp@gmail.com`.

## Escopo

- CTA na `SignInScreen` (telefone e tablet)
- Abrir `mailto:evolenteapp@gmail.com` via `Linking`
- Helper + teste unitário do mailto

## Fora de escopo

- Front-end web (já coberto pela Task 811 na assinatura)
- Backend / OpenAPI
- Tela de assinatura/paywall mobile
- Chat in-app

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

prints de telas + artefato documental

### Fonte primaria visual

- `design-system/mobile/prints/login-mobile.png` (layout atual do login)
- `design-system/mobile/Design_System_Evolente_App_Mobile.md` (botões, tokens, hit target)

### Regra de aderencia visual

- preservar layout, copy, campos, Entrar, biometria, “Criar conta”, “Esqueci minha senha” e versão
- lacuna do print: inserir CTA secundário “Falar com o suporte” sem redesign
- reutilizar `Button` ghost e padrão da Task 788

## Origem da solicitacao

Pedido direto após a Task 811: no Apple mobile, colocar o suporte na página de login (não na assinatura).

## Comportamento esperado

- Login exibe "Falar com o suporte"
- Toque abre o e-mail para `evolenteapp@gmail.com`
- Fluxo de autenticação e demais CTAs permanecem iguais

## Criterios de aceite

- [x] Botão "Falar com o suporte" no login mobile (telefone e tablet)
- [x] Toque abre `mailto:evolenteapp@gmail.com`
- [x] Helper com teste unitário
- [x] Sem mudança em front-end, backend ou política de privacidade

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/002-autenticacao.md`
- handoff Task 811 / Task 788 quando útil

## Contexto sob demanda

| Gatilho | Fonte | Decisão |
|---|---|---|
| UI login | `mobile/src/features/auth/screens/SignInScreen.tsx` | inserir CTA |
| Estilos | `mobile/src/features/auth/screens/styles.ts` | espaçamento |
| Abrir URL | `mobile/src/features/auth/utils/openResponsibleSignup.ts` | espelhar Linking |
| E-mail web | `front-end/src/constants/support.ts` | mesmo endereço |

## Orçamento de contexto

baixo — só auth mobile; sem OpenAPI, sem web UI

## Estrategia de reducao

- Espelhar Task 788
- Não reler requirements nem paywall IAP

## Dependencias

- Task 788 (CTA Criar conta no login) — done
- Task 811 (suporte na assinatura web) — done (mesmo e-mail)

## Resultado da execucao

- Botão ghost “Falar com o suporte” no `loginForm` (telefone e tablet), entre “Criar conta” e “Esqueci minha senha”.
- `openSupportEmail` abre `mailto:evolenteapp@gmail.com`.
- Desvio do print `login-mobile.png` registrado: CTA de suporte via e-mail.

## Contexto utilizado

- Contexto mínimo + SignInScreen/styles + openResponsibleSignup + e-mail da Task 811.

## Handoff

- `.agents/state/handoffs/TASK-812.md`

## Arquivos alterados

- `mobile/src/features/auth/constants.ts`
- `mobile/src/features/auth/utils/openSupportEmail.ts`
- `mobile/src/features/auth/utils/openSupportEmail.test.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/screens/styles.ts`
- `tasks/change-requests/812-botao-falar-com-suporte-login-mobile.md`
- `tasks/slices/002-autenticacao.md`
- `tasks/000-index.md`

## Validacoes executadas

- Jest `openSupportEmail.test.ts` — 2 passed
- Acessibilidade: `Button` com label/hint e `minHeight` 52

## Pendencias pos-task

- Conferir no iOS que o Mail abre; publicar build/OTA se o login em loja precisar do CTA

## Status final

done
