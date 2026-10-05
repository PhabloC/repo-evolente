# Task 755 - API e contrato de endereço no cadastro

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend

## Contrato

- `AddressData`
- `POST /professionals/register`
- `POST /guardians/register` / `GuardianRegistrationData`
- `User.address`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 064 — `tasks/slices/064-endereco-cadastro-profissional-responsavel.md`

## Criterios de aceite

- [x] OpenAPI atualizado
- [x] Migration + entity + DTOs + services
- [x] Testes de registro cobrem endereço
- [x] Build backend ok

## Resultado da execucao

- Endereço obrigatório nos registros; número opcional; CEP com 8 dígitos.
- Colunas nullable em `users` para legado.
- `User.address` na resposta pública.

## Handoff

- `.agents/state/handoffs/TASK-755.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/common/dto/address-data.dto.ts`
- `backend/src/common/utils/postal-code.util.ts`
- `backend/src/database/migrations/1910000000000-AddAddressFieldsToUsers.ts`
- módulos users/professionals/guardians (entity, repos, DTOs, services, specs)

## Validacoes executadas

- jest professionals + guardians — ok
- nest build — ok

## Pendencias pos-task

- Rodar migration em ambientes com banco
- Task 756

## Status final

done
