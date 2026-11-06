# Slice 074 - Limite de três filhos por responsável

## Status

done

## Objetivo de negocio

O responsável autenticado cadastra no máximo três filhos na mesma conta, na web e no aplicativo.

## Entrega verificavel

- `POST /guardians/me/children` rejeita o quarto filho com mensagem clara.
- A web deixa de oferecer o cadastro quando a conta já tem três filhos.
- O app deixa de oferecer o cadastro quando a conta já tem três filhos.
- Filhos já existentes acima do teto permanecem; a conta só não recebe um novo.

## Fora de escopo

- Excluir ou inativar filhos para liberar vaga.
- Cobrança por filho.
- Cadastro de paciente feito pelo profissional fora de `POST /guardians/me/children`.

## Stacks envolvidas

- backend
- front-end
- mobile

## Contrato

- `POST /guardians/me/children`
- `GET /guardians/me/children`

## Tasks relacionadas

- Task 810

## Contexto mínimo

- `AGENTS.md`, `GUIDE.md`, `.agents/context-map.md`, `tasks/000-index.md`
- este slice

## Contexto sob demanda

- `contracts/openapi.yaml` no path `/guardians/me/children`
- criação de filho em `backend/src/modules/guardians/guardians.service.ts`
- páginas de filhos e cadastro em `front-end/src/pages/Main/Guardian/`
- seletor e cadastro em `mobile/src/features/children/`

## Orçamento de contexto

- baixo: uma regra, três pontos de entrada já existentes

## Status final

done
