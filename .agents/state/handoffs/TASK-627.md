# Handoff TASK-627

## Identificador

TASK-627

## Título

Corrigir vínculo cancelado e deeplink AdminUsers web

## Slice vertical

Slice 054 — Cancelamento da conta do responsável e restrição de acesso profissional

## Status final

done

## Decisões preservadas

- Remoção de vínculo cancelado continua usando `PATCH /patients/{id}/status` com `inactive` (única operação da API); copy ajustada para **inativar vínculo**, não remover fisicamente.
- **Reativar** só aparece quando `link.status === 'inactive'` e `guardian.subscriptionAccessGranted !== false`.
- Perfil restrito (`canceled` ou inativo sem assinatura) oculta conteúdo clínico e trilha; cancelado permite apenas inativar vínculo.
- Deeplink `profileId` em AdminUsers usa `catch` + `role="alert"` e limpa o query param no `finally`.

## Contexto utilizado

- Task 627, Slice 054, páginas Patients/PatientProfile/AdminUsers, util `patientLinkActions`, testes focados.

## Arquivos alterados

- `front-end/src/pages/Main/Patients/utils/patientLinkActions.ts` (novo)
- `front-end/src/pages/Main/Patients/index.tsx`
- `front-end/src/pages/Main/Patients/PatientProfile/index.tsx`
- `front-end/src/pages/Main/AdminUsers/index.tsx`
- testes correspondentes
- `tasks/change-requests/627-*.md`, `tasks/000-index.md`

## Validações executadas

- `npx vitest run` focado em Patients (18 testes) — passou na execução consolidada anterior; 2 timeouts intermitentes em rerun isolado.
- `npx vitest run -t "profileId deeplink"` AdminUsers — passou.
- eslint nos arquivos alterados — ok.

## Pendências

- Endurecer no backend a proibição de reativar vínculo inativo de conta cancelada (hoje bloqueado na UI via `subscriptionAccessGranted`).

## Próximo contexto recomendado

Retomar backlog normal.

## Contexto que não deve ser carregado

- Mobile, checkout, gateway Asaas completo.
