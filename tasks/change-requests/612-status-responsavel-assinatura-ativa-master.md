# Task 612 - Status do responsável pela assinatura no master

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- front-end

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- Estender `GET /admin/guardians-tree` com `subscriptionActive`, derivado da assinatura mais recente do responsável.

## Modo de execução

cross-stack

## Slice vertical

- Slice 009 — `tasks/slices/009-administracao-master.md`

## Objetivo

Mostrar na coluna Status da aba Pacientes se a assinatura do responsável está ativa, sem confundir esse estado com o status técnico da conta.

## Dependências

- Task 611 — done (árvore responsável → filhos no master)

## Contexto mínimo

- esta task
- `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-611.md`
- `backend/src/modules/admin/admin.service.ts`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `contracts/openapi.yaml` no schema `AdminGuardianTreeNode`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Estado de assinatura | `backend/src/modules/subscriptions/{subscriptions.service.ts,entities/subscription.entity.ts}` | derivar com segurança o status da assinatura mais recente. |
| Cliente e tipo web | `front-end/src/{types/admin.ts,services/admin/adminService.ts}` | consumir o novo campo do contrato. |
| UI e acessibilidade | `front-end/docs/ai/{ACCESSIBILITY,CODE_STYLE,QA}.md` | exibir texto claro, não depender apenas da cor e validar a página. |

## Orçamento de contexto

- baixo
- estratégia: enriquecer o endpoint já consumido, sem criar rota, cadastro, edição ou mudança no ciclo de cobrança.

## Critérios de aceite

- [x] A resposta administrativa contém `subscriptionActive` por responsável.
- [x] Apenas assinatura com status `active` torna o responsável ativo na coluna Status.
- [x] Demais estados de assinatura mostram Inativo; ausência de assinatura também.
- [x] Filhos continuam exibindo somente seu status de vínculo profissional.
- [x] Contrato, testes e página são atualizados.

## Resultado da execução

- `GET /admin/guardians-tree` passa a devolver `subscriptionActive` por responsável. O backend escolhe a assinatura mais recente por `createdAt` e só considera ativo o status `active`.
- A coluna Status e o filtro da aba Pacientes usam `subscriptionActive` para linhas de responsáveis. As linhas-filho preservam a leitura do vínculo profissional, sem misturar os dois conceitos.

## Contexto utilizado

- Task 612, Slice 009 e handoff da Task 611.
- AdminService e entidades/serviço de assinaturas no backend; contrato OpenAPI.
- Tipos, serviço administrativo e página/testes AdminUsers no front-end.

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/admin/{admin.service.ts,admin.service.spec.ts}`
- `front-end/src/types/admin.ts`
- `front-end/src/pages/Main/AdminUsers/{index.tsx,index.test.tsx}`
- `tasks/change-requests/612-status-responsavel-assinatura-ativa-master.md`
- `tasks/000-index.md`
- `tasks/slices/009-administracao-master.md`
- `.agents/state/handoffs/TASK-612.md`

## Validações executadas

- Backend: `npm run test -- --runInBand src/modules/admin/admin.service.spec.ts` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final do Jest).
- Front-end: `npm run test -- --run src/pages/Main/AdminUsers` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final do Vitest).
- Front-end: `npm run build` — concluído sem mensagem de erro (o ambiente não exibiu o resumo final).
- `git diff --check` — aprovado.

## Pendências pós-task

- Validar visualmente uma assinatura `active`, uma `pending` e uma conta sem assinatura no ambiente master.

## Handoff

- `.agents/state/handoffs/TASK-612.md`

## Status final

done
