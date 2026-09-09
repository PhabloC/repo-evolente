# Task 642 - Diagnosticar erro Asaas ao criar assinatura PIX

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `POST /subscriptions/checkout`

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura (`tasks/slices/039-gateway-asaas-assinatura.md`)

## Objetivo

Melhorar o diagnostico e tratamento do erro retornado pelo Asaas ao criar assinatura PIX, preservando logs seguros e uma resposta mais util para o cliente.

## Comportamento esperado

- Falhas do Asaas em `POST /subscriptions` devem registrar status, endpoint, codigo/mensagem retornada e contexto seguro do checkout.
- A resposta HTTP da aplicacao deve conter codigo interno especifico para assinatura PIX rejeitada quando aplicavel.
- Dados sensiveis como token Asaas, CPF completo e payload bruto nao devem ser expostos na resposta.

## Contexto minimo

- esta task
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`

## Contexto sob demanda

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts` para teste focado
- documentacao oficial Asaas sobre assinaturas quando houver duvida de payload

## Orcamento de contexto

- baixo - ajuste localizado no adapter do Asaas e testes unitarios.

## Criterios de aceite

- [x] Log de erro do Asaas informa detalhes seguros suficientes para diagnosticar a rejeicao.
- [x] Erro de assinatura PIX rejeitada retorna codigo interno especifico.
- [x] Teste focado cobre a rejeicao do `POST /subscriptions`.

## Resultado da execucao

- O adapter agora registra endpoint, método, status e detalhes seguros (`code`/mensagem) retornados pelo Asaas, sem payload bruto ou token.
- Rejeições do `POST /subscriptions` no fluxo PIX retornam `ASAAS_PIX_SUBSCRIPTION_REJECTED`.
- O teste focado valida o mapeamento e confirma que o token não é exposto.

## Contexto utilizado

- Contexto mínimo da raiz, Slice 039 e esta task.
- `backend/docs/ai/AGENTS.md`, adapter e teste unitário do Asaas.

## Handoff

- Task concluída no adapter `AsaasPaymentProvider`; o próximo agente pode validar a suíte completa do backend se necessário.

## Arquivos alterados

- `backend/src/modules/subscriptions/providers/asaas-payment.provider.ts`
- `backend/src/modules/subscriptions/providers/asaas-payment.provider.spec.ts`

## Validacoes executadas

- `npm test -- --runInBand src/modules/subscriptions/providers/asaas-payment.provider.spec.ts` — passou (15 testes).

## Pendencias pos-task

- Nenhuma.

## Status final

done
