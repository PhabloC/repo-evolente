# Task 696 - Manter pagamento somente na página Asaas

**Status**: done
**Tipo**: front
**Stacks envolvidos**: front-end (React/Vite)
**Contrato**: nenhum — a API continua compatível
**Modo de execução**: single-stack
**Slice vertical**: `tasks/slices/060-cartao-debito-assinatura.md`

## Objetivo

Fazer com que o usuário realize o pagamento exclusivamente na página/fatura hospedada do Asaas.

## Escopo

- Remover da tela de aguardando pagamento o bloco local de PIX copia e cola.
- Manter a abertura e reabertura da fatura Asaas.
- Preservar polling, botão de verificação e retorno após `autoRedirect`.

## Critérios de aceite

- O PIX copia e cola não aparece no Evolente.
- A fatura Asaas continua sendo aberta após criar o checkout.
- A confirmação via webhook e o polling permanecem inalterados.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/060-cartao-debito-assinatura.md`
- `tasks/change-requests/695-implementar-cartao-debito-assinatura.md`

## Contexto sob demanda

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/docs/ai/ACCESSIBILITY.md`

## Orçamento de contexto

Até 6 fontes; limitar a mudança ao componente do gate e seus testes.

## Dependências

- Task 695.

## Resultado da execucao

Removida a exibição do PIX copia e cola no Evolente. A fatura Asaas continua sendo aberta automaticamente e pode ser reaberta pelo botão existente; polling, verificação manual e webhook permaneceram inalterados.

## Contexto utilizado

- Gate web de assinatura.
- Checklist de acessibilidade do front-end.
- Tasks 695 e Slice 060.

## Handoff

Pagamento PIX agora é realizado somente na página/fatura do Asaas. O front-end não renderiza mais o payload local.

## Arquivos alterados

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`

## Validacoes executadas

- `npm run lint` — aprovado.
- `npm test -- src/pages/Auth/SubscriptionGate/index.test.tsx` — 5 testes aprovados.

## Pendencias pos-task

- Nenhuma.

## Status final

done
