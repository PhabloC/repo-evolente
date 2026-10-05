# Task 764 - API: número obrigatório e complemento no endereço

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend

## Contrato

- `AddressData`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 069 — `tasks/slices/069-numero-obrigatorio-complemento-endereco.md`

## Criterios de aceite

- [x] number obrigatório no contrato/DTO
- [x] complement opcional + migration
- [x] Persistência e resposta pública

## Resultado da execucao

- Migration `1920000000000-AddAddressComplementToUsers`
- `AddressData.number` required; `complement` optional

## Handoff

- `.agents/state/handoffs/TASK-764.md`

## Validacoes executadas

- migration run — ok
- jest users + professionals — ok

## Pendencias pos-task

- Task 765

## Status final

done
