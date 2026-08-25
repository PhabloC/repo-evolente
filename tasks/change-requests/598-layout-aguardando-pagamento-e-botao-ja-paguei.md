# Task 598 - Layout aguardando pagamento e botão Já paguei

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

Não se aplica.

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Melhorar o layout da etapa `awaiting-payment` do gate `/assinatura` e garantir que o botão “Já paguei — verificar agora” dê feedback claro (loading, ainda pendente ou liberação).

## Origem da solicitacao

Pedido humano com print da tela de aguardo + verificação do botão.

## Dependencias

- Task 597 — done

## Contexto mínimo

- esta task
- `front-end/src/pages/Auth/SubscriptionGate/`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Service | `subscriptionService.getSubscriptionStatus` | verificação manual |

## Orçamento de contexto

- baixo

## Criterios de aceite

- [x] Layout da etapa aguardando alinhado ao painel das etapas anteriores
- [x] Banner “Conta criada” não permanece na etapa de aguardo autenticada
- [x] Botão “Já paguei” com estado de loading
- [x] Se ainda pendente, mensagem explícita ao usuário
- [x] Se `accessGranted`, libera sessão como já fazia

## Fora de escopo

- Backend / webhook Asaas
- Mobile

## Resultado da execucao

- Etapa `awaiting-payment` em painel com indicador de espera e CTAs agrupados.
- Banner pós-cadastro só na view `login`.
- `onVerifyPayment`: loading, erro de API e mensagem quando status ainda pendente; libera se `accessGranted`.

## Contexto utilizado

- SubscriptionGate + subscriptionService

## Handoff

- `.agents/state/handoffs/TASK-598.md`

## Arquivos alterados

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/styles.module.css`
- `tasks/change-requests/598-layout-aguardando-pagamento-e-botao-ja-paguei.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-598.md`

## Validacoes executadas

- ReadLints SubscriptionGate — ok

## Pendencias pos-task

- Webhook Asaas precisa alcançar o backend público para `accessGranted` virar true após pagamento real

## Status final

done
