# Task 641 - Gate de assinatura nao verifica sem checkout

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

- `GET /subscriptions/me`
- `POST /subscriptions/verify`
- `POST /subscriptions/checkout`

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura (`tasks/slices/039-gateway-asaas-assinatura.md`)
- Slice 049 - Cadastro publico so do responsavel (`tasks/slices/049-cadastro-responsavel-sem-filho.md`)

## Objetivo

Corrigir o gate web de assinatura para nao chamar `POST /subscriptions/verify` antes de existir checkout/assinatura pendente, evitando o erro "Nenhuma assinatura encontrada para este usuario" na tela inicial de pagamento.

## Comportamento esperado

- Ao entrar autenticado no gate sem assinatura, a tela consulta `GET /subscriptions/me` e exibe a escolha de forma de pagamento.
- `POST /subscriptions/verify` fica reservado para retorno de checkout, polling ou botao "Ja paguei".
- A mensagem de erro de assinatura ausente nao aparece antes do usuario tentar iniciar/verificar pagamento.

## Contexto minimo

- esta task
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`

## Contexto sob demanda

- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx` para teste focado
- `front-end/docs/ai/ACCESSIBILITY.md` para manter estados de erro/status acessiveis

## Orcamento de contexto

- baixo - ajuste localizado no gate de assinatura web.

## Criterios de aceite

- [x] Entrada autenticada sem assinatura usa `getSubscriptionStatus`, nao `verifySubscriptionPayment`.
- [x] Tela exibe CTA de pagamento sem erro vermelho nesse estado.
- [x] Teste focado cobre o fluxo.

## Resultado da execucao

- O carregamento inicial autenticado do gate de assinatura passou a usar `GET /subscriptions/me`.
- `POST /subscriptions/verify` ficou restrito ao retorno `?checkout=success`, polling da tela de aguardando pagamento e botao "Ja paguei".
- O estado sem assinatura agora cai direto em `pending` com CTA "Pagar com Asaas", sem exibir erro vermelho antes de iniciar checkout.
- O teste da tela cobre usuario responsavel autenticado sem assinatura e garante que `verifySubscriptionPayment` nao e chamado nesse estado.
- Ajustado callback de navegacao em `MainLayout` para satisfazer lint sem alterar comportamento.

## Contexto utilizado

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `front-end/docs/ai/AGENTS.md`
- `front-end/docs/ai/ARCHITECTURE.md`
- `front-end/docs/ai/CODE_STYLE.md`
- `front-end/docs/ai/QA.md`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx`

## Handoff

- `.agents/state/handoffs/TASK-641.md`

## Arquivos alterados

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx`
- `front-end/src/layout/MainLayout/index.tsx`
- `tasks/change-requests/641-gate-assinatura-nao-verificar-sem-checkout.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `.agents/state/handoffs/TASK-641.md`

## Validacoes executadas

- `npm test -- src/pages/Auth/SubscriptionGate/index.test.tsx` - 5 testes passaram.
- `npm run lint` - passou.
- `npm run build` - falhou por erros TypeScript preexistentes em `src/pages/Main/Patients/**` e `src/pages/Main/Plans/**`, fora do gate de assinatura.

## Pendencias pos-task

- Corrigir tipos antigos de pacientes/planos para o build completo voltar a passar.

## Status final

done
