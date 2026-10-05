# Slice 064 - Endereço no cadastro de profissional e responsável

## Status

done

## Objetivo de negócio

Coletar endereço no cadastro público do profissional e do responsável para contato e futura operação comercial/clínica.

## Entrega verificável

- Cadastro profissional exige rua, CEP e cidade; número é opcional.
- Cadastro responsável exige os mesmos campos.
- Dados persistem no usuário e constam no contrato OpenAPI.
- Contas antigas sem endereço continuam válidas (campos nullable no banco).

## Fora de escopo

- App mobile (cadastro público é web)
- Edição de endereço no perfil pós-cadastro (pode ser task futura)
- Validação via ViaCEP / geocoding
- Endereço da clínica separado do endereço do profissional

## Decisões confirmadas

- Campos: `street` (rua), `postalCode` (CEP), `city` (cidade), `number` (número completo, opcional).
- Objeto aninhado `address` nos payloads de registro.
- Persistência na tabela `users` (compartilhada pelos dois papéis).

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim (fora deste slice)

## Stacks envolvidas

- contracts
- backend
- front-end

## Contrato

- `AddressData`
- `POST /professionals/register` (campo `address`)
- `POST /guardians/register` e `GuardianRegistrationData.address`
- `User.address` (resposta)

## Tasks relacionadas

- `tasks/change-requests/755-api-endereco-cadastro-profissional-responsavel.md`
- `tasks/change-requests/756-formulario-endereco-cadastro-web.md`

## Progresso

- Task 755 — done
- Task 756 — done

## Risco de contexto

médio — contrato + migration + dois formulários web
