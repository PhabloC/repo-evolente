# Task 757 - Autopreencher endereço por CEP no cadastro web

## Status

done

## Tipo

front

## Stacks envolvidos

- front-end

## Contrato

- N/A (ViaCEP externo; `AddressData` já existe)

## Modo de execucao

single-stack

## Slice vertical

- Slice 065 — `tasks/slices/065-autopreencher-endereco-por-cep.md`

## Contexto mínimo

- `AGENTS.md`
- `GUIDE.md`
- `.agents/context-map.md`
- `tasks/000-index.md`
- este arquivo
- `tasks/slices/065-autopreencher-endereco-por-cep.md`
- `.agents/state/handoffs/TASK-756.md`

## Contexto sob demanda

- formulários RegisterProfessional / RegisterGuardian
- `front-end/src/utils/postalCode.ts`

## Orçamento de contexto

baixo

## Criterios de aceite

- [x] Ao completar 8 dígitos do CEP, rua e cidade são preenchidos automaticamente
- [x] Número não é autopreenchido
- [x] Feedback de busca / CEP não encontrado
- [x] Mesmo comportamento nos dois cadastros
- [x] Testes focados ok

## Dependencias

- Task 756

## Resultado da execucao

- Consulta ViaCEP com debounce ao completar o CEP.
- Autopreenche `street` e `city` nos cadastros profissional e responsável.
- Ordem dos campos: CEP → Rua → Cidade → Número.
- Feedback "Buscando endereço..." e erro de CEP não encontrado.

## Contexto utilizado

- Slice 065, handoff 756, formulários de cadastro web, ViaCEP público

## Handoff

- `.agents/state/handoffs/TASK-757.md`

## Arquivos alterados

- `front-end/src/services/address/postalCodeLookup.ts`
- `front-end/src/services/address/postalCodeLookup.test.ts`
- `front-end/src/hooks/usePostalCodeAutofill.ts`
- `front-end/src/pages/Auth/RegisterProfessional/index.tsx`
- `front-end/src/pages/Auth/RegisterProfessional/index.test.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/index.tsx`
- `front-end/src/pages/Auth/RegisterGuardian/index.test.tsx`
- `tasks/slices/065-autopreencher-endereco-por-cep.md`
- `tasks/000-index.md`

## Validacoes executadas

- vitest postalCodeLookup + RegisterGuardian + RegisterProfessional — ok

## Pendencias pos-task

- Nenhuma

## Status final

done
