# Task 500 - Contrato: trilha self-serve do responsável

## Status

done

## Tipo

shared

## Stacks envolvidos

- contracts (openapi)

## Perfil do projeto

- stack web escolhida: front-end (React/Vite)
- mobile: sim

## Contrato

- `contracts/openapi.yaml`

## Modo de execucao

single-stack

## Slice vertical

- `tasks/slices/047-trilha-self-serve-responsavel-mobile.md`

## Objetivo

Atualizar OpenAPI para trilhas do responsável: `professionalUserId` nullable; create/suggest/replace permitidos a `responsavel` sem vínculo; `TrailListResponse.canManage`; documentar ownership.

## Contexto minimo

- slice 047, openapi trails/Child schemas

## Orcamento de contexto

baixo

## Criterios de aceite

- [x] WeeklyTrail.professionalUserId nullable
- [x] descrições create/suggest/replaceItems para guardian self-serve
- [x] TrailListResponse.canManage
- [x] indice atualizado

## Status final

done
