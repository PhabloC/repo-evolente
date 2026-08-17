# Task 501 - Backend: trilha self-serve do responsável

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Contrato

- Task 500 / openapi trails

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Dependencias

- Task 500

## Objetivo

Liberar create/suggest/replaceItems para responsável sem vínculo ativo; `professional_user_id` nullable; listar `canManage`; bloquear edição se houver vínculo profissional.

## Criterios de aceite

- [x] migration nullable professional_user_id
- [x] roles + assertCanManagePatientTrail / canManagePatientTrail
- [x] listByPatient retorna `{ items, canManage }`
- [x] testes unitários (guardian sem link / com link ativo)

## Status final

done
