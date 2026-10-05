# Task 772 - Copy do login mobile sem menção a pagamento

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

## Referencia de design system

### Stack de referencia visual

mobile

### Tipo de referencia visual

nao se aplica

### Fonte primaria visual

- nao se aplica (somente texto do modal de erro de login)

### Regra de aderencia visual

- preservar layout do modal; alterar apenas o corpo da mensagem

## Origem da solicitacao

Apple e Google Play barraram o app por interpretação de forma de pagamento no aplicativo. O modal de login exibia orientação para regularizar assinatura no site.

## Objetivo

Substituir o corpo do modal de erro de login (acesso negado por falta de liberação) por copy neutra, sem mencionar pagamento, assinatura, checkout ou site.

## Escopo

- Mensagem lançada em `assertMobileSubscriptionAccess` no login mobile
- Texto exibido no modal `Não foi possível entrar` do `SignInScreen`

## Fora de escopo

- Copy de perfil / `SubscriptionManagementCard` (também menciona site/pagamento; tratar em task separada se a loja exigir)
- Backend, web, checkout Asaas
- Fluxo de liberação de acesso (apenas wording)

## Entradas

- pedido explícito do usuário nesta conversa
- `tasks/change-requests/603-gate-assinatura-antes-login-mobile.md`
- `mobile/src/features/auth/services/authService.ts`
- `mobile/src/features/auth/screens/SignInScreen.tsx`

## Slice vertical

### Identificador do slice

Slice 039 - Gateway Asaas e ciclo de assinatura

### Arquivo do slice

- `tasks/slices/039-gateway-asaas-assinatura.md`

### Objetivo de negocio

Manter o gate de acesso no mobile sem copy que as lojas interpretem como pagamento no app.

### Entrega verificavel do slice

Modal de login sem acesso usa mensagem neutra, sem palavras de pagamento/assinatura/site.

### Fora do slice

- remoção completa de menções a pagamento em telas autenticadas

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- esta task
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Contexto sob demanda

| Gatilho | Fonte | Quando carregar | Obrigatório? |
|---|---|---|---|
| Mensagem atual e ponto de throw | `mobile/src/features/auth/services/authService.ts` | ao alterar copy | sim |
| Exibição do modal | `mobile/src/features/auth/screens/SignInScreen.tsx` | confirmar título/corpo | nao |
| Handoff do gate | `.agents/state/handoffs/TASK-603.md` | retomada do gate | nao |

## Orçamento de contexto

- Fontes obrigatórias estimadas: 6
- Fontes sob demanda estimadas: 2
- Risco de contexto excessivo: baixo
- Estratégia para reduzir contexto: só o throw do login e o modal; sem carregar SubscriptionGate web nem Asaas

## Dependencias

- Task 603 (gate de assinatura antes do login mobile)

## Criterios de conclusao

- [x] Corpo do erro de acesso no login não menciona pagamento, assinatura, checkout nem site
- [x] Título do modal permanece `Não foi possível entrar`
- [x] Comportamento do gate (bloqueio sem `accessGranted`) permanece igual

## Instrucoes de implementacao

- Nova mensagem: `Esta conta ainda não tem acesso ao aplicativo. Se precisar de ajuda, fale com o suporte Evolente.`
- Alterar apenas a string em `assertMobileSubscriptionAccess`
- Não alterar a regra de `accessGranted`

## Validacao esperada

- lint/teste do `authService`
- confirmação: modal exibe o novo corpo

## Entregaveis esperados

- string atualizada em `authService.ts`
- task, índice, slice e handoff atualizados

## Resultado da execucao

- Corpo do modal de login sem acesso passou a: `Esta conta ainda não tem acesso ao aplicativo. Se precisar de ajuda, fale com o suporte Evolente.`
- Gate (`accessGranted`) e título `Não foi possível entrar` preservados.

## Contexto utilizado

- Task 772, Slice 039, `authService.ts`, `SignInScreen.tsx` (confirmação do modal).

## Handoff

- `.agents/state/handoffs/TASK-772.md`

## Arquivos alterados

- `mobile/src/features/auth/services/authService.ts`
- `tasks/change-requests/772-copy-login-mobile-sem-mencao-pagamento.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `.agents/state/handoffs/TASK-772.md`

## Validacoes executadas

- `npx eslint src/features/auth/services/authService.ts` + `npx jest src/features/auth/services/authService.test.ts --runInBand` — passaram.

## Pendencias pos-task

- Se a loja ainda flagrar copy em perfil/`SubscriptionManagementCard` (menções a pagamento/site), abrir task dedicada.

## Status final

done
