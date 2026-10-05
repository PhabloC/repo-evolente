# Task 762 - API de endereço no perfil do usuário

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend

## Contrato

- `PATCH /users/me` / `UpdateOwnProfileRequest.address`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 068 — `tasks/slices/068-endereco-perfil-configuracoes.md`

## Criterios de aceite

- [x] OpenAPI com address em UpdateOwnProfileRequest
- [x] DTO + service persistem endereço
- [x] Teste de updateOwnProfile com address

## Resultado da execucao

- `PATCH /users/me` aceita `address` e devolve `User.address`.

## Handoff

- `.agents/state/handoffs/TASK-762.md`

## Arquivos alterados

- openapi, UpdateOwnProfileDto, users.service(+spec)

## Validacoes executadas

- jest users.service.spec — ok

## Pendencias pos-task

- Task 763

## Status final

done
