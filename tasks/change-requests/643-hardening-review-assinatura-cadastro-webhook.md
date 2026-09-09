# Task 643 - Hardening de revisão: assinatura, cadastro público e webhook

## Status

done

## Tipo

shared

## Stacks envolvidos

- front-end
- backend

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `GET /subscriptions/me`
- `POST /subscriptions/verify`
- `POST /guardians/register`
- `POST /subscriptions/webhooks/asaas`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura (`tasks/slices/039-gateway-asaas-assinatura.md`)
- Slice 049 - Cadastro público só do responsável (`tasks/slices/049-cadastro-responsavel-sem-filho.md`)

## Objetivo

Corrigir os três apontamentos válidos do code review em `ajustes.md`, preservando o fluxo de pagamento e eliminando as brechas de troca de senha e logging antes da autenticação do webhook.

## Escopo

- Permitir que o gate web ofereça verificação manual e/ou dispare `POST /subscriptions/verify` quando já existir assinatura `overdue` ou `suspended`, inclusive sem `checkout=success`, sem reintroduzir a verificação automática para conta sem assinatura.
- Exigir credencial atual ou token de recuperação válido para alterar a senha no reaproveitamento público de responsável órfão.
- Validar o segredo do webhook antes de registrar qualquer dado operacional e limitar os logs ao payload autenticado e seguro.
- Adicionar testes focados para os três comportamentos.

## Fora de escopo

- Alterar o ciclo de estados de assinatura ou o contrato público além do necessário para esses fluxos.
- Reabrir as tasks 640, 641 ou 639; elas são referências de comportamento já entregue.

## Contexto minimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`
- `tasks/000-index.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/slices/049-cadastro-responsavel-sem-filho.md`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`

## Contexto sob demanda

- testes correspondentes das três áreas, para preservar regressões;
- `front-end/docs/ai/ACCESSIBILITY.md`, porque o gate terá ação/estado de verificação;
- `backend/docs/ai/SECURITY.md`, porque há alteração de autenticação, senha e logs;
- paths relevantes de `contracts/openapi.yaml`, somente para validar que nenhuma mudança quebra o contrato.

## Orcamento de contexto

medio; carregar somente os arquivos de implementação, testes e trechos de contrato diretamente relacionados. Não carregar requirements, design-system ou stacks não envolvidas.

## Criterios de aceite

- [x] Conta sem assinatura continua sem chamar verify automaticamente.
- [x] Conta com assinatura `overdue`/`suspended` consegue verificar/regularizar pelo gate.
- [x] Reaproveitamento público não permite definir senha sem prova de posse da conta.
- [x] Webhook inválido não gera log operacional antes da autenticação.
- [x] Testes focados passam.

## Resultado da execucao

- Gate verifica estados `overdue` e `suspended`, sem verificar automaticamente conta sem assinatura.
- Recadastro órfão não troca senha com dados públicos.
- Webhook autentica antes dos logs operacionais.

## Contexto utilizado

- Contexto mínimo da raiz, slices 039/049, implementação e testes do gate/guardians/subscriptions.
- `front-end/docs/ai/ACCESSIBILITY.md` e `backend/docs/ai/SECURITY.md`.

## Handoff

- `.agents/state/handoffs/TASK-643.md`

## Arquivos alterados

- `ajustes.md`
- `front-end/src/pages/Auth/SubscriptionGate/index.tsx`
- `backend/src/modules/guardians/guardians.service.ts`
- `backend/src/modules/guardians/guardians.service.spec.ts`
- `backend/src/modules/subscriptions/subscriptions.service.ts`

## Validacoes executadas

- Backend: 40 testes focados passaram.
- Front-end: 5 testes focados passaram.
- Backend lint passou.
- Front-end lint não concluiu com saída nesta sessão.

## Pendencias pos-task

- Repetir o lint do front-end se necessário.

## Status final

done

## Dependencias

- Complementa as tasks concluídas 639, 640 e 641.
