# Task 424 - Página de planos do master com valores Asaas

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

- `contracts/openapi.yaml` schemas Subscription / SubscriptionPlan (Task 419) — sem mudança de contrato nesta task

## Modo de execucao

single-stack

## Slice vertical

- Slice 039 - Gateway Asaas e ciclo de assinatura
- `tasks/slices/039-gateway-asaas-assinatura.md`

## Objetivo

Atualizar a página master de Planos para refletir os planos oficiais (R$ 79 / R$ 49 mensais), meios Asaas e o ciclo de status PENDING→ACTIVE→OVERDUE→SUSPENDED→CANCELED, removendo copy TBD.

## Dependencias

- Task 419 — done

## Contexto mínimo

- esta task
- slice 039
- handoff TASK-419
- `front-end/src/pages/Main/AdminPlans/`
- `front-end/src/pages/Main/Admin/sections.tsx` (PlansSection)
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/types/subscription.ts`
- `front-end/src/constants/adminOptions.ts`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| A11y | `front-end/docs/ai/ACCESSIBILITY.md` | checklist UI |
| DS | `design-system/front/Design_System_Evolente_Desktop.md` | tokens/cards |
| Planos oficiais | `requirements/002-regras-de-negocio.md` §5 | valores/ciclo |
| Docs front | `front-end/docs/ai/` | padrões |

## Orçamento de contexto

- baixo/médio
- estrategia: só Admin Plans + types/constants; sem implementar Asaas nem mobile

## Criterios de aceite

- [x] Remover copy “valores TBD” da seção Planos
- [x] Exibir catálogo dos planos oficiais: profissional R$ 79/mês; responsável R$ 49/mês; mensal; meios cartão/PIX/boleto; gateway Asaas
- [x] Tabela mostra valor formatado (BRL) quando `amountCents` existir
- [x] Labels de status cobrem pending, active, overdue, suspended, canceled, refused
- [x] Estilos visuais distinguem estados (não só por cor: texto do label)
- [x] Ações manuais Ativar/Recusar permanecem (backend ainda só aceita esses até 420/421)
- [x] Subtítulo/overview da área Planos alinhados ao novo ciclo
- [x] Testes/lint relevantes passam

## Fora de escopo

- Provider Asaas / webhooks (420/421)
- Checkout do usuário (422)
- Alterar enum/DTO no backend
- Mobile admin

## Referencia visual

### Stack de referencia visual

front-end

### Tipo de referencia visual

artefato de design system

### Fonte primaria visual

- `design-system/front/Design_System_Evolente_Desktop.md`

### Lacunas

- Sem print dedicado de Planos master — reutilizar cards/tabelas do admin atual

## Resultado da execucao

- Catálogo de planos oficiais na página `/admin/planos`.
- Tabela com usuário resolvido, valor BRL, status do ciclo completo e ações Ativar/Recusar mantidas.
- Types/labels front alinhados ao contrato da Task 419.

## Contexto utilizado

- contexto mínimo: task 424, slice 039, Admin Plans/sections/workspace
- contexto sob demanda: ACCESSIBILITY (checklist), requirements §5 (valores)
- contexto evitado: backend Asaas, mobile, checkout

## Handoff

- `.agents/state/handoffs/TASK-424.md`

## Arquivos alterados

- `front-end/src/types/subscription.ts`
- `front-end/src/constants/adminOptions.ts`
- `front-end/src/pages/Main/Admin/sections.tsx`
- `front-end/src/pages/Main/Admin/useAdminWorkspace.tsx`
- `front-end/src/pages/Main/Admin/utils.ts`
- `front-end/src/pages/Main/Admin/styles.module.css`
- `front-end/src/pages/Main/Admin/index.tsx`
- `front-end/src/pages/Main/AdminPlans/index.tsx`
- `tasks/change-requests/424-pagina-planos-master-valores-asaas.md`
- `tasks/slices/039-gateway-asaas-assinatura.md`
- `tasks/000-index.md`
- `.agents/state/handoffs/TASK-424.md`

## Validacoes executadas

- `vitest run src/pages/Main/Admin/index.test.tsx` — ok
- ReadLints nos arquivos Admin alterados — sem erros
- `tsc --noEmit` — erros pré-existentes em Library/Patients (não relacionados)

## Acessibilidade aplicada

- Catálogo com headings `h3` e lista semântica
- Meta dos planos em `dl/dt/dd`
- Status com texto legível (não só cor)
- Botões de ação com labels textuais existentes

## Pendencias pos-task

- Task 420 (provider Asaas) para popular `amountCents`/provider reais
- Ações admin para overdue/suspended/canceled quando backend expandir enum

## Status final

done
