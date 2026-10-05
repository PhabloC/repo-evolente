# Task 758 - API de profissionais próximos no diretório

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend

## Contrato

- `GET /professionals`
- `ProfessionalDirectoryListResponse`
- `ProfessionalDirectoryItem`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 066 — `tasks/slices/066-profissionais-proximos-diretorio.md`

## Criterios de aceite

- [x] Response com `nearby`, `others`, totais e `referenceLocation`
- [x] Critério cidade/CEP documentado no OpenAPI
- [x] Item pode incluir `city` pública
- [x] Testes de serviço cobrem próximos vs distantes
- [x] Build/testes backend ok

## Resultado da execucao

- Diretório classifica por cidade (normalizada) ou CEP/prefixo 5 dígitos do responsável.
- `city` exposta no item; rua/CEP completo do profissional não.

## Contexto utilizado

- Slice 066, openapi diretório, professionals.service, users address

## Handoff

- `.agents/state/handoffs/TASK-758.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/src/common/utils/address-proximity.util.ts(+spec)`
- `backend/src/modules/professionals/professionals.service.ts(+spec)`
- `backend/src/modules/professionals/professionals.controller.ts`
- `backend/src/modules/users/users.service.ts`

## Validacoes executadas

- jest professionals.service + address-proximity — ok

## Pendencias pos-task

- Task 759

## Status final

done
