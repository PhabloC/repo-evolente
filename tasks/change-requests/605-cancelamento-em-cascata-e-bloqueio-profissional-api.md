# Task 605 - Cancelamento em cascata da conta e bloqueio profissional na API

## Status

done

## Tipo

shared

## Stacks envolvidos

- backend
- contracts

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `POST /subscriptions/cancel`
- `POST /subscriptions/refund`
- `POST /subscriptions/webhooks/asaas`
- `GET /patients`
- `GET /patients/{patientId}` e rotas filhas
- `PATCH /patients/{patientId}/status` (remoção/inativação do vínculo)
- `GET|POST /patients/{patientId}/trails` e rotas de trilha relacionadas

## Modo de execução

cross-stack

## Slice vertical

- Slice 054 — `tasks/slices/054-cancelamento-conta-responsavel-acesso-profissional.md`

## Objetivo

Fazer do cancelamento/reembolso da assinatura do responsável uma revogação em cascata de sua conta familiar e impedir, no servidor, qualquer acesso clínico ou mutação de trilha por profissional em pacientes cancelados, preservando apenas a remoção do vínculo profissional.

## Dependências

- Task 421 — done
- Task 423 — done
- Task 581 — done
- Task 595 — done
- Task 602 — done (regra de permissão substituída por esta task)

## Contexto mínimo

- esta task
- Slice 054, Slices 039 e 053
- `.agents/state/handoffs/TASK-421.md`
- `.agents/state/handoffs/TASK-595.md`
- `.agents/state/handoffs/TASK-602.md`
- paths e schemas de subscriptions, patients e trails em `contracts/openapi.yaml`

## Contexto sob demanda

| Gatilho | Fonte | Uso |
|---|---|---|
| Cascata de cancelamento | módulos `subscriptions`, `guardians`, `patients` e migrations do backend | localizar a conta familiar e persistir a inativação dos filhos de forma idempotente |
| Autorização clínica | serviços/repositórios/controladores de `patients`, `trails`, `progress` e consultas | negar leitura e mutações de profissional antes de expor dados sensíveis |
| Remover vínculo | implementação de `PATCH /patients/{patientId}/status` | permitir somente inativar/remover o vínculo atual; não permitir reativação de paciente cancelado |
| Segurança | `backend/docs/ai/SECURITY.md` | validar isolamento e respostas 403 sem vazamento |
| Cobertura | testes focados desses módulos | validar cascata, idempotência e matriz de permissões |

## Orçamento de contexto

- médio
- estratégia: limitar às rotas de assinatura, patients e trails; não carregar checkout, catálogo, relatórios ou app mobile.

## Critérios de aceite

- [x] Cancelamento, reembolso e evento Asaas que levem a `canceled` inativam todos os pacientes/filhos do responsável no mesmo fluxo idempotente, sem apagar seus dados.
- [x] `GET /patients` retorna pacientes cancelados apenas com identificação e estado suficientes para o profissional remover o vínculo; nenhum dado clínico é incluído.
- [x] Um profissional recebe `403` ao buscar o detalhe ou acessar/mutar anamnese, avatar, evolução, consultas e trilhas de paciente cancelado.
- [x] A criação, sugestão, edição e exclusão de trilhas é bloqueada também no servidor para paciente cancelado.
- [x] A única operação de profissional permitida para paciente cancelado é remover/inativar seu vínculo atual; reativar o vínculo não volta a liberar o paciente cancelado.
- [x] O contrato descreve o estado de paciente cancelado e a limitação da listagem; testes cobrem cancelamento manual, reembolso, webhook repetido e tentativas de acesso profissional.

## Fora de escopo

- Apagar dados da família ou desfazer automaticamente vínculos.
- Reativar paciente/vínculos ao criar uma assinatura futura.
- Alterar telas web ou mobile.

## Resultado da execucao

- O cancelamento manual, o reembolso e eventos Asaas confirmados como `canceled` agora marcam como `canceled` todos os vínculos profissionais ativos das crianças do responsável, de forma idempotente e sem excluir dados.
- Rotas clínicas do profissional já centralizadas em `assertProfessionalOwnsPatient` passaram a exigir vínculo `active`, bloqueando detalhe, avatar, consultas, evolução e trilhas para vínculo cancelado.
- O único `PATCH /patients/{patientId}/status` permitido após o cancelamento é a inativação/remoção do vínculo; a reativação é rejeitada.
- O contrato passou a expor `canceled` no status de vínculo e descreve a limitação de acesso.

## Contexto utilizado

- Task 605, Slice 054, handoffs 421/595/602, contrato de assinatura/pacientes/trilhas, módulos backend de subscriptions, patients, guardians e trails, além das diretrizes locais de arquitetura e segurança.

## Handoff

- `.agents/state/handoffs/TASK-605.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/subscriptions/subscriptions.service.ts`
- `backend/src/modules/subscriptions/subscriptions.module.ts`
- `backend/src/modules/subscriptions/subscriptions.service.spec.ts`
- `backend/src/modules/patients/entities/professional-patient-link.entity.ts`
- `backend/src/modules/patients/patients.service.ts`
- `backend/src/modules/patients/patients.module.ts`
- `backend/src/modules/patients/patients.service.spec.ts`

## Validacoes executadas

- `npx eslint` nos arquivos backend alterados — passou.
- `npm test -- --runInBand src/modules/patients/patients.service.spec.ts src/modules/subscriptions/subscriptions.service.spec.ts` — 33 testes passaram.
- `npm run typecheck` — bloqueado por erros preexistentes em testes de `admin`, `contents`, `reports`, `trails` e e2e; nenhum diagnóstico nos arquivos de produção alterados desta task.
- `git diff --check` — sem erros de whitespace.

## Pendencias pos-task

- Nenhuma.

## Status final

done
