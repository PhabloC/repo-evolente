# Task 756 - Formulários web de endereço no cadastro

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- Depende da Task 755

## Modo de execucao

single-stack

## Slice vertical

- Slice 064 — `tasks/slices/064-endereco-cadastro-profissional-responsavel.md`

## Criterios de aceite

- [x] Campos visíveis e obrigatórios (exceto número)
- [x] Submit envia `address`
- [x] Lint/testes focados ok

## Resultado da execucao

- Cadastro profissional e responsável coletam rua, CEP, cidade e número opcional.
- Máscara de CEP e validação alinhadas ao contrato.

## Handoff

- `.agents/state/handoffs/TASK-756.md`

## Arquivos alterados

- types address/professional/guardian
- utils/postalCode.ts
- RegisterProfessional + RegisterGuardian (+ schemas/tests)

## Validacoes executadas

- vitest RegisterGuardian — ok

## Pendencias pos-task

- Nenhuma

## Status final

done
