# Task 627 - Corrigir vínculo cancelado e deeplink AdminUsers web

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

- `PATCH /patients/{patientId}/status`
- `GET /users/{userId}` (deeplink `profileId` em AdminUsers)

## Modo de execucao

single-stack

## Slice vertical

- Slice 054 — Cancelamento da conta do responsável e restrição de acesso profissional (`tasks/slices/054-cancelamento-conta-responsavel-acesso-profissional.md`)

## Objetivo

Corrigir três gaps de code review na área profissional web:

1. **Lista de pacientes:** confirmar remoção de vínculo cancelado envia `inactive` (preserva o vínculo) mas a UI promete remoção e o item reaparece como reativável.
2. **Perfil do paciente:** rota direta ou estado `canceled` expõe ação de reativar, contornando restrições da lista.
3. **AdminUsers:** deeplink `profileId` sem `catch` gera rejeição não tratada e fecha o fluxo sem feedback.

## Comportamento esperado

- Paciente cancelado: ação destrutiva continua usando `inactive` permitido pela API, com copy honesta; após a operação, o item não oferece **Reativar** quando a assinatura do responsável estiver revogada.
- Perfil: vínculo `canceled` (ou inativo sem assinatura) não exibe CTAs clínicos/trilha/reativar; oferece somente retorno e remoção/inativação do vínculo quando aplicável.
- AdminUsers: falha ao carregar `profileId` exibe erro ao usuário e remove apenas o parâmetro da URL.

## Dependências

- Task 606 — paciente cancelado na lista (done)

## Contexto mínimo

- esta task, Slice 054
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Semântica de status | `contracts/openapi.yaml` — `PatientLinkStatus` | inativação vs reativação |
| Testes | `index.test.tsx` das três páginas | regressão |

## Orçamento de contexto

- baixo — três pontos localizados em páginas web existentes.

## Critérios de aceite

- [x] Lista: paciente cancelado inativado não exibe **Reativar** quando assinatura do responsável estiver revogada; mensagem não promete remoção física do vínculo.
- [x] Perfil: vínculo `canceled` tratado explicitamente sem reativar nem CTAs clínicos.
- [x] AdminUsers: erro de `getUserById` exibido e `profileId` removido da URL.
- [x] Testes focados passam.

## Resultado da execucao

- Criado util `patientLinkActions` centralizando regras de reativação e perfil restrito.
- Lista e perfil usam copy de **inativar vínculo** para pacientes cancelados; **Reativar** oculto quando `subscriptionAccessGranted === false`.
- Perfil cancelado renderiza card restrito sem evolução, consultas ou trilha.
- AdminUsers trata falha do deeplink `profileId` com alerta acessível.

## Contexto utilizado

- Task 627, Slice 054, páginas Patients/PatientProfile/AdminUsers, contrato de status de vínculo, testes focados.

## Handoff

`.agents/state/handoffs/TASK-627.md`

## Arquivos alterados

- `front-end/src/pages/Main/Patients/utils/patientLinkActions.ts`
- `front-end/src/pages/Main/Patients/utils/patientLinkActions.test.ts`
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/index.test.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.test.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.test.tsx`
- `tasks/change-requests/627-corrigir-vinculo-cancelado-e-deeplink-admin-users-web.md`
- `tasks/000-index.md`

## Validacoes executadas

- eslint nos arquivos alterados — ok
- vitest focado Patients (18) + AdminUsers deeplink — ok na execução principal

## Pendencias pos-task

- Endurecer no backend bloqueio de reativação de vínculo inativo originado de conta cancelada.

## Status final

done
