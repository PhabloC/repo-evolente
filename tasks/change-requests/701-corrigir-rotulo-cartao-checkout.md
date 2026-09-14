# Task 701 - Corrigir rótulo do cartão no checkout

## Status

done

## Tipo

front

## Stacks envolvidos

front-end (React/Vite)

## Contrato

Nenhum — somente o texto da opção existente; o método enviado continua `credit_card`.

## Modo de execução

single-stack

## Slice vertical

`tasks/slices/060-cartao-debito-assinatura.md`

## Objetivo

Alinhar o rótulo exibido no gate de assinatura ao método efetivamente enviado ao checkout, removendo a promessa de cartão de débito não representada pelo contrato.

## Escopo

- Alterar “Cartão de crédito ou débito” para “Cartão de crédito”.
- Atualizar teste do gate, se houver cobertura do texto.
- Marcar o comentário correspondente em `ajustes.md` como corrigido.

## Critérios de aceite

- A opção que envia `credit_card` informa somente cartão de crédito.
- PIX permanece disponível e o pagamento continua hospedado no Asaas.

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/060-cartao-debito-assinatura.md`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`

## Contexto sob demanda

- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx`: verificar cobertura do rótulo.
- `front-end/docs/ai/ACCESSIBILITY.md`: validar texto acessível da opção.

## Orçamento de contexto

Até 6 fontes; limitar a alteração ao gate, teste, backlog e registro de review.

## Dependências

- Tasks 695 e 696.

## Resultado da execucao

O rótulo da opção foi alterado para “Cartão de crédito”, mantendo o envio de `credit_card`. O comentário correspondente em `ajustes.md` foi marcado como `[ok]`.

## Contexto utilizado

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `front-end/src/pages/Auth/SubscriptionGate/index.test.tsx`
- `front-end/docs/ai/ACCESSIBILITY.md`
- `tasks/slices/060-cartao-debito-assinatura.md`

## Handoff

O rótulo está alinhado ao método suportado. O próximo contexto recomendado é repetir as validações automatizadas do front-end.

## Arquivos alterados

- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `ajustes.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-701.md`

## Validacoes executadas

- Vitest e ESLint foram iniciados, mas permaneceram sem saída por mais de um minuto e foram interrompidos; não foi possível obter resultado automatizado nesta execução.

## Pendencias pos-task

- Reexecutar Vitest/ESLint em ambiente sem o travamento observado.

## Status final

done
