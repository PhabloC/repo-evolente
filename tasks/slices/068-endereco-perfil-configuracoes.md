# Slice 068 - Endereço no perfil (configurações)

## Status

done

## Objetivo de negócio

Permitir que profissional e responsável cadastrem/editem endereço em Configurações → Perfil (necessário para proximidade no diretório e dados de contato).

## Entrega verificável

- `PATCH /users/me` aceita `address`.
- Tela de Perfil (web) mostra e edita rua, CEP, cidade e número (opcional) para profissional e responsável.
- Autopreenchimento por CEP no formulário de edição.
- Resposta de `User`/`AuthUser` inclui `address`.

## Fora de escopo

- App mobile
- Master (sem seção de endereço nesta entrega)
- Validação geográfica avançada

## Decisões confirmadas

- Mesmo objeto `AddressData` do cadastro.
- Edição via `PATCH /users/me` (shared entre papéis).
- Autofill ViaCEP no client.

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim (fora)

## Stacks envolvidas

- contracts
- backend
- front-end

## Contrato

- `UpdateOwnProfileRequest.address`
- `User.address`

## Tasks relacionadas

- `tasks/change-requests/762-api-endereco-perfil-usuario.md`
- `tasks/change-requests/763-formulario-endereco-perfil-configuracoes-web.md`

## Progresso

- Task 762 — done
- Task 763 — done

## Risco de contexto

baixo-médio
