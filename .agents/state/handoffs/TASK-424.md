# Handoff - Task 424

## Task

- identificador: 424
- título: Página de planos do master com valores Asaas
- tipo: front
- modo de execução: single-stack
- status final: done

## Slice vertical

- identificador: Slice 039 - Gateway Asaas e ciclo de assinatura
- objetivo de negócio: UI master alinhada aos planos oficiais enquanto sandbox Asaas é preparado
- entrega verificável: `/admin/planos` sem TBD, com catálogo R$ 79 / R$ 49
- status do slice: todo (419+424 done; 420–423 pendentes)

## Decisões preservadas

- decisão: Catálogo visual dos planos oficiais na página master (não só tabela)
- motivo: master precisa ver valores/meios antes do gateway real
- impacto: `PlansSection` com dois cards + tabela

- decisão: Fallback de valor = plano oficial por audience quando `amountCents` é null (fake)
- motivo: provider fake ainda não grava valor
- impacto: coluna Valor sempre preenchida

- decisão: Ações Ativar/Recusar mantidas; novos status só para exibição
- motivo: backend enum ainda legado até 420/421
- impacto: sem PATCH de overdue/suspended/canceled nesta task

## Contexto utilizado

### Contexto mínimo lido

- task 424, slice 039, handoff 419
- Admin Plans / sections / workspace / types / adminOptions

### Contexto sob demanda carregado

| Fonte | Gatilho | Uso |
|---|---|---|
| ACCESSIBILITY.md | UI | checklist |
| requirements §5 | planos | valores/ciclo |

### Contexto evitado

| Fonte | Motivo |
|---|---|
| backend Asaas / mobile | fora do escopo |

## Resultado por stack

- front-end: done
- backend: não alterado
- mobile: não alterado

## Arquivos alterados

- `front-end/src/types/subscription.ts`
- `front-end/src/constants/adminOptions.ts`
- `front-end/src/pages/Main/Admin/**` (sections, workspace, utils, styles, index)
- `front-end/src/pages/Main/AdminPlans/index.tsx`
- task/slice/index/handoff 424

## Validações executadas

- Admin index.test — ok
- lints Admin — ok

## Pendências ou bloqueios

- 420 provider Asaas
- sandbox do usuário em andamento

## Próxima ação sugerida

- Continuar sandbox Asaas; depois Task 420

## Próximo contexto recomendado

- handoff 419 + 424
- task 420 + `backend/src/modules/subscriptions/`
- docs Asaas sandbox

## Contexto que não deve ser carregado na próxima etapa

- jogos / design prints de jogos
- mobile UI (exceto se for 423)
