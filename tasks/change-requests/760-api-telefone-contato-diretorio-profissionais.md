# Task 760 - Telefone de contato no diretório de profissionais

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts
- backend

## Contrato

- `ProfessionalDirectoryItem.phone`

## Modo de execucao

cross-stack

## Slice vertical

- Slice 067 — `tasks/slices/067-modal-contato-profissional-diretorio.md`

## Criterios de aceite

- [x] Item do diretório inclui telefone de contato para WhatsApp
- [x] Clínica prioriza telefone da clínica
- [x] Testes atualizados

## Resultado da execucao

- Campo `phone` no diretório: clínica → clinicPhone; senão telefone do profissional.

## Handoff

- `.agents/state/handoffs/TASK-760.md`

## Arquivos alterados

- `contracts/openapi.yaml`
- `backend/.../professionals.service.ts(+spec)`

## Validacoes executadas

- jest professionals.service — ok

## Pendencias pos-task

- Task 761

## Status final

done
