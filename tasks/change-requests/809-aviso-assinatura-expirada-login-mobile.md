# Task 809 - Aviso de assinatura expirada no login mobile

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

- `GET /subscriptions/me` (já existente; o app passa a ler `subscription.status`, `provider` e `firstPaidAt`)

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 — `tasks/slices/039-gateway-asaas-assinatura.md`

## Escopo

- No login mobile, conta que já pagou no Asaas (PIX ou cartão) e perdeu o acesso vê que a assinatura expirou e que a renovação é na versão web.
- Conta que nunca assinou mantém a mensagem neutra.
- Compra Apple sem acesso continua no paywall do iOS.

## Criterios de aceite

- [x] Assinatura Asaas suspensa, vencida, ou cancelada depois de paga (`firstPaidAt`), sem acesso, bloqueia o login com o aviso de expiração. Checkout cancelado sem pagamento mantém a mensagem neutra
- [x] Modal do login usa o título "Assinatura expirada" nesse caso
- [x] Quem nunca assinou não recebe esse texto
- [x] Assinatura Apple não é mandada para a web

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- este arquivo e o slice 039
- `tasks/change-requests/772-copy-login-mobile-sem-mencao-pagamento.md` (a mensagem genérica permanece para quem nunca pagou)

## Contexto sob demanda

- `mobile/src/features/auth/services/authService.ts` — gate do login
- `mobile/src/features/auth/screens/SignInScreen.tsx` — modal
- `GET /subscriptions/me` já devolve `subscription`

## Orçamento de contexto

- baixo; só o gate de login mobile
- referência visual: modal de erro já existente; só título e corpo

## Resultado da execucao

- Login de responsável com assinatura Asaas já paga e sem acesso mostra "Assinatura expirada" e pede renovação na versão web.
- Quem nunca assinou continua com a mensagem neutra. Compra Apple no iOS segue para o paywall.
- Slice 039 permanece done; esta task é um complemento do gate.

## Contexto utilizado

- Mínimo da task, slice 039 e a task 772.
- Sob demanda: `authService`, `SignInScreen` e o tipo de `GET /subscriptions/me`.
- Design system não carregado: o modal já existia e só o texto mudou.

## Handoff

- `.agents/state/handoffs/TASK-809.md`

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/services/authService.test.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`
- `mobile/src/features/auth/utils/resolveBlockedLoginMessage.ts`
- `mobile/src/features/auth/utils/resolveBlockedLoginMessage.test.ts`

## Validacoes executadas

- Jest `authService.test.ts` e `resolveBlockedLoginMessage.test.ts`: 10 testes passaram

## Pendencias pos-task

- Nenhuma. O aviso aparece ao tentar entrar; reabrir o app sem novo login só volta para a tela de login.

## Status final

done
