# Slice 065 - Autopreenchimento de endereço por CEP

## Status

done

## Objetivo de negócio

Ao digitar um CEP válido nos cadastros web de profissional e responsável, preencher automaticamente rua e cidade para reduzir atrito e erro de digitação.

## Entrega verificável

- Com CEP completo (8 dígitos), o formulário busca o endereço e preenche rua e cidade.
- Número permanece manual/opcional.
- CEP inválido ou não encontrado exibe feedback sem bloquear o restante do fluxo.
- Funciona em `/cadastro/profissional` e `/cadastro/responsavel`.

## Fora de escopo

- Backend próprio de CEP / proxy
- App mobile
- Autopreenchimento de número
- Edição de endereço no perfil pós-cadastro

## Decisões confirmadas

- Consulta client-side via ViaCEP (`https://viacep.com.br`).
- Mapeamento: `logradouro` → `street`, `localidade` → `city`.
- Ordem dos campos: CEP → Rua → Cidade → Número.

## Perfil do projeto

- stack web: front-end (React/Vite)
- mobile: sim (fora deste slice)

## Stacks envolvidas

- front-end

## Contrato

- N/A (integração externa ViaCEP; payload de registro já definido na Task 755)

## Tasks relacionadas

- `tasks/change-requests/757-autopreencher-endereco-por-cep-cadastro-web.md`

## Progresso

- Task 757 — done

## Risco de contexto

baixo — apenas front-end e dois formulários já existentes
