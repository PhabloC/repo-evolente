# Slice 069 - Número obrigatório e complemento no endereço

## Status

done

## Objetivo de negócio

Ajustar o endereço para exigir número e permitir complemento opcional (cadastro e perfil).

## Entrega verificável

- `AddressData.number` obrigatório; `complement` opcional.
- Migration com coluna `address_complement`.
- Formulários de cadastro (profissional/responsável) e Perfil atualizados.
- Contas legadas sem número continuam no banco (coluna nullable); novos envios exigem número.

## Fora de escopo

- Mobile
- Backfill de números vazios

## Decisões confirmadas

- Campos: street, city, postalCode, number (obrigatório), complement (opcional).
- Complemento não entra no critério de proximidade.

## Perfil do projeto

- stack web: front-end
- mobile: sim (fora)

## Stacks envolvidas

- contracts, backend, front-end

## Contrato

- `AddressData`

## Tasks relacionadas

- `tasks/change-requests/764-api-numero-obrigatorio-complemento-endereco.md`
- `tasks/change-requests/765-forms-numero-complemento-endereco-web.md`

## Progresso

- Task 764 — done
- Task 765 — done
