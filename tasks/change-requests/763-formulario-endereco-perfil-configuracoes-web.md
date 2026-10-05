# Task 763 - Formulário de endereço no perfil web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- Depende da Task 762

## Modo de execucao

single-stack

## Slice vertical

- Slice 068 — `tasks/slices/068-endereco-perfil-configuracoes.md`

## Criterios de aceite

- [x] Profissional e responsável veem/editam endereço no Perfil
- [x] Autofill CEP
- [x] Persistência via updateMyProfile

## Resultado da execucao

- Configurações → Perfil: campos CEP/rua/cidade/número para profissional e responsável.
- Autofill ViaCEP na edição.

## Handoff

- `.agents/state/handoffs/TASK-763.md`

## Arquivos alterados

- Settings page, AuthUser, adaptAuthResponse, userService

## Validacoes executadas

- ReadLints Settings — ok

## Pendencias pos-task

- Nenhuma

## Status final

done
