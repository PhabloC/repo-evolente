# TASK-751

## Slice

Slice 063 — diretório de profissionais para o responsável (web)

## Status

done

## Decisões preservadas

- Endpoint `GET /professionals` autenticado, papel `responsavel` + `AccessGrantedGuard`.
- Payload público: id, userId, name, avatarUrl, specialties, professionalRegistry, practiceType, clinicName, clinicPhone.
- Sem e-mail, CPF, CNPJ ou dados de assinatura.
- Busca por nome/especialidade + paginação page/pageSize.
- Circular dependency Professionals ↔ Subscriptions resolvida com `forwardRef`.

## Contexto usado

- `contracts/openapi.yaml`
- módulo `backend/src/modules/professionals/**`
- `UsersService.findActiveProfessionalsByIds`
- `backend/docs/ai/SECURITY.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/modules/professionals/**` (controller, service, repos, dto, module, spec)
- `backend/src/modules/users/users.service.ts`
- `backend/src/modules/subscriptions/subscriptions.module.ts`

## Validações

- `npx jest --runInBand professionals.service.spec --no-coverage` — ok
- `npm run build` (backend) — ok

## Pendências

- Task 752 consome o endpoint na web.

## Próximo contexto recomendado

- Task 752: `front-end/src/pages/Main/Guardian/Children/`, rotas, services/hooks.
- Não recarregar mobile nem Slice 053 inteiro.
