# Task 238 - API: editar perfil responsável e criança (campos seguros)

## Status

done

## Tipo

shared

## Stacks envolvidos

backend, contracts

## Modo de execucao

cross-stack

## Slice vertical

`tasks/slices/010-app-responsavel-home-notificacoes.md`

## Contrato

`contracts/openapi.yaml` — `PATCH /guardians/me`, `PATCH /guardians/me/children/{childId}`

## Objetivo

Permitir que o responsável atualize apenas campos seguros: nome + parentesco; na criança, nome + sexo.

## Entrega verificavel

- OpenAPI atualizado
- Endpoints implementados e testados
- Campos sensíveis (CPF, e-mail, patientCode, birthDate da criança) fora do payload

## Fora de escopo

- UI mobile (Task 239)
- Alterar e-mail/CPF/senha

## Contexto minimo

- Esta task
- `guardians.controller.ts`, `guardians.service.ts`, repositórios
- `contracts/openapi.yaml`

## Orcamento de contexto

medio
